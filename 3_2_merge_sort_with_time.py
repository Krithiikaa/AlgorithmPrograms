# -*- coding: utf-8 -*-
"""3.2.Merge Sort with Time.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1andyLgkZDqg7l8PM1DGp0z9zBlf4QbpM
"""

import time              # To measure time taken by sorting algorithms
import random            # To generate random numbers
import matplotlib.pyplot as plt   # To plot the graph
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2             # Find the middle point
        L = arr[:mid]                   # Divide into left half
        R = arr[mid:]                   # Divide into right half

        merge_sort(L)                   # Sort the left half
        merge_sort(R)                   # Sort the right half

        # Merge the two halves
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):               # Copy remaining elements
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def quick_sort(arr):
    if len(arr) <= 1:
        return arr                      # Base case
    else:
        pivot = arr[0]                  # Choose the first element as pivot
        less = [i for i in arr[1:] if i <= pivot]   # Smaller than pivot
        greater = [i for i in arr[1:] if i > pivot] # Greater than pivot
        return quick_sort(less) + [pivot] + quick_sort(greater)
sizes = [100, 500, 1000, 2000, 5000, 10000]  # Different input sizes
merge_times = []   # Store merge sort times
quick_times = []   # Store quick sort times

for size in sizes:
    arr = random.sample(range(1, size * 10), size)  # Generate random array

    # Test Merge Sort
    arr1 = arr.copy()
    start = time.time()
    merge_sort(arr1)
    end = time.time()
    merge_times.append(end - start)

    # Test Quick Sort
    arr2 = arr.copy()
    start = time.time()
    quick_sort(arr2)
    end = time.time()
    quick_times.append(end - start)
plt.plot(sizes, merge_times, label="Merge Sort", marker='o')
plt.plot(sizes, quick_times, label="Quick Sort", marker='x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Time vs Input Size for Merge and Quick Sort")
plt.legend()
plt.grid(True)
plt.show()