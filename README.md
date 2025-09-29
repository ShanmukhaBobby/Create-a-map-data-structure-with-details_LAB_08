Project: Smart Car Kit – Map Data Structure with Arduino & Raspberry Pi

This project demonstrates how to build a basic radar-style map system using an Arduino and Raspberry Pi. The Arduino is connected to an ultrasonic distance sensor, which continuously measures the distance of nearby objects. These distance values are then sent to the Raspberry Pi over a serial connection in a JSON-like format.

On the Raspberry Pi side, a Python script is used to:

Read the distance data coming from the Arduino.

Parse the data into a structured map data structure.

Use Matplotlib’s polar plotting to visualize the environment in real-time, creating a radar-style display.

The system works as follows:

Arduino Part

Sends out trigger pulses via the ultrasonic sensor.

Measures the time taken for the echo to return.

Converts this time into distance (in centimeters).

Transmits the distance as a JSON string (e.g., {"distance": 45}).

Raspberry Pi Part

Reads the serial data from the Arduino.

Uses Python and json to parse the distance values.

Maintains a map structure (array of distances) that represents 360° surroundings.

Updates the polar plot dynamically to visualize real-time obstacle detection.

Why a Map Data Structure?

The map here is represented as a circular buffer of distance values corresponding to angles (0°–360°). As new distances are read, older values are shifted, simulating a radar sweep effect. This allows the smart car kit to visualize its environment and detect obstacles effectively.

Applications

Obstacle avoidance in robotics.

Real-time radar simulation.

Autonomous navigation systems.
