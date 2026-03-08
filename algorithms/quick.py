from utils import draw_bars
import time

def partition(arr, low, high, delay):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        highlight = [j, high]  # Show pivot comparison
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        draw_bars(arr[:high+1], highlight, "Quick Sort", f"Partition {low}-{high}")
        time.sleep(delay)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_visual(arr, low=0, high=None, delay=0.1):
    if high is None: high = len(arr)-1
    if low < high:
        pi = partition(arr, low, high, delay)
        quick_visual(arr, low, pi-1, delay)
        quick_visual(arr, pi+1, high, delay)

def visualize(arr, delay=0.1):
    quick_visual(arr, delay=delay)
    draw_bars(arr, [], "Quick Sort ✅", "Complete!")
