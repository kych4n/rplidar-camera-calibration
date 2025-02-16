import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def pose_callback(msg):
    position = msg.pose.pose.position
    orientation = msg.pose.pose.orientation

    print(f"X: {position.x}, Y: {position.y}, Z: {position.z}")
    print(f"Orientation (Quaternion): x={orientation.x}, y={orientation.y}, z={orientation.z}, w={orientation.w}")

def listener():
    rospy.init_node('pose_listener', anonymous=True)
    rospy.Subscriber('/initialpose', PoseWithCovarianceStamped, pose_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()