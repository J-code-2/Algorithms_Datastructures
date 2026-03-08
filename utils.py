import os, time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_bars(arr, highlight=[], title="Sorting...", info=""):
    """Vertical bars for ALL algorithms"""
    max_val = max(arr)
    width = 55
    clear()
    print(f"{title} | Size: {len(arr)} | {info}")
    print()
    for i, val in enumerate(arr):
        bar_len = int(width * val / max_val)
        bar = '█' * bar_len

        color = '\033[92m' if i in highlight else ''
        print(f"{color}{bar.ljust(width)}{' ' * 4}{val:3d}\033[0m")
    print('─' * (width + 8))
