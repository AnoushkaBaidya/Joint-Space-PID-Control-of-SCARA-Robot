# JOINT SPACE PID CONTROL OF SCARA ROBOT

## 1. Creating the Robot

### 1.1 Robot Creation

* Detailed steps for creating the SCARA robot in Gazebo simulator.
* Ensure all necessary components and configurations are correctly set up.

## 2. Forward Kinematics

### 2.1 Node Implementation

* **Subscription**: Reads joint values from the Gazebo simulator.
* **Calculation**: Computes the end-effector pose.
* **Publication**: Publishes the pose as a ROS topic.

## 3. Inverse Kinematics

### 3.1 Node Implementation

* **Service Client**: Takes a desired end-effector pose from the user.
* **Response**: Returns joint positions.

## 4. Controlling the Robot Joints

### 4.1 PD Controller

* **Implementation**: Reads joint values and receives reference joint values through a service.
* **Publishing**: Publishes joint efforts back to the SCARA robot.
* **Control Input**:
  \[
  U = -K_p \cdot e - K_d \cdot e_{dot}
  \]
  where:
  - \( K_p \) = Proportional Gain
  - \( K_d \) = Derivative Gain
  - \( e \) = ( \( X_{ref} \) - \( X \) )
  - \( e_{dot} \) = \(\frac{e(current\_time) - e(previous\_time)}{current\_time - previous\_time}\)

### 4.2 Tuning

* **Proportional Gain (Kp)**: Adjusted for fast convergence and minimal overshoot.
* **Derivative Gain (Kd)**: Optimized for stability.

## 5. Moving the Robot on a Linear Path

### 5.1 Velocity Level Kinematics

* **Calculations**: Computes end-effector and joint velocities using the Jacobian matrix.
* **Services**:
  1. Converts joint velocities to end-effector velocities.
  2. Converts end-effector velocities to joint velocities.

### 5.2 Velocity Controller

* **Implementation**: Added a reference velocity compared with the desired velocity to find the cumulative error.
* **Tuning**: Increased the value of Kp while keeping one of the joints constant for optimal performance.

## 6. Simulation Videos

### 6.1 Videos

* **Video 1**: Velocity in the x and y directions is 0, whereas in the z direction, the velocity is 1 unit.

[![Video 1](https://github.com/AnoushkaBaidya/Joint-Space-PID-Control-of-SCARA-Robot/assets/115124698/fbbddbe8-9814-4526-aa56-4791554d30be)](https://github.com/AnoushkaBaidya/Joint-Space-PID-Control-of-SCARA-Robot/assets/115124698/fbbddbe8-9814-4526-aa56-4791554d30be)

* **Video 2**: Velocity in the x direction is 0, whereas in the y and z directions, the velocity is 1 unit.

[![Video 2](https://github.com/AnoushkaBaidya/Joint-Space-PID-Control-of-SCARA-Robot/assets/115124698/48d0739d-add1-47ad-b8f9-32c5c622bce5)](https://github.com/AnoushkaBaidya/Joint-Space-PID-Control-of-SCARA-Robot/assets/115124698/48d0739d-add1-47ad-b8f9-32c5c622bce5)

* **Video 3**: Velocity in all directions is 1 unit.

[![Video 3](https://github.com/AnoushkaBaidya/Joint-Space-PID-Control-of-SCARA-Robot/assets/115124698/ea9821a8-2349-47a7-a66e-5ca6d50d0b89)](https://github.com/AnoushkaBaidya/Joint-Space-PID-Control-of-SCARA-Robot/assets/115124698/ea9821a8-2349-47a7-a66e-5ca6d50d0b89)

---
