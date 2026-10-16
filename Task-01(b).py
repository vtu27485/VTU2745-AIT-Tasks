# /* DFS function */
def dfs(vertex, graph, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            dfs(neighbour, graph, visited)


# /* Input */
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# /* Create adjacency list */
graph = {i: [] for i in range(n)}

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
        dfs(i, graph, visited)
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
