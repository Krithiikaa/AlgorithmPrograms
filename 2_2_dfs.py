# -*- coding: utf-8 -*-
"""2.2.DFS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lej7jDexY081i8y3feim7unS5LcVqZcz
"""

def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path

    return None  # If no path is found
# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Start and goal nodes
start_node = 'A'
goal_node = 'F'

# Run DFS
result = dfs(graph, start_node, goal_node)

# Print the result
if result:
    print("Path found:", " -> ".join(result))
else:
    print("No path found.")