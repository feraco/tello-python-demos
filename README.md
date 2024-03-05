# Tello Drone Python & Jupyter Notebooks 🚁🐍📓
This repository provides various Python and Jupyter Notebook examples of how to code Tello drones using Python. These coding examples were created by Frederick Feraco and are utilized in the "Science of Drones" course, teaching science research students at Walt WHitman HS and students at Five Towns College 🏫🎓.

This repository provides various approaches to program DJI's Tello drone using Python and Jupyter Notebooks. Whether you are using pure Python scripts or leveraging the interactive capabilities of Jupyter Notebooks, you'll find valuable examples and methods to get the most out of your Tello drone programming experience.

## Overview

Tello drones are not only fun to fly but also come with a robust programming interface that allows developers, students, and hobbyists to explore various aspects of drone technology. The examples provided in this repository range from basic flight commands to complex missions, like capturing a 360-degree panorama. Furthermore, these missions are accomplished by utilizing the extensive list of commands provided by Tello's SDK, which allows programmers to control the drone’s movement, camera, and retrieve real-time data about its state.

## Command Reference Table

Understanding the commands available in the Tello SDK is essential for effective drone programming. Below is a markdown table which provides a brief explanation, the actual code command, an example of how it might be used, and an explanation of the example for various SDK commands.

| Explanation                                          | Code Command                          | Example of Use                    | Explanation of Example                          |
|------------------------------------------------------|---------------------------------------|----------------------------------|-----------------------------------------------------------|
| Connects to the drone and initiates SDK mode.        | `tello.connect()`                     | `tello.connect()`                | Establishes a connection with the drone.                  |
| Sends a keepalive message to prevent auto-landing.   | `tello.send_keepalive()`              | `tello.send_keepalive()`         | Sends a signal to avoid automatic landing due to inactivity.|
| Turns motors on without flying (for cooling).        | `tello.turn_motor_on()`               | `tello.turn_motor_on()`          | Activates the motors without initiating flight for cooling purposes. |
| Turns off the motor cooling mode.                    | `tello.turn_motor_off()`              | `tello.turn_motor_off()`         | Deactivates the cooling mode by turning off the motors.   |
| Enables throw takeoff mode.                          | `tello.initiate_throw_takeoff()`      | `tello.initiate_throw_takeoff()` | Enables the mode that allows the drone to take off when thrown into the air. |
| Drone takes off automatically.                       | `tello.takeoff()`                     | `tello.takeoff()`                | Commands the drone to automatically take off.              |
| Drone lands automatically.                           | `tello.land()`                        | `tello.land()`                   | Commands the drone to land automatically.                  |
| Initiates video streaming from the drone.            | `tello.streamon()`                    | `tello.streamon()`               | Begins streaming video from the drone’s camera.            |
| Halts video streaming from the drone.                | `tello.streamoff()`                   | `tello.streamoff()`              | Stops streaming video from the drone’s camera.             |
| Stops all motors immediately.                        | `tello.emergency()`                   | `tello.emergency()`              | Instantly halts all motor functions.                       |
| Move the drone in a specified direction.             | `tello.move_forward()`                | `tello.move_forward(100)`        | Commands the drone to move forward by 100 units.          |
| Move the drone in a specified direction.             | `tello.move_left()`                   | `tello.move_left(100)`           |                                                           |
| Move the drone in a specified direction.             | `tello.move_backward()`               | `tello.move_backward(100)`       | Commands the drone to move forward by 100 units.          |
| Move the drone in a specified direction.             | `tello.move_right()`                  | `tello.move_right(100)`          |                                                           |
| Move the drone in a specified direction.             | `tello.move_up()`                     | `tello.move_up(100)`             |                                                           |
| Move the drone in a specified direction.             | `tello.move_down()`                   | `tello.move_down(100)`           |                                                           |
| Rotates the drone clockwise by x degrees.            | `tello.rotate_clockwise(x)`           | `tello.rotate_clockwise(90)`     | Rotates the drone clockwise by 90 degrees.                |
| Rotates the drone counter-clockwise by x degrees.    | `tello.rotate_counter_clockwise(x)`   | `tello.rotate_counter_clockwise(90)` | Rotates the drone counter-clockwise by 90 degrees.    |
| Flips the drone in a specified direction.            | `tello.flip(direction)`               | `tello.flip('l')`                | Commands the drone to perform a left flip.                 |
| Attains the state of the Tello                      | `tello.get_current_state()`           | `tello.get_current_state()`      |                                                           |
| Get a specific state field by name.                  | `tello.get_state_field(key)`          | `tello.get_state_field(key)`     |                                                           |
| ID of the currently detected mission pad.            | `tello.get_mission_pad_id()`          | `tello.get_mission_pad_id()`     |                                                           |
| X distance to current mission pad.                   | `tello.get_mission_pad_distance_x()`  | `tello.get_mission_pad_distance_x()` |                                                     |
| Y distance to current mission pad.                   | `tello.get_mission_pad_distance_y()`  | `tello.get_mission_pad_distance_y()` |                                                     |
| Z distance to current mission pad.                   | `tello.get_mission_pad_distance_z()`  | `tello.get_mission_pad_distance_z()` |                                                     |
| Get pitch in degree.                                 | `tello.get_pitch()`                   | `tello.get_pitch()`              |                                                           |
| Get roll in degree.                                  | `tello.get_roll()`                    | `tello.get_roll()`               |                                                           |
| Get yaw in degree.                                   | `tello.get_yaw()`                     | `tello.get_yaw()`                |                                                           |
| X-Axis Speed.                                        | `tello.get_speed_x()`                 | `tello.get_speed_x()`            |                                                           |
| Y-Axis Speed.                                        | `tello.get_speed_y()`                 | `tello.get_speed_y()`            |                                                           |
| Z-Axis Speed.                                        | `tello.get_speed_z()`                 | `tello.get_speed_z()`            |                                                           |
| X-Axis Acceleration.                                 | `tello.get_acceleration_x()`          | `tello.get_acceleration_x()`     |                                                           |
| Y-Axis Acceleration.                                 | `tello.get_acceleration_y()`          | `tello.get_acceleration_y()`     |                                                           |
| Z-Axis Acceleration.                                 | `tello.get_acceleration_z()`          | `tello.get_acceleration_z()`     |                                                           |
| Get lowest temperature in °C.                        | `tello.get_lowest_temperature()`      | `tello.get_lowest_temperature()` |                                                           |
| Get highest temperature in °C.                       | `tello.get_highest_temperature()`     | `tello.get_highest_temperature()`|                                                           |
| Get average temperature in °C.                       | `tello.get_temperature()`             | `tello.get_temperature()`        |                                                           |
| Get current height in cm.                            | `tello.get_height()`                  | `tello.get_height()`             |                                                           |
| Get current distance value from TOF in cm.           | `tello.get_distance_tof()`            | `tello.get_distance_tof()`       |                                                           |
| Get current barometer measurement in cm.             | `tello.get_barometer()`               | `tello.get_barometer()`          |                                                           |
| Get the time the motors have been active in seconds. | `tello.get_flight_time()`             | `tello.get_flight_time()`        |                                                           |
| Get current battery percentage.                      | `tello.get_battery()`                 | `tello.get_battery()`            |                                                           |
| Get the UDP video address.                           | `tello.get_udp_video_address()`       | `tello.get_udp_video_address()`  |                                                           |
| Get the BackgroundFrameRead object from the camera drone. | `tello.get_frame_read()`          | `tello.get_frame_read()`         |                                                           |


## Missions

Various mission examples have been provided in both Python script (.py) and Jupyter Notebook (.ipynb) formats. These missions explore diverse functionalities such as taking off, landing, streaming video, capturing photos, and complex navigational operations. Some missions specifically explore the drone’s photographic capabilities, flying through scenic routes, and capturing images at predefined waypoints.


   
## Prerequisites

Before running the code examples, ensure that you have the necessary software and libraries installed:
- Python 3.x
- Jupyter Notebook (if running .ipynb files)
- Necessary Python libraries: `numpy`, `opencv-python`, etc.
- Ensure your machine is connected to the Tello's Wi-Fi network for direct communication.

  ## Contribution 🤝
This repository encourages the scientific community, especially students and researchers, to contribute and enhance the ways in which Tello drones can be utilized for educational purposes. Feel free to submit a pull request or share insights on additional functionalities.

## Acknowledgements 🙏
Special thanks to Five Towns College and all the inquisitive minds in the "Science of Drones" course. May your curiosity continue to soar to new heights!

Created with ❤️ by Frederick Feraco.

## Getting Started

1. **Clone the Repository:**
   ```sh
   git clone [https://github.com/[your-github-username]/tello-drone-python-jupyter.git](https://github.com/feraco/tello-python-demos.git](https://github.com/feraco/tello-python-demos.git)https://github.com/feraco/tello-python-demos.git)
