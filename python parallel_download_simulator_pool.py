import time
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import multiprocessing
import sys

# ---------------------------------------
# SAFE matplotlib import
# ---------------------------------------
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

# ---------------------------------------
# Progress Bar Function
# ---------------------------------------
def show_progress(completed, total, label=""):
    bar_length = 30
    progress = completed / total
    filled = int(bar_length * progress)
    bar = "#" * filled + "-" * (bar_length - filled)
    percent = int(progress * 100)

    sys.stdout.write(f"\r{label} [{bar}] {percent}%")
    sys.stdout.flush()

# ---------------------------------------
# Simulated Download Task
# ---------------------------------------
def download_file(file_id):
    size = random.randint(1, 5)

    time.sleep(size * 0.01)

    total = 0
    for i in range(10000):
        total += i

    return total

# ---------------------------------------
# 1. SEQUENTIAL
# ---------------------------------------
def sequential_download(n):
    start = time.time()

    for i in range(n):
        download_file(i)
        show_progress(i + 1, n, "Sequential")

    print()  # move to next line
    return time.time() - start

# ---------------------------------------
# 2. THREADPOOL
# ---------------------------------------
def threaded_download(n):
    start = time.time()
    completed = 0

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(download_file, i) for i in range(n)]

        for future in as_completed(futures):
            completed += 1
            show_progress(completed, n, "ThreadPool")

    print()
    return time.time() - start

# ---------------------------------------
# 3. PROCESSPOOL
# ---------------------------------------
def multiprocessing_download(n):
    start = time.time()
    completed = 0

    cores = multiprocessing.cpu_count()

    with ProcessPoolExecutor(max_workers=cores) as executor:
        futures = [executor.submit(download_file, i) for i in range(n)]

        for future in as_completed(futures):
            completed += 1
            show_progress(completed, n, "ProcessPool")

    print()
    return time.time() - start

# ---------------------------------------
# GRAPH FUNCTION
# ---------------------------------------
def plot_graph(seq, thread, process):
    methods = ['Sequential', 'ThreadPool', 'ProcessPool']
    times = [seq, thread, process]

    plt.figure()
    plt.bar(methods, times)

    plt.xlabel('Execution Method')
    plt.ylabel('Time (seconds)')
    plt.title('Performance Comparison')

    for i in range(len(times)):
        plt.text(i, times[i], f"{times[i]:.2f}", ha='center')

    plt.savefig("performance_graph.png")
    plt.show()

# ---------------------------------------
# MAIN
# ---------------------------------------
if __name__ == "__main__":

    try:
        NUM_FILES = int(input("Enter number of files (recommended: 5000 - 20000): "))
    except:
        print("Invalid input. Using default = 20000")
        NUM_FILES = 20000

    print("\n=== LARGE SCALE SIMULATION ===\n")

    print("Running Sequential...")
    seq_time = sequential_download(NUM_FILES)
    print(f"Sequential Time: {seq_time:.2f}s\n")

    print("Running ThreadPool...")
    thread_time = threaded_download(NUM_FILES)
    print(f"ThreadPool Time: {thread_time:.2f}s\n")

    print("Running ProcessPool...")
    process_time = multiprocessing_download(NUM_FILES)
    print(f"ProcessPool Time: {process_time:.2f}s\n")

    print("CPU Cores Used:", multiprocessing.cpu_count())

    speedup = seq_time / process_time
    print(f"\nSpeedup: {speedup:.2f}x faster")

    if HAS_MATPLOTLIB:
        plot_graph(seq_time, thread_time, process_time)
    else:
        print("\n[INFO] Matplotlib not installed. Skipping graph.")