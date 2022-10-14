#!/usr/bin/env python3
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys


def perform_trajectory():
    rospy.init_node('mikasa_trajectory_node')
    controller_name = '/mikasa_controller/command'
    trajectory_publisher = rospy.Publisher(controller_name,JointTrajectory, queue_size=10)
    argv = sys.argv[1:]
    mikasa_joints = ['joint_1', 'joint_2', 'joint_3', 'joint_4']
    goal_positions = [float(argv[0]), float(argv[1]), float(argv[2]), float(argv[3])]

    rospy.loginfo("goal position set lets go!")
    rospy.sleep(1)


    trajectory_msg = JointTrajectory()
    trajectory_msg.joint_names = mikasa_joints
    trajectory_msg.points.append(JointTrajectoryPoint())
    trajectory_msg.points[0].positions = goal_positions
    trajectory_msg.points[0].velocities = [0.0 for i in mikasa_joints]
    trajectory_msg.points[0].accelerations = [0.0 for i in mikasa_joints]
    trajectory_msg.points[0].time_from_start = rospy.Duration(3)


if __name__ == '__main__':
    perform_trajectory()