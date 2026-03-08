from utils import draw_bars
import time

def visualize(arr, delay=0.2):
    """Bubble sort with live visualization"""
    n = len(arr)
    for i in range(n):
        highlight = []
        swaps = 0
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                highlight = [j, j+1]
                swaps += 1
            draw_bars(arr, highlight, "Bubble Sort", f"Pass {i+1}, Swap {swaps}")
            time.sleep(delay)
    draw_bars(arr, [], "Bubble Sort ✅", "Complete!")
