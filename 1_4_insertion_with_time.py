# -*- coding: utf-8 -*-
"""1.4.Insertion With Time.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1851asISfqPiNe40r_M7gZNXMJmzLqJ2I
"""

import time
import random
import matplotlib.pyplot as plt
import heapq

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

sizes = [100, 500, 1000, 2000]
insert_times = []
heap_times = []

for size in sizes:
    arr = random.sample(range(size*10), size)

    # Insertion Sort
    a = arr.copy()
    start = time.time()
    insertion_sort(a)
    end = time.time()
    insert_times.append(end - start)

    # Heap Sort
    b = arr.copy()
    start = time.time()
    heap_sort(b)
    end = time.time()
    heap_times.append(end - start)

plt.plot(sizes, insert_times, label="Insertion Sort", marker='o')
plt.plot(sizes, heap_times, label="Heap Sort", marker='x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (s)")
plt.title("Insertion vs Heap Sort Time")
plt.legend()
plt.grid(True)
plt.show()