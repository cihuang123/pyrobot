import time
from pyrobot import Robot

# This script closes and opens the gripper twice, changing the gripper pressure half way through
#
# To get started, open a terminal and type 'roslaunch interbotix_sdk arm_run.launch robot_name:=wx200 use_time_based_profile:=true gripper_operating_mode:=pwm'
# Then change to this directory and type 'python gripper_control.py'

def main():
    arm = Robot("vx300s", use_arm=True, use_base=False, use_camera=False, use_gripper=True)
    arm.gripper.close()

    arm.gripper.open()

    arm.gripper.set_gripper_pressure(0.8)

    arm.gripper.close()

    arm.gripper.open()

if __name__=='__main__':
    main()
