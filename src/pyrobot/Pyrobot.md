# pyrobot Class Diagram

---
title : allegro_hand
---
```mermaid
classDiagram
    Gripper <|-- AllegroHand : Inhirit
    Robot o-- Gripper : Aggregation
    class Robot{
        __init__()
    }
    class Gripper{
        __init__()
        open()
        close()
    }
    class AllegroHand{
        __init__()
        set_primitive()
        go_home()
        move_to_neutral()
        set_joint_velocities()
        set_joint_positions()
        get_joint_angles()
        get_joint_velocities()
        get_joint_torques()
        get_joint_angle()
        get_joint_velocity()
        get_joint_torque()
        set_joint_torques()
        _pub_joint_torques()
        _callback_joint_states()
        _pub_joint_positions()
        _angle_error_is_small()
        _setup_joint_pub()
        _setup_torque_pub()
        _setup_primitive_pub()
        open()
        close()
    } 
```

---
title : azure_kinect
---
```mermaid
classDiagram
    Camera <|-- Kinect2Camera : Inhirit
    Kinect2Camera <|-- AzureKinectCamera : Inhirit
    class Camera{
    __init__()
    _sync_callback()
    _camera_info_callback()
    get_rgb()
    get_depth()
    get_rgb_depth()
    get_intrinsics()
    }
    

```

---
title : core
---
```mermaid
classDiagram
    Robot o-- Base : Aggregation
    Robot o-- Gripper : Aggregation
    Robot o-- Camera : Aggregation
    Robot o-- Arm : Aggregation

```

---
title : habitat
---
```mermaid
classDiagram
    Robot o-- LoCoBotBase : Aggregation
    Robot o-- LoCoBotCamera : Aggregation

```

---
title : kinect2
---
```mermaid
classDiagram
    Camera <|-- Kinect2Camera : Inhirit

```

---
title : locobot
---
```mermaid
classDiagram
    Arm <|-- LoCoBotArm : Inhirit
    Base <|-- LoCoBotBase : Inhirit
    SimpleCamera <|-- LoCoBotCamera : Inhirit
    Camera <|-- SimpleCamera : Inhirit
    Gripper <|-- LoCoBotGripper : Inhirit
    TrajectoryTracker <|-- ILQRControl : Inhirit
    BaseSafetyCallbacks <|-- BaseState : Inhirit
    Robot o-- LoCoBotGripper : Aggregation
    Robot o-- LoCoBotGripper : Aggregation
    Robot o-- LoCoBotCamera : Aggregation
    Robot o-- LoCoBotArm : Aggregation

```

---
title : sawyer
---
```mermaid
classDiagram
    Arm <|-- SawyerArm : Inhirit
    Gripper <|-- SawyerGripper : Inhirit
    SawyerArm *-- SawyerGripper : Composition
    Robot o-- Arm : Aggregation
    Robot o-- Gripper : Aggregation

```

---
title : ur5
---
```mermaid
classDiagram
    Arm <|-- UR5Arm : Inhirit
    Gripper <|-- AllegroHand : Inhirit
    UR5Arm o-- AllegroHand : Aggregation
    Robot o-- Arm : Aggregation
    Robot o-- Gripper : Aggregation

```

---
title : ur5
---
```mermaid
classDiagram
    MoveitObjectHandler *-- PlanningSceneInterface : Composition

```

---
title : vrep_locobot
---
```mermaid
classDiagram
    Robot o-- LoCoBotBase : Aggregation
    Robot o-- LoCoBotGripper : Aggregation
    Robot o-- LoCoBotCamera : Aggregation
    Robot o-- LoCoBotArm : Aggregation

```

---
title : vx300s
---
```mermaid
classDiagram
    Arm <|-- vx300sArm : Inhirit
    Camera <|-- SimpleCamera : Inhirit
    SimpleCamera <|-- LoCoBotCamera : Inhirit
    vx300sArm *-- vx300sGripper : Composition
    LoCoBotCamera o-- DepthImgProcesso : Aggregation
    vx300sArm o-- LoCoBotCamera : Aggregation
    Robot o-- LoCoBotGripper : Aggregation
    Robot o-- LoCoBotGripper : Aggregation
    Robot o-- LoCoBotCamera : Aggregation
    Robot o-- LoCoBotArm : Aggregation

```

