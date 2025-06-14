# -*- coding: utf-8 -*-
"""2.5.Floyd warshall.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RBq2Mfa6JN0wW0zjllbmeDRLFNeBAxfn
"""

def floyd_warshall(dist):
    """
    dist: 2D list (n x n) with dist[i][j] = edge weight or float('inf') if no direct edge.
    Returns: 2D list of shortest-path distances.
    """
    n = len(dist)
    # Make a copy so we don’t overwrite the original
    d = [row[:] for row in dist]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If going through k is shorter, update
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d

# Example usage:
INF = float('inf')
dist_matrix = [
    [0,   3,   INF, 7],
    [8,   0,   2,   INF],
    [5,   INF, 0,   1],
    [2,   INF, INF, 0]
]

shortest = floyd_warshall(dist_matrix)
for row in shortest:
    print(row)