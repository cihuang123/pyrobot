# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Example for commanding robot to specific gripper pose
"""
import time

import numpy as np
from pyrobot import Robot


def main():
    # Example poses
    # orientation can be either rotation matrix or quaternion
    target_poses = [
        {
            "position": np.array([0.18, 0.0, 0.15]),
            "orientation": np.array([0, 1.57, 0]),
        },
    ]
    bot = Robot("vx300s", use_arm=True, use_base=False, use_camera=False, use_gripper=False)

    bot.arm.go_home()

    time.sleep(1)

    for pose in target_poses:
        bot.arm.set_ee_pose(plan=True, **pose)
        time.sleep(2)

    bot.arm.go_home()

    # Forward Kinematics Example
    angles = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    print(bot.arm.compute_fk_position(angles, "vx300s/ee_arm_link"))


if __name__ == "__main__":
    main()
