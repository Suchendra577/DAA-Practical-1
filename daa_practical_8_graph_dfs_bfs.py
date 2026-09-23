"""DAA Practical 8: Implementation of Graph and Searching (DFS and BFS).

Example:
    Vertices = 6 (labelled 0 to 5)
    Edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5)]
    Starting vertex = 0
    BFS traversal = [0, 1, 2, 3, 4, 5]
    DFS traversal = [0, 1, 3, 5, 2, 4]
"""

import time
from collections import deque


def build_graph(vertex_count, edges):
    """Return an adjacency list representation of an undirected graph."""
    graph = {vertex: [] for vertex in range(vertex_count)}
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    return graph


def breadth_first_search(graph, start_vertex):
    """Return the BFS traversal order starting from start_vertex."""
    visited = {start_vertex}
    traversal_order = []
    queue = deque([start_vertex])

    while queue:
        current_vertex = queue.popleft()
        traversal_order.append(current_vertex)

        for neighbour in sorted(graph[current_vertex]):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return traversal_order


def depth_first_search(graph, start_vertex):
    """Return the DFS traversal order starting from start_vertex."""
    visited = set()
    traversal_order = []

    def visit(vertex):
        visited.add(vertex)
        traversal_order.append(vertex)
        for neighbour in sorted(graph[vertex]):
            if neighbour not in visited:
                visit(neighbour)

    visit(start_vertex)
    return traversal_order


def main():
    print("=" * 50)
    print("DAA Practical 8: Implementation of Graph and Searching (DFS and BFS)")
    print("=" * 50)

    try:
        vertex_count = int(input("Enter the number of vertices: "))
        edge_count = int(input("Enter the number of edges: "))

        if vertex_count <= 0:
            print("Invalid input! The number of vertices must be positive.")
            return
        if edge_count < 0:
            print("Invalid input! The number of edges cannot be negative.")
            return

        edges = []
        print("Enter each edge as two space-separated vertices (e.g. 0 1):")
        for edge_number in range(1, edge_count + 1):
            edge_input = input(f"Edge {edge_number}: ")
            start, end = map(int, edge_input.split())

            if not (0 <= start < vertex_count) or not (0 <= end < vertex_count):
                print(f"Invalid input! Vertices must be between 0 and {vertex_count - 1}.")
                return
            edges.append((start, end))

        start_vertex = int(input("Enter the starting vertex: "))
        if not (0 <= start_vertex < vertex_count):
            print(f"Invalid input! The starting vertex must be between 0 and {vertex_count - 1}.")
            return

        graph = build_graph(vertex_count, edges)

        start_time = time.perf_counter()
        bfs_order = breadth_first_search(graph, start_vertex)
        bfs_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        dfs_order = depth_first_search(graph, start_vertex)
        dfs_time = time.perf_counter() - start_time

        print(f"\nVertices: {vertex_count}")
        print(f"Edges: {edges}")
        print(f"Starting vertex: {start_vertex}")
        print(f"\nBFS traversal order: {bfs_order}")
        print(f"BFS execution time: {bfs_time:.9f} seconds")
        print(f"\nDFS traversal order: {dfs_order}")
        print(f"DFS execution time: {dfs_time:.9f} seconds")

        if len(bfs_order) < vertex_count:
            unreachable = sorted(set(range(vertex_count)) - set(bfs_order))
            print(f"\nNote: Vertices {unreachable} are unreachable from vertex {start_vertex}.")

        print("-" * 50)
        print("Time complexity: O(V + E)")
        print("Space complexity: O(V)")
        print("V = number of vertices, E = number of edges")
    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()
