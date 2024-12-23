import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from tf2_ros import TransformListener, Buffer
from geometry_msgs.msg import TransformStamped, Point
import math
from message_filters import Subscriber, ApproximateTimeSynchronizer

class LaserFusionNode(Node):
    def __init__(self):
        super().__init__('laser_fusion_node')

        # TF listener and buffer
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # Publishers and subscribers
        self.publisher = self.create_publisher(LaserScan, '/laser/all_laser', 10)

        # Create message filters for synchronization
        self.front_laser_sub = Subscriber(self, LaserScan, '/laser/front_laser')
        self.back_laser_sub = Subscriber(self, LaserScan, '/laser/back_laser')

        # Synchronize the laser topics with approximate time
        self.sync = ApproximateTimeSynchronizer(
            [self.front_laser_sub, self.back_laser_sub],
            queue_size=10,
            slop=0.01
        )
        self.sync.registerCallback(self.laser_callback)

        # Rotation angle in radians
        self.rotation_angle = math.pi / 2

        self.get_logger().info('Laser fusion node initialized.')

    def laser_callback(self, front_msg, back_msg):
        try:
            # Get transforms from laser frames to all_laser_link
            front_transform = self.tf_buffer.lookup_transform('all_laser_link', 'front_laser_link', rclpy.time.Time())
            back_transform = self.tf_buffer.lookup_transform('all_laser_link', 'back_laser_link', rclpy.time.Time())

            # Create the fused LaserScan message
            fused_scan = LaserScan()
            fused_scan.header.stamp = front_msg.header.stamp  # Using the front laser timestamp
            fused_scan.header.frame_id = 'all_laser_link'

            # Set parameters for fused scan (using one laser's range_min and range_max)
            fused_scan.range_min = front_msg.range_min
            fused_scan.range_max = front_msg.range_max

            # Set the full angular range for the combined scan
            min_angle = -math.pi
            max_angle = math.pi
            fused_scan.angle_min = min_angle
            fused_scan.angle_max = max_angle
            fused_scan.angle_increment = (max_angle - min_angle) / 360

            # Transform and combine laser ranges
            fused_scan.ranges = self.transform_laser_data(front_msg, front_transform) + \
                                self.transform_laser_data(back_msg, back_transform)

            # Apply custom rotation around Z-axis to all points
            fused_scan.ranges = self.apply_rotation(fused_scan.ranges, fused_scan.angle_min, fused_scan.angle_increment)

            # Set intensities to 0.0 for each range
            fused_scan.intensities = [0.0] * len(fused_scan.ranges)

            # Publish the fused data
            self.publisher.publish(fused_scan)

        except Exception as e:
            self.get_logger().error(f'Error in laser fusion: {str(e)}')

    def transform_laser_data(self, msg, transform):
        # Apply the transformation to each laser scan range
        transformed_ranges = []
        default_range = msg.range_max  # Set to the laser's maximum range
        for i, range_value in enumerate(msg.ranges):
            if math.isnan(range_value) or math.isinf(range_value):
                range_value = default_range

            # Convert each range to a point (x, y) in polar coordinates
            angle = msg.angle_min + i * msg.angle_increment
            x = range_value * math.cos(angle)
            y = range_value * math.sin(angle)

            # Apply the transform (rotation and translation)
            transformed_point = self.apply_transform_to_point(x, y, transform)

            # Convert back to polar coordinates (range)
            transformed_range = math.sqrt(transformed_point.x**2 + transformed_point.y**2)

            # Check if transformed range is valid
            if math.isnan(transformed_range) or math.isinf(transformed_range):
                self.get_logger().warn(f"Invalid transformed range at index {i}: {transformed_range}")
                continue

            transformed_ranges.append(transformed_range)

        return transformed_ranges

    def apply_transform_to_point(self, x, y, transform):
        # Apply translation and rotation to the point (x, y) using the transform
        rotation = transform.transform.rotation
        translation = transform.transform.translation

        # Apply rotation (2D rotation matrix)
        x_new = rotation.w * x - rotation.z * y + translation.x
        y_new = rotation.z * x + rotation.w * y + translation.y

        # Ignore invalid points
        if math.isnan(x_new) or math.isnan(y_new):
            return None

        # Return the transformed point
        transformed_point = Point()
        transformed_point.x = x_new
        transformed_point.y = y_new
        transformed_point.z = 0.0  # Correcting the z-coordinate to 0.0 for 2D

        return transformed_point

    def apply_rotation(self, ranges, angle_min, angle_increment):
        rotated_ranges = [float('nan')] * len(ranges)  # Initialize with NaNs for invalid ranges
        num_points = len(ranges)

        for i, range_value in enumerate(ranges):
            if math.isnan(range_value) or math.isinf(range_value):
                continue

            # Calculate the original angle
            original_angle = angle_min + i * angle_increment

            # Rotate by the specified angle
            rotated_angle = original_angle + self.rotation_angle
            if rotated_angle > math.pi:
                rotated_angle -= 2 * math.pi  # Wrap angle to [-pi, pi]
            elif rotated_angle < -math.pi:
                rotated_angle += 2 * math.pi

            # Find the new index after rotation
            new_index = int((rotated_angle - angle_min) / angle_increment)
            if 0 <= new_index < num_points:
                rotated_ranges[new_index] = range_value

        return rotated_ranges


def main(args=None):
    rclpy.init(args=args)
    node = LaserFusionNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
