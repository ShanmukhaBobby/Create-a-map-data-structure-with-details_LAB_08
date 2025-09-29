import serial
import json
import time
import matplotlib.pyplot as plt
import numpy as np

# --- Connect to Arduino ---
ser = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
time.sleep(2)  # Give Arduino time to reset

# --- Initialize Map ---
max_distance = 100  # Maximum distance in cm to display
num_points = 360    # Degrees in radar
angles = np.linspace(0, 2*np.pi, num_points)

# Placeholder for distances (initially max_distance)
distances = np.ones(num_points) * max_distance

# Setup matplotlib figure
plt.ion()  # Interactive mode on
fig, ax = plt.subplots(subplot_kw={'projection':'polar'})
sc = ax.scatter(angles, distances, c='red')
ax.set_rmax(max_distance)
ax.set_rticks([20, 40, 60, 80, 100])
ax.set_theta_zero_location('N')  # 0° at top
ax.set_theta_direction(-1)

def update_plot(distances):
    sc.set_offsets(np.c_[angles, distances])
    fig.canvas.draw()
    fig.canvas.flush_events()

# --- Main Loop ---
while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    data = json.loads(line)
                    distance = data["distance"]

                    # Shift distances to create a moving radar effect
                    distances = np.roll(distances, -1)
                    distances[-1] = min(distance, max_distance)  # Keep max distance limit

                    update_plot(distances)
                except Exception as e:
                    print("Parse error:", line, e)
    except KeyboardInterrupt:
        print("Exiting...")
        break
