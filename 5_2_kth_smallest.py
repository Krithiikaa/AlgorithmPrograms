# -*- coding: utf-8 -*-
"""5.2.Kth smallest.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P_iw3u9Lb4WrsMgwUkS3zMrX0of8MgBd
"""

import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = randomized_partition(arr, low, high)
    rank = pivot_index - low + 1

    if k == rank:
        return arr[pivot_index]
    elif k < rank:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k - rank)

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
result = randomized_select(arr.copy(), 0, len(arr) - 1, k)
print(f"The {k}rd smallest number is: {result}")