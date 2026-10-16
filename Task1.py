def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (5, 5)

path = [start]
current = start
visited = {start}

while current != goal:
    x, y = current
    neighbours = []

    # Check up, down, left and right
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if (0 <= nx < 6 and 0 <= ny < 6
                and grid[nx][ny] == 0
                and (nx, ny) not in visited):
            neighbours.append((nx, ny))

    if not neighbours:
        print("Trapped!")
        break

    # Choose the neighbour closest to the goal
    best = min(neighbours, key=lambda p: distance(p, goal))

    # Stop if no neighbour improves the distance
    if distance(best, goal) >= distance(current, goal):
        print("Trapped!")
        break

    current = best
    path.append(current)
    visited.add(current)

print("Path:", path)

if current == goal:
    print("Goal reached")
else:
    print("Goal not reached")
"""
INPUT:
Enter start (row col): 0 0
Enter goal (row col): 5 5
OUTPUT
Grid (0 = Free, 1 = Obstacle):
[0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 0, 0]
[0, 0, 0, 1, 0, 0]
[0, 1, 0, 0, 0, 0]
[0, 1, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0]
Enter start (row col): 0 0
Enter goal (row col): 5 5
Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5)]
Goal reached
"""
