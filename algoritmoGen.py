coords = load_tsp("att48.tsp")
distance = create_distance_matrix(coords)
num_cities = len(distance)
import math

def load_tsp(path):
    coords = []
    with open(path, "r") as f:
        read = False
        for line in f:
            line = line.strip()
            if line == "NODE_COORD_SECTION":
                read = True
                continue
            if line == "EOF":
                break
            if read:
                parts = line.split()
                if len(parts) == 3:
                    _, x, y = parts
                    coords.append((float(x), float(y)))
    return coords

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def create_distance_matrix(coords):
    n = len(coords)
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = dist(coords[i], coords[j])
    return matrix
