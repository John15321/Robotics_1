"""
Module contains rotations for robotics.
"""
import numpy as numpy
import matplotlib.pyplot as plt
import sympy as sp
from sympy import print_latex


def rot_z_fun(alpha):
    return sp.Matrix([
        [sp.cos(alpha), -sp.sin(alpha), 0],
        [sp.sin(alpha),  sp.cos(alpha), 0],
        [0,              0,             1]
    ])


def rot_x_fun(beta):
    return sp.Matrix([
        [1,  0,             0],
        [0,  sp.cos(beta), -sp.sin(beta)],
        [0,  sp.sin(beta),  sp.cos(beta)]
    ])


def rot_y_fun(gamma):
    return sp.Matrix([
        [sp.cos(gamma), 0, sp.sin(gamma)],
        [0,             1, 0],
        [-sp.sin(gamma), 0, sp.cos(gamma)]
    ])


R = sp.Matrix([
    [sp.cos(q1 + q1),  -sp.sin(q1+q2), 0],
    [-sp.sin(q1 + q2),  sp.cos(q1 + q2), 0],
    [0,  0,  1]
])
