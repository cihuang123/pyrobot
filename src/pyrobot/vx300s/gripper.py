# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from interbotix_sdk.robot_manipulation_vx300s_short import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd
import rospy
from pyrobot.core import Gripper


class vx300sGripper(Gripper):
    """
    Interface for gripper.
    """

    def __init__(self, configs, wait_time=2.0):
        """
        :param wait_time: waiting time for opening/closing gripper
        :type wait_time: float
        """
        self.gripper = InterbotixRobot(robot_name="vx300s", mrd=mrd)
        self.wait_time = wait_time

    def open(self, position=None, wait=True):
        """
        @brief Opens the gripper (when in 'pwm' control mode)

        :param wait: True if blocking call and will return after
                     target_joint is achieved, False otherwise
        :type wait: bool
        """
        self.gripper.open_gripper(2.0)
        if wait:
            rospy.sleep(self.wait_time)

    def set_gripper_pressure(self, pressure):
        """
	@brief Set the amount of pressure that the gripper should use when grasping an object (when in 'pwm' control mode)
	@param pressure - a scaling factor from 0 to 1 where the pressure increases as the factor increases
        """
        self.gripper.set_gripper_pressure(pressure)

    def close(self, position=None, wait=True):
        """
        @brief Closes the gripper (when in 'pwm' control mode)

        :param wait: True if blocking call and will return after
                     target_joint is achieved, False otherwise
        :type wait: bool
        """
        self.gripper.close_gripper(2.0)
        if wait:
            rospy.sleep(self.wait_time)
