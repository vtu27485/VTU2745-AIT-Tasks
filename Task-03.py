import heapq

def a_star(graph, h, start, goal):
    queue = [(h[start], 0, start, [start])]

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        for next_node, distance in graph[node]:
            new_cost = cost + distance
            new_f = new_cost + h[next_node]

            heapq.heappush(
                queue,
                (new_f, new_cost, next_node, path + [next_node])
            )

    return None, float("inf")


graph = {
    "Accident": [("A", 2), ("B", 4)],
    "A": [("C", 3)],
    "B": [("C", 1)],
    "C": [("Hospital", 2)],
    "Hospital": []
}

h = {
    "Accident": 5,
    "A": 4,
    "B": 3,
    "C": 2,
    "Hospital": 0
}

start = "Accident"
goal = "Hospital"

path, cost = a_star(graph, h, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")


"""
INPUT:
Accident
Hospital

Roads:
Accident -> A = 2
Accident -> B = 4
A -> C = 3
B -> C = 1
C -> Hospital = 2

OUTPUT:
Shortest Path: Accident -> A -> C -> Hospital
Total Cost: 7
"""
