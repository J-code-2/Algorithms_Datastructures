from utils import draw_bars
import time


def visualize(arr, delay=0.2):
    n = len(arr)
    for i in range(n):
        min_idx = i
        highlight = [i]  # Current position

        for j in range(i + 1, n):
            highlight = [i, j]  # Compare i vs j
            if arr[j] < arr[min_idx]:
                min_idx = j
            draw_bars(arr, highlight, "Selection Sort", f"Finding min for pos {i}")
            time.sleep(delay)

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_bars(arr, [i], "Selection Sort", f"Placed {arr[i]} at pos {i}")
    draw_bars(arr, [], "Selection Sort ✅", "Complete!")
