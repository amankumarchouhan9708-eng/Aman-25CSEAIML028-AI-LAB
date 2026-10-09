def bfs(graph, start):
    visited =[]
    queue = []

    queue.append(start)
    visited.append(start)
    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited