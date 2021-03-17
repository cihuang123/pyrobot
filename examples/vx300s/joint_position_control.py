# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Example for commanding robot with position control
"""

import time

from pyrobot import Robot


def main():
    sleep = [0, -1.7, -1.6, 0.0015, -1.110, -0.006]


    bot = Robot("vx300s", use_arm=True, use_base=False, use_camera=False, use_gripper=False)

    bot.arm.go_home()

    time.sleep(1)

    bot.arm.set_joint_positions(sleep, plan=True)

    time.sleep(1)

if __name__ == "__main__":
    main()
