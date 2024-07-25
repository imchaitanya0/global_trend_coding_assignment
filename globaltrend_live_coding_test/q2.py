''''
Write a function to find the shortest path from a source vertex to all other vertices in a graph using Dijkstra's algorithm.
Sample Test Case
Input: graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}, source = 0 Output: {0: 0, 1: 3, 2: 1, 3: 4}
'''
import heapq

def dijkstra(graph, source):
    # Initialize distances and visited set
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    visited = set()

    # Priority queue to store vertices and their distances
    pq = [(0, source)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # If we've already found a shorter path, continue
        if current_vertex in visited:
            continue

        # Mark the current vertex as visited
        visited.add(current_vertex)

        # Check all neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If we've found a shorter path, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}
source = 0
result = dijkstra(graph, source)
print(result)  # Output: {0: 0, 1: 3, 2: 1, 3: 4}


