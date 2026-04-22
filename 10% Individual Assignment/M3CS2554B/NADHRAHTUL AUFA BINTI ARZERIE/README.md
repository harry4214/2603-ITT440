# NADHRAHTUL AUFA BINTI ARZERIE
# Task Queue Simulator

# Introduction 
This project is a Command-Line Interface (CLI) application developed to simulate and analyze task execution behaviors in an Operating System. Developed using Python 3.13 on Visual Studio Code (VS Code), the program demonstrates the core differences between Sequential, Concurrent (Threading), and Parallel (Multiprocessing) processing. This terminal-based approach is designed for high-performance execution and detailed logging of system resource management.

# Objectives
1) Concurrency vs Parallelism
   - to demonstrate how the operating system handles multiple threads within a single process vs multiple proceese accross CPU cores.
2) System Resource Evaluation
   - to understand the trade-offs between execution speed and system overhead (CPU/RAM).

# Reason used Visual Studio Code 
- Integrated Terminal : I can run the Python script and view the output in the same window.
- Lightweight & Fast : even though it has many features, it is relatively fast and stable compared to other heavy IDE (Integrated Development Environment).
  
# Coding in Python 
```python
import threading
import multiprocessing
import time

def work_function(task_id, mode):
    speed = 0.003
    print(f"[{mode}] Worker START: Task #{task_id}")
    time.sleep(speed) 
    print(f"[{mode}] Task #{task_id} COMPLETED")

def run_sequential(num_tasks):
    print("\n--- Running Sequential Mode ---")
    start = time.time()
    for i in range(num_tasks):
        work_function(1 + i, "Sequential")
    print(f">> Total Sequential Time: {time.time() - start:.2f}s")

def run_threading(num_tasks):
    print("\n--- Running Threading Mode (Concurrent) ---")
    start = time.time()
    threads = []
    for i in range(num_tasks):
        t = threading.Thread(target=work_function, args=(1 + i, "Threading"))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    print(f">> Total Threading Time: {time.time() - start:.2f}s")

def run_multiprocessing(num_tasks):
    print("\n--- Running Multiprocessing Mode (Parallel) ---")
    start = time.time()
    processes = []
    for i in range(num_tasks):
        p = multiprocessing.Process(target=work_function, args=(1 + i, "Multiprocessing"))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    print(f">> Total Multiprocessing Time: {time.time() - start:.2f}s")

if __name__ == "__main__":
    tasks_to_run = 10000
    
    print(f"Starting Simulator for {tasks_to_run} tasks...")
    
    run_sequential(tasks_to_run)
    run_threading(tasks_to_run)
    run_multiprocessing(tasks_to_run)
    
    print("\nSimulation Finished!")
```

# Conclusion 
The simulation successfully illustrates the critical role of task scheduling in modern computing. 
- Sequential : processing is simple but inefficient for large workloads.
- Threading : provides better responsiveness for I/O bound tasks.
- Multiprocessing : offers the best performance for CPU intensive tasks by utilizing multiple cores.

# Demonstration of Task Queue Simulation
