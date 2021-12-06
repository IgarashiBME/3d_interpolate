import numpy as np
import csv

METER = 0.5

with open('ndt_pose.csv') as f:
    reader = csv.reader(f)
    x = np.array([])
    y = np.array([])
    z = np.array([])
    for row in reader:
        x = np.append(x, float(row[0]))
        y = np.append(y, float(row[1]))
        z = np.append(z, float(row[2]))

    x_dist = abs(min(x)) + max(x)
    print(x_dist)

    x_predict = np.linspace(min(x), max(x), int(x_dist))
    print(x_predict)
