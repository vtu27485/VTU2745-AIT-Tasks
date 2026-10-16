from collections import deque

# /* BFS function */
def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# /* Input */
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for i in range(n)]

print("Enter edges:")
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# /* Find connected components */
visited = [False] * n

# /* Output */
print("Connected Components:")
for i in range(n):
    if not visited[i]:
        bfs(i, graph, visited)
        print()
"""
Enter number of vertices: 7
Enter number of edges: 5
Enter edges:
0 1
1 2
3 4
4 5
5 3
Connected Components:
0 1 2
3 4 5
6
"""
