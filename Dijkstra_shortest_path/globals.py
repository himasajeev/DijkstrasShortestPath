print "Reading Data..."

result_file = r'data.txt'
with open(result_file) as file:
    adjacency = [[(digit.split(",")) for digit in line.split()] for line in file]

for i in range(0, len(adjacency)):
    for j in range(0, len(adjacency[i])):
        for k in range(0, len(adjacency[i][j])):
            adjacency[i][j][k] = int(adjacency[i][j][k])

A = [0 for i in range(len(adjacency))]

X = []

V_X = [[1000000, j] for j in range(1, len(adjacency)+1)]