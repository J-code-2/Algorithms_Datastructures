import random
import time
from algorithms.bubble import visualize as bubble_viz
from algorithms.quick import visualize as quick_viz
from algorithms.selection import visualize as selection_viz

ALGORITHMS = {
    '1': ('Bubble Sort O(n²)', bubble_viz),
    '2': ('Quick Sort O(n log n)', quick_viz),
    '3': ('Selection Sort O(n²)', selection_viz)
}

SPEEDS = {
    '1': 0.1,  # Fast
    '2': 0.2,  # Normal
    '3': 0.4  # Slow (watch every step)
}


def main():
    while True:
        print("\n" + "=" * 50)
        print(" TERMINAL SORTING VISUALIZER")
        print("=" * 50)
        for key, (name, _) in ALGORITHMS.items():
            print(f"{key}. {name}")
        print("q. Quit")

        algo_choice = input("\nAlgorithm (1-3/q): ").strip()

        if algo_choice.lower() == 'q':
            print(" Goodbye!")
            break

        if algo_choice in ALGORITHMS:
            name, viz_func = ALGORITHMS[algo_choice]

            size = int(input("Array size (10-30): ") or "20")

            print("\nSpeed:")
            print("1. Fast (0.1s)")
            print("2. Normal (0.2s)")
            print("3. Slow (0.4s)")
            speed_choice = input("Speed (1-3): ").strip()

            if speed_choice in SPEEDS:
                delay = SPEEDS[speed_choice]
                print(f"\n Running {name} at speed {speed_choice}...")
                time.sleep(0.5)

                arr = [random.randint(1, 99) for _ in range(size)]
                viz_func(arr, delay)
                input("\nPress Enter for menu...")
            else:
                print(" Choose 1, 2, or 3")
        else:
            print(" Choose 1-3 or q")


if __name__ == "__main__":
    main()
