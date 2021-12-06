#! /usr/bin/python
# coding:utf-8

import numpy as np
import scipy as sp
import scipy.interpolate

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

# Figureを追加
fig = plt.figure(figsize = (8, 8))

# 3DAxesを追加
ax = fig.add_subplot(111, projection='3d')

# Axesのタイトルを設定
ax.set_title("ndt_pose", size = 20)

# 軸ラベルを設定
ax.set_xlabel("x", size = 14)
ax.set_ylabel("y", size = 14)
ax.set_zlabel("z", size = 14)

# 軸目盛を設定
#ax.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
#ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])
#ax.set_zticks([-1.0, 0.0, 1.0])
ax.set_zlim(-1.0, 10.0)

with open('ndt_pose.csv') as f:
    reader = csv.reader(f)
    x = np.array([])
    y = np.array([])
    z = np.array([])
    for row in reader:
        x = np.append(x, float(row[0]))
        y = np.append(y, float(row[1]))
        z = np.append(z, float(row[2]))
    #print(x)
    #print min(x), max(x)

# grid
x_grid = np.linspace(min(x), max(x), 30)
y_grid = np.linspace(min(y), max(y), 30)
B1, B2 = np.meshgrid(x_grid, y_grid, indexing='xy')
Z = np.zeros((x.size, z.size))

# interpolation
spline = sp.interpolate.Rbf(x,y,z,function='thin_plate',smooth=5, episilon=5)
Z = spline(B1,B2)

print(B1.size, B2.size, Z.size)
#print(B1)

# view
ax.plot_wireframe(B1, B2, Z)
ax.plot(x, y, z, color = "red")
plt.show()
