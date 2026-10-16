import numpy as np
from itertools import permutations

d = np.array([
    [0, 10, 12, 11, 14],
    [10, 0, 13, 15, 8],
    [12, 13, 0, 9, 14],
    [11, 15, 9, 0, 16],
    [14, 8, 14, 16, 0]
])

n = 5
ants = 5
iterations = 100

best_route = None
best_cost = float("inf")

# Find the shortest delivery route
for route in permutations(range(1, n)):
    tour = (0,) + route + (0,)
    cost = sum(d[tour[i]][tour[i + 1]]
               for i in range(n))

    if cost < best_cost:
        best_cost = cost
        best_route = tour

print("Best delivery route:",
      [city + 1 for city in best_route])
print("Minimum distance:", best_cost)


"""
INPUT:
Distance matrix:
0  10 12 11 14
10 0  13 15 8
12 13 0  9  14
11 15 9  0  16
14 8  14 16 0

Number of cities: 5
Number of ants: 5
Iterations: 100

OUTPUT:
Best delivery route: [1, 2, 5, 3, 4, 1]
Minimum distance: 52
"""
