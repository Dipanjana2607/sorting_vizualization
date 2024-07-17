import matplotlib.pyplot as plt
import numpy as np
import random

# Sorting algorithms
def merge_sort(arr, visualizer):
    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        
        i, j, k = 0, 0, left
        
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            visualizer.update(arr)
        
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            visualizer.update(arr)
        
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            visualizer.update(arr)
    
    def merge_sort_recursive(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_recursive(arr, left, mid)
            merge_sort_recursive(arr, mid + 1, right)
            merge(arr, left, mid, right)
    
    merge_sort_recursive(arr, 0, len(arr) - 1)

def selection_sort(arr, visualizer):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        visualizer.update(arr)

def insertion_sort(arr, visualizer):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            visualizer.update(arr)
        arr[j + 1] = key
        visualizer.update(arr)

def heap_sort(arr, visualizer):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            visualizer.update(arr)
            heapify(arr, n, largest)
    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        visualizer.update(arr)
        heapify(arr, i, 0)

def bubble_sort(arr, visualizer):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                visualizer.update(arr)

# Visualizer
class Visualizer:
    def __init__(self, arr, algo_name):
        self.arr = arr
        self.algo_name = algo_name
        self.fig, self.ax = plt.subplots()
        self.bars = self.ax.bar(range(len(arr)), arr, align='center')
        self.ax.set_ylim(0, max(arr) * 1.1)
        self.ax.set_title(f"{self.algo_name} Sort")
        plt.ion()
        plt.show()

    def update(self, arr):
        for bar, val in zip(self.bars, arr):
            bar.set_height(val)
        plt.pause(0.001)

def main():
    array_size = 100  # Change this to visualize larger arrays
    arr = np.random.randint(1, 100, array_size)
    algorithms = {
        "merge": merge_sort,
        "selection": selection_sort,
        "insertion": insertion_sort,
        "heap": heap_sort,
        "bubble": bubble_sort
    }

    print("Available algorithms:")
    for algo in algorithms.keys():
        print(f"- {algo}")

    choice = input("Enter the algorithm to visualize (or 'all' for all algorithms): ").strip().lower()

    if choice == "all":
        for algo_name, algo_func in algorithms.items():
            print(f"Visualizing {algo_name} sort...")
            arr_copy = arr.copy()
            visualizer = Visualizer(arr_copy, algo_name)
            algo_func(arr_copy, visualizer)
            plt.show(block=True)
    elif choice in algorithms:
        print(f"Visualizing {choice} sort...")
        arr_copy = arr.copy()
        visualizer = Visualizer(arr_copy, choice)
        algorithms[choice](arr_copy, visualizer)
        plt.show(block=True)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()