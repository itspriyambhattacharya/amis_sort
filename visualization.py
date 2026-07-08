import sys
import time
import tracemalloc
import random
import copy
import matplotlib.pyplot as plt

# Import sorting algorithms from the existing sort.py file
from sort import bubbleSort, insertionSort, heapSort, quickSort, quickSort2, mergeSort, mergeSort2, hrpSort, sieveSort, amis


class RecursionTracker:
    def __init__(self):
        self.current_depth = 0
        self.max_depth = 0

    def trace_calls(self, frame, event, arg):
        if event == 'call':
            self.current_depth += 1
            if self.current_depth > self.max_depth:
                self.max_depth = self.current_depth
        elif event == 'return':
            self.current_depth -= 1
        return self.trace_calls


def generate_dataset(n):
    return [random.randint(-10000, 10000) for _ in range(n)]


def benchmark_algorithms(dataset_sizes):
    algorithms = {
        # "Bubble Sort": bubbleSort,
        # "Insertion Sort": insertionSort,
        "Quick Sort": quickSort,
        "Merge Sort": mergeSort,
        "Heap Sort": heapSort,
        "Sieve Sort": sieveSort,
        # "Quick Sort (3-way)": quickSort2,
        # "Merge Sort (Iterative)": mergeSort2,
        # "HRP Sort": hrpSort,
        "AMIS Sort": amis
    }

    results = {name: {'time': [], 'space': [], 'recursion': []}
               for name in algorithms}

    for size in dataset_sizes:
        print(f"Benchmarking dataset size: {size}")
        base_dataset = generate_dataset(size)

        for name, func in algorithms.items():
            dataset_copy = copy.deepcopy(base_dataset)
            n = len(dataset_copy)

            tracker = RecursionTracker()
            sys.settrace(tracker.trace_calls)

            tracemalloc.start()
            start_time = time.perf_counter()

            try:
                func(dataset_copy, 0, n - 1)
            except Exception as e:
                print(f"Error in {name} at size {size}: {e}")

            end_time = time.perf_counter()
            current_mem, peak_mem = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            sys.settrace(None)

            exec_time = end_time - start_time
            peak_memory_kb = peak_mem / 1024

            results[name]['time'].append(exec_time)
            results[name]['space'].append(peak_memory_kb)
            results[name]['recursion'].append(tracker.max_depth)

    return results


def plot_results(dataset_sizes, results):
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6), dpi=300)
    markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p']

    for (name, metrics), marker in zip(results.items(), markers):
        ax1.plot(dataset_sizes, metrics['time'],
                 marker=marker, label=name, linewidth=2)
        ax2.plot(dataset_sizes, metrics['space'],
                 marker=marker, label=name, linewidth=2)
        ax3.plot(dataset_sizes, metrics['recursion'],
                 marker=marker, label=name, linewidth=2)

    ax1.set_title('Time Complexity Analysis', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Number of Elements (n)', fontsize=12)
    ax1.set_ylabel('Execution Time (Seconds)', fontsize=12)
    ax1.set_yscale('log')
    ax1.legend(fontsize=9)

    ax2.set_title('Space Complexity (Peak Memory)',
                  fontsize=14, fontweight='bold')
    ax2.set_xlabel('Number of Elements (n)', fontsize=12)
    ax2.set_ylabel('Memory Allocated (KB)', fontsize=12)
    ax2.legend(fontsize=9)

    ax3.set_title('Recursion Stack Depth', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Number of Elements (n)', fontsize=12)
    ax3.set_ylabel('Maximum Call Stack Depth', fontsize=12)
    ax3.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig('sorting_analysis_publication.png',
                dpi=300, bbox_inches='tight')
    print("Graphs successfully generated and saved as 'sorting_analysis_publication.png'.")
    plt.show()


if __name__ == "__main__":
    sys.setrecursionlimit(500000)
    dataset_sizes = [10, 50, 100, 500, 1000, 1500, 2000,
                     2500, 5000, 7500, 10000, 15000, 20000, 50000, 100000]
    results = benchmark_algorithms(dataset_sizes)
    plot_results(dataset_sizes, results)
