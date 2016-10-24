from globals import *
from functions import *

import numpy as np



print adjacency
print adjacency[0]   #which v
print adjacency[0][1]  #v's first neighbour info
print adjacency[0][1][0]  #name of v's first neighbour
print adjacency[0][1][1]  #the distance of edge connecting v's first neighbour
#Edges = np.delete(Edges, r, axis=0)

X.append(adjacency[0][0][0])

v = adjacency[0][0][0]

V_X = np.delete(V_X, v-1, axis=0)

def update_V_X(v):
    for i in range(1, len(adjacency[v - 1])):
        w = adjacency[v - 1][i][0]
        for j in range(0, len(V_X)):
            if V_X[j][1] == w:
                oldMin = V_X[j][0]
                newMin = A[v - 1] + adjacency[v - 1][i][1]
                if oldMin > newMin:
                    V_X[j][0] = A[v - 1] + adjacency[v - 1][i][1]




def growX():
    min = 1000000
    for i in range(0, len(V_X)):
        greed = V_X[i][0]
        if greed < min:
            min = greed
            w = V_X[i][1]

    A[w-1] = min

    return w

print "V:\n", V_X

while len(V_X) != 0:#len(V_X) != 0:

    update_V_X(v)

    w = growX()

    for i in range(0, len(V_X)):
        if V_X[i][1] == w:
            V_X = np.delete(V_X, i, axis=0)
            break

    v = w
    X.append(w)




print "A", A
print "X", X
print "V:\n", V_X

print "Shortest paths to nodes:"
print A[6],",",A[36],",",A[58],",",A[81],",",A[98],",",A[114],",",A[132],",",A[164],",",A[187],",",A[196]