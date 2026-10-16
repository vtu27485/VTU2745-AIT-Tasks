graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

colors = 3
color = [-1] * 4


def safe(v, c):
    for u in graph[v]:
        if color[u] == c:
            return False
    return True


def solve(v):
    if v == 4:
        return True

    for c in range(colors):
        if safe(v, c):
            color[v] = c

            if solve(v + 1):
                return True

            color[v] = -1

    return False


if solve(0):
    print("Coloring:", color)
else:
    print("No valid coloring")


"""
INPUT:
Number of vertices: 4
Number of colors: 3

Edges:
V1 - V2
V1 - V3
V2 - V3
V2 - V4
V3 - V4

OUTPUT:
Coloring: [0, 1, 2, 0]
"""
