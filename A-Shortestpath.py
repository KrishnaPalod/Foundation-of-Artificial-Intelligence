import heapq

def heuristic_cost_estimate(graph, start, goal):
    # A* heuristic function - in this case, simply return 0 for all vertices
    return 0

def a_star(graph, start, goal):
    # Initialize distances to all vertices as infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Distance from start vertex to itself is 0
    # Initialize priority queue with the start vertex and its distance (f-score)
    pq = [(0 + heuristic_cost_estimate(graph, start, goal), start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # If the current distance is greater than the known distance to the vertex, skip
        if current_distance > distances[current_vertex]:
            continue

        # If the current vertex is the goal, return the distances
        if current_vertex == goal:
            return distances

        # Iterate through neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            # If the new distance is shorter than the known distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Calculate f-score (distance + heuristic) and add to priority queue
                heapq.heappush(pq, (distance + heuristic_cost_estimate(graph, neighbor, goal), neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_vertex = 'A'
goal_vertex = 'D'
shortest_distances = a_star(graph, start_vertex, goal_vertex)
print("Shortest distances from", start_vertex, "to all vertices:", shortest_distances)

# Assuming you want to find the shortest path using A* algorithm, you should call a_star function instead
# path = a_star(start_node, goal_node, grid)
# Replace start_node, goal_node, and grid with your actual inputs
# if path:
#     print("Path found:", path)
# else:
#     print("No path found.")
