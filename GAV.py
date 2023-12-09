import heapq

def dijkstra(graph, start):
    """
    Dijkstra's Algorithm to find the shortest path in a graph

    :param graph: A dictionary where keys are nodes and values are lists of tuples (neighbor, weight)
    :param start: The starting node
    :return: Shortest path from start to all other nodes in the graph
    """
    # Initialize distances as infinity and set distance to start node as 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Use a priority queue to store nodes to visit
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If the distance to the current node is already optimal, skip
        if current_distance > distances[current_node]:
            continue

        # Visit each neighbor of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Find shortest paths from node 'A'
shortest_paths = dijkstra(graph, 'A')
print("Shortest paths from A:", shortest_paths)
