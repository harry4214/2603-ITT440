# NUR BAYAN NAJIHAH BINTI NAZARUDDIN

# ˚˖𓍢ִ໋🌷͙֒  Parallel Random Number Sorting ˚˖𓍢ִ໋🌷͙֒

**STUDENT NAME:** NUR BAYAN NAJIHAH BINTI NAZARUDDIN

**STUDENT ID:** 2024299378

**CLASS:** M3CS2554B

**LECTURER NAME:** ENCIK SHAHADAN BIN SAAD

**VIDEO LINK:** [Watch the Demonstration ೀ⋆｡˚](https://youtu.be/ffCQGnaGHpY)

---

## 1.0 Introduction 💻✨
This repository presents a technical performance audit of Python’s core concurrency and parallelism modules: `threading` and `multiprocessing`. The study is centered on a comparative analysis of execution times when subjected to a high-density, CPU-bound task. By leveraging a recursive **Merge Sort** implementation, this project benchmarks the system's ability to handle an array of **600,000 randomized integers**—a scale large enough to expose the overhead and efficiency of different processing paradigms.

The project evaluates three specific execution workflows:
*   **Sequential Baseline:** Standard linear execution on a single core. 🚶
*   **Threaded Concurrency:** Context-switching between threads within a single process. 👯
*   **Process-level Parallelism:** Simultaneous execution across multiple independent OS-level processes. 🚀

Through this academic exercise, we demonstrate how Visual Studio Code's development environment can be used to profile and diagnose the impacts of the **Global Interpreter Lock (GIL)** on modern hardware, ultimately determining the most scalable approach for intensive data processing. 🌟

---

## 2.0 Problem Statement 🚦
In standard Python execution, performance is frequently constrained by the **Global Interpreter Lock (GIL)**. The GIL is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once. 

While the GIL ensures thread safety, it creates a bottleneck for CPU-bound tasks like mathematical sorting. This project investigates whether process-based parallelism can successfully bypass these concurrency limitations by leveraging multi-core CPU architectures to enhance throughput and reduce total execution time. 🏎️💨

---

## 3.0 System Requirements 🖥️
*   **Operating System:** Windows 10/11, macOS, or Linux
*   **Editor:** [Visual Studio Code (VS Code)](https://code.visualstudio.com/) 💙
*   **Extensions:** Python extension by Microsoft 🐍
*   **CPU:** A multi-core processor
*   **Python:** Version 3.7+ 

---

## 4.0 Installation & Setup (VS Code) 🛠️
1.  **Get Python:** Ensure Python is installed on your system. 
2.  **Open VS Code:** Open your project folder. 📂
3.  **Extensions:** Go to the Extensions view (`Ctrl+Shift+X`) and install the **Python** extension. 
4.  **The File:** Create a new file called `parallel_sort.py`. 📄
5.  **Interpreter:** Check the bottom right of VS Code to ensure your Python environment is active! 

---

## 5.0 How to Run ⌨️
1.  Open `parallel_sort.py` in your VS Code editor.
2.  Open the **Integrated Terminal** (``Ctrl + ` ``).
3.  Run the script:
    ```bash
    python parallel_sort.py
    ```
4.  When prompted, type number 600,000,then watch the magic happen! ✨

---

## 6.0 Sample Input/Output 🎲

**Input:**
<img width="465" height="26" alt="image" src="https://github.com/user-attachments/assets/e26fb4c2-4413-4e2e-a471-487954a0ad4d" />

**Output**
<img width="502" height="355" alt="image" src="https://github.com/user-attachments/assets/d50f4323-d77c-44f8-87c4-14d09a16d5b7" />

---

## 7.0 Source Code 🐍
import random
import time
import threading
import multiprocessing
from multiprocessing import Pool

# --- 1. THE COMPUTATIONAL WORK (Merge Sort) ---
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

# --- 2. SEQUENTIAL APPROACH ---
def run_sequential(data):
    return merge_sort(data)

# --- 3. THREADING APPROACH ---
def run_threading(data):
    mid = len(data) // 2
    left_part = data[:mid]
    right_part = data[mid:]
    results = [None, None]

    def wrapper(chunk, index):
        results[index] = merge_sort(chunk)

    t1 = threading.Thread(target=wrapper, args=(left_part, 0))
    t2 = threading.Thread(target=wrapper, args=(right_part, 1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return merge(results[0], results[1])

# --- 4. MULTIPROCESSING APPROACH ---
def run_multiprocessing(data):
    num_cores = multiprocessing.cpu_count()
    size = max(1, len(data) // num_cores)
    chunks = [data[i:i + size] for i in range(0, len(data), size)]
    
    with Pool(processes=num_cores) as pool:
        sorted_chunks = pool.map(merge_sort, chunks)
    
    final_result = sorted_chunks[0]
    for i in range(1, len(sorted_chunks)):
        final_result = merge(final_result, sorted_chunks[i])
    return final_result

if __name__ == "__main__":
    print("="*60)
    print("  PARALLEL RANDOM NUMBER SORTING")
    print("="*60)
    try:
        user_input = input("Enter number of elements to sort: ")
        n = int(user_input)
        
        print(f"\n[+] Generating {n} random integers...")
        original_data = [random.randint(0, 1000000) for _ in range(n)]

        # --- Test Sequential ---
        print("[!] Processing Sequential Sort...")
        start = time.perf_counter()
        res_seq = run_sequential(original_data.copy())
        time_seq = time.perf_counter() - start
        print(f"    Finished in {time_seq:.4f}s")

        # --- Test Threading ---
        print("[!] Processing Threading Sort...")
        start = time.perf_counter()
        res_th = run_threading(original_data.copy())
        time_th = time.perf_counter() - start
        print(f"    Finished in {time_th:.4f}s")

        # --- Test Multiprocessing ---
        print("[!] Processing Multiprocessing Sort...")
        start = time.perf_counter()
        res_mp = run_multiprocessing(original_data.copy())
        time_mp = time.perf_counter() - start
        print(f"    Finished in {time_mp:.4f}s")

        # --- Summary Table ---
        all_results = [
            ("Sequential", time_seq), 
            ("Threading", time_th), 
            ("Multiprocessing", time_mp)
        ]
        all_results.sort(key=lambda x: x[1])

        print("\n" + " PERFORMANCE SUMMARY ".center(50, "-"))
        for i, (name, t) in enumerate(all_results, 1):
            status = " (FASTEST)" if i == 1 else ""
            print(f"{i}. {name:<20} | {t:.4f}s{status}")
        
    except Exception as e:
        print(f"Oopsie! An error occurred: {e}")
 
---

## 8.0 Conclusion 🎀
The empirical data collected from the 600,000 element benchmark confirms that Multiprocessing is the superior paradigm for CPU-bound computational tasks in Python. While the Sequential and Multithreaded approaches yielded comparable execution times—due to GIL-imposed concurrency limitations—Multiprocessing achieved true parallelism by utilizing multiple OS-level processes. This study concludes that for high-performance data processing, developers should prioritize process-based parallelism to optimize throughput and resource utilization. 🌸🙌

---

## 9.0 Video Demonstration 📽️
(https://youtu.be/ffCQGnaGHpY)
