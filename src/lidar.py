#!/usr/bin/env python
# -- coding: utf-8 --
import rospy
from sensor_msgs.msg import LaserScan
from laser_geometry import LaserProjection


class LaserToPointCloud:
    def __init__(self):
        self.laserProj = LaserProjection()
        self.laser_scan_subscriber = rospy.Subscriber(
            "/scan", LaserScan, self.scanCallback)

    def scanCallback(self, data):
        self.cloud = self.laserProj.projectLaser(data)
        print("LIDAR IN OPERATION")


if __name__ == '__main__':
    rospy.init_node('laser_to_pointcloud', anonymous=True)
    ltp = LaserToPointCloud()
    rospy.spin()