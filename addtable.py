import nbformat as nbf
import os

table_markdown = """| Explanation                                          | Code Command                          | Example of Use                    | Explanation of Example                                    |
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

"""

# You can then use this `table_markdown` string with the script provided in the previous message.


def add_table_to_notebook(notebook_path, table_markdown):
    with open(notebook_path, 'r') as f:
        nb = nbf.read(f, as_version=4)
    
    # Creating a new markdown cell with the table at the top.
    new_cells = [nbf.v4.new_markdown_cell(table_markdown)] + nb.cells
    
    # Assigning the modified cells back to the notebook.
    nb.cells = new_cells
    
    # Writing the modified notebook back to file.
    with open(notebook_path, 'w') as f:
        nbf.write(nb, f)

def add_table_to_all_notebooks(directory_path, table_markdown):
    for filename in os.listdir(directory_path):
        if filename.endswith(".ipynb"):
            notebook_path = os.path.join(directory_path, filename)
            add_table_to_notebook(notebook_path, table_markdown)

# Example usage:
# Replace 'path_to_your_directory' with the path to your directory containing the notebooks.
add_table_to_all_notebooks('/Users/wwhs-research/Downloads/UPH_DJITello-main/Sensors', table_markdown)
