import numpy as np

# Time step (seconds)
dt = 0.1

# State vector: [x, y, vx, vy]
x = np.array([[0], [0], [0], [0]])

# State transition matrix
F = np.array([[1, 0, dt, 0],
              [0, 1, 0, dt],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

# Control input matrix (acceleration from IMU)
B = np.array([[0.5*dt**2, 0],
              [0, 0.5*dt**2],
              [dt, 0],
              [0, dt]])

# Measurement matrix (position from odometry or beacon)
H = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0]])

# Process noise covariance
Q = np.eye(4) * 0.01

# Measurement noise covariance
R = np.eye(2) * 0.1

# Initial covariance
P = np.eye(4)

# Example IMU acceleration data (ax, ay)
imu_data = [[0.1, 0.0], [0.1, 0.05], [0.0, 0.1], [-0.05, 0.0]]

# Example odometry measurements (x, y)
odom_data = [[0.0, 0.0], [0.01, 0.0], [0.03, 0.005], [0.04, 0.02]]

def kalman_filter(x, P, z, u):
    # Prediction
    x_pred = F @ x + B @ u
    P_pred = F @ P @ F.T + Q

    # Measurement update
    y = z - (H @ x_pred)              # Innovation
    S = H @ P_pred @ H.T + R          # Innovation covariance
    K = P_pred @ H.T @ np.linalg.inv(S) # Kalman gain

    x_new = x_pred + K @ y
    P_new = (np.eye(len(x)) - K @ H) @ P_pred
    return x_new, P_new

positions = []

for i in range(len(imu_data)):
    u = np.array(imu_data[i]).reshape(2, 1)
    z = np.array(odom_data[i]).reshape(2, 1)
    x, P = kalman_filter(x, P, z, u)
    positions.append(x[:2].flatten())

print("Estimated positions:\n", positions)




