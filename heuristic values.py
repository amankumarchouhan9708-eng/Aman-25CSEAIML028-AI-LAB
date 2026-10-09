def get_user_input():
    heuristic = {}
    num_nodes = int(input("enter total number of nodes (students) in the graph: "))
    print("\nenter the heuristic values for each node (student):")
    for i in range(num_nodes):
        node = input("node name: ").strip().upper()
        h_val =  float(input(f"heuristic value for {node}: "))
        heuristic[node] = h_val
        
    graph = {node: [] for node in heuristic}
    num_edges = int(input("\nenter the number of edges (connections) in the graph: "))
    print("enter the edges separated by space (e.g., A B):")
    for i in range(num_edges):
        u,v,w = input(f"edge {i + 1}: ").strip().split()
        u,v,= u.upper(), v.upper()
        weight = float(w)
        graph[u].append((v, weight))
        
    return graph, heuristic

def astar(graph, heuristic, start, goal):
    open_list = [(start,0)]
    came_from = {}
    g_cost = {start: 0}
    
    while open_list:
        current = min(open_list,key=lambda x: x[1]+heuristic[x[0]])
        open_list.remove(current)
        current_node = current[0]
        
        if current_node == goal:
            path = []
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path + g_cost[goal]
    for neighbor, weight in graph.get(current_node, []):
        new_cost = g_cost[current_node] + weight
        
        if neighbor not in g_cost or new_cost < g_cost[neighbor]:
            g_cost[neighbor] = new_cost
            came_from[neighbor] = current_node
            open_list.append((neighbor, new_cost))
    return None,float('inf')

            
        
        
        
    