# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from pyrobot.cfg.config import get_cfg_defaults

_C = get_cfg_defaults()

_C.HAS_BASE = False
_C.HAS_CAMERA = False

_ARMC = _C.ARM
_ARMC.CLASS = "vx300sArm"
_ARMC.ARM_ROBOT_DSP_PARAM_NAME= "vx300s/robot_description"
_ARMC.MOVEGROUP_NAME = "interbotix_arm"
_ARMC.ARM_BASE_FRAME = "vx300s/base_link"
_ARMC.EE_FRAME = "vx300s/ee_arm_link"
_ARMC.ROSTOPIC_JOINT_STATES = "vx300s/joint_states"
_ARMC.JOINT_NAMES = [
    "waist",
    "shoulder",
    "elbow",
    "forearm_roll",
    "wrist_angle",
    "wrist_rotate",
]

_ARMC.ARM_MAX_JOINT_VELOCITY = 0.6

_ARMC.IK_POSITION_TOLERANCE = 0.01
_ARMC.IK_ORIENTATION_TOLERANCE = 0.1

_GRIPPERC = _C.GRIPPER
# # GRIPPER class name
_GRIPPERC.CLASS = 'vx300sGripper'
# # maximum gripper open position
_GRIPPERC.GRIPPER_MAX_POSITION = 0.041667
# # minimum gripper open position
_GRIPPERC.GRIPPER_MIN_POSITION = 0.0
# # maximum gripper movement velocity
_GRIPPERC.GRIPPER_MAX_VELOCITY = 3.0
# # minimum gripper movement velocity
_GRIPPERC.GRIPPER_MIN_VELOCITY = 0.15


def get_cfg():
    return _C.clone()
