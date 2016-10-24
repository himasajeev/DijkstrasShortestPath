from globals import *
import numpy as np

def update_V_X(v):
    for i in range(1, len(adjacency[v - 1])):
        w = adjacency[v - 1][i][0]
        for j in range(0, len(V_X)):
            if V_X[j][1] == w:
                V_X[j][0] = A[v - 1] + adjacency[v - 1][i][1]