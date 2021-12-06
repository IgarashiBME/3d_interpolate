#! /usr/bin/python
# coding:utf-8

import numpy as np
import scipy as sp
import scipy.interpolate

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import random

arr1 = np.arange(3)
arr2 = np.arange(3, 6)
arr3 = np.arange(6, 9)
res = np.stack((arr1,arr2,arr3), axis=1)

print(arr1.shape)
print(res)
