n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []


def dfs(graph, node, visited):
    visited.append(node)
    graph[node].sort()
    for link_node in graph[node]:
        if link_node not in visited:
            dfs(graph, link_node, visited)


dfs(graph, 1, visited)
print(len(visited) - 1)
