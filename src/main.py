#!/usr/bin/env python
# -- coding: utf-8 --
import cv2
import rospy
import numpy as np
from calibration import Calibration
from lidar import LaserToPointCloud
import sensor_msgs.point_cloud2 as pc2

if __name__ == '__main__':
    rospy.init_node('main_node', anonymous=True)

    # Laser to pointcloud
    ltp = LaserToPointCloud()

    # Calculate intrinsic, extrinsic parameter
    calibration = Calibration()

    # Open the video. When `ls -ltrh /dev/video*` is entered in the terminal, enter the number corresponding to *
    cap = cv2.VideoCapture(2)

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Read points from the cloud
            points = pc2.read_points(ltp.cloud)
            points_list = list(points)
            # Points consist of world-coordinate x, y, z, intensity and ring
            # We only use (x, y, z)
            points_list = [(x, y, z) for x, y, z, _, _ in points_list]

            print("Length of points: ", len(points_list))
            print("First few elements of points: ", points_list[:10])

            # Convert to numpy array and reshape
            objPoints = np.array(points_list, dtype=np.float32).reshape(-1, 3)

            # Display the annotated frame
            img_points, jacobian = cv2.projectPoints(
                objPoints, calibration.rvec, calibration.tvec, calibration.cameraMatrix, np.array([0, 0, 0, 0], dtype=float))
            print("Shape of img_points: ", img_points.shape)
            print("First few elements of img_points: ", img_points[:5])

            for i in range(len(img_points)):
                # Express Lidar points to image using circle
                cv2.circle(frame, (int(img_points[i][0][0]), int(
                    img_points[i][0][1])), 3, (0, 0, 255), 1)

            cv2.imshow("image", frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()