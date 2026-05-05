# MUHAMMAD AMIRUL HAIQAL BIN MOHD SUBRI
# 1.0 Project Title: GAME SCORE ANALYZER

**Course:** ITT440 - Network Programming  
**Group:** M3CS2554B  
**Name:** MUHAMMAD AMIRUL HAIQAL BIN MOHD SUBRI  
**Student ID:** 2024215692  
**Lecturer:** Sir Shahadan Bin Saad  
**Video Link:** https://youtu.be/M1ozVjQgShw

---

## 1.1 Project Overview and Description
The **Game Score Analyzer** is a performance simulation and benchmarking tool designed to evaluate how different execution models handle CPU-heavy network and server workloads. In large-scale online games, servers are tasked with constantly processing millions of data points—such as calculating player ranks from raw scores. When handled inefficiently, these calculations create severe bottlenecks that result in network latency and server lag.

This project simulates that environment by generating massive datasets (ranging from 1,000 to 1,000,000 player scores) and pushing them through a heavy mathematical ranking algorithm. To find the optimal solution for backend server architecture, the system processes this data using three distinct methods: Sequential, Multithreading, and Multiprocessing.

## 2.0 Problem Statement

Online game servers need to process thousands of player scores to calculate ranks. If the server processes this data sequentially (one player at a time), it takes too long. This creates a bottleneck, causing server lag and delays for the players.

To speed things up, developers often try **Multithreading**. However, Python has a built-in limitation called the Global Interpreter Lock (GIL). Because of the GIL, Python threads cannot perform heavy math at the exact same time. They just take turns using a single CPU core, meaning the server doesn't actually get any faster.

Therefore, the problem is figuring out the best way to truly speed up the server for heavy tasks. This project will compare Sequential execution, Multithreading, and **Multiprocessing** to prove that only Multiprocessing can use multiple CPU cores at once to solve this lag issue.

---

## 3.0 Development Environment

To build, test, and run this project, the following hardware and software tools were utilized:

### 3.1 Hardware Requirements
* **Processor (CPU):** A multi-core processor is required to properly test and observe the speed improvements of the Multiprocessing method. *(The script automatically detects and uses the available CPU cores).*
* **Memory (RAM):** 4GB or higher (Standard modern computer).

### 3.2 Software & Tools
* **Operating System:** Windows 10/11, macOS, or Linux.
* **Programming Language:** Python 3.x.
* **IDE / Code Editor:** Visual Studio Code (VS Code), PyCharm, or any standard text editor.

### 3.3 Python Libraries Used
**Built-in Libraries:**
* `random`: Used to generate the simulated datasets of up to 1,000,000 player scores.
* `time`: Used as a stopwatch to measure the exact execution time of each method.
* `threading`: Used to implement the Multithreading approach.
* `multiprocessing`: Used to implement the true parallel processing approach.

**External Libraries:**
* `matplotlib`: Used to generate the visual dashboard and bar charts (Rank Distribution and Execution Time comparison).

---

## 4.0 Methodology

The project was developed in Python using a step-by-step process to generate data, simulate a heavy server workload, and test different execution methods. The methodology is broken down into four main phases:

### 4.1 Data Generation
The simulation begins by creating a mock dataset for the game server. The script uses Python's `random` library to generate varying sizes of random integers (ranging from 0 to 1,000) to simulate different server loads. Specifically, datasets of **1,000**, **100,000**, and **1,000,000** player scores are generated to observe how the execution methods scale under increasingly heavy traffic.

### 4.2 Simulating the CPU Workload (Ranking Algorithm)
To simulate a heavy server task, an `assign_rank()` function was created.
* First, it runs a mathematical loop 200 times for every single score. This artificially stresses the CPU, simulating complex game logic or database calculations.
* Second, it checks the score and assigns the player to a ranking tier (Iron, Bronze, Silver, Gold, Platinum, or Diamond) based on their points.

### 4.3 Execution and Testing Methods
The generated player scores are then passed through the ranking algorithm using three different approaches:
* **Sequential:** The baseline method. A standard `for` loop processes the players one by one, waiting for each to finish before starting the next.
* **Multithreading:** The data is divided into chunks and processed by 4 separate threads simultaneously. *(This tests how Python's Global Interpreter Lock impacts CPU-heavy tasks).*
* **Multiprocessing:** The data is divided into chunks and assigned to the computer's physical CPU cores using `multiprocessing.Pool`. This allows multiple cores to process the mathematical workload at the exact same time.

### 4.4 Benchmarking and Visualization
To analyze the results, the system uses the `time` module to record the start and end times for each of the three methods. Finally, the program outputs the results in two ways:
* **Console Output:** A clean ASCII table displaying the total player rank distribution and the execution times for each method.
* **Graphical Dashboard:** The `matplotlib` library is used to automatically generate and save a visual dashboard (`performance_graph.png`), making it easy to compare the execution speeds visually.

---

## 5.0 Results and Discussion

### 5.1 Terminal Output For 1000 Player
<div align="center">
  
<img width="395" height="431" alt="image" src="https://github.com/user-attachments/assets/b638747c-e458-465d-8218-77581d9c6739" />

**Figure 1.0:** Console output of the final performance report.
</div>

### 5.2 Automated Graph Generation For 1000 Player
<div align="center">
<img width="802" height="592" alt="image" src="https://github.com/user-attachments/assets/9e0e6ae7-8a55-4f61-aa51-2146305e081c" />

**Figure 2.0:** Automated Graph Generation showing execution times.
</div>

### 5.3 Terminal Output For 100,000 Player

<div align="center">

<img width="391" height="442" alt="image" src="https://github.com/user-attachments/assets/74dbd083-66de-45f4-968e-c10ce1961692" />

**Figure 3.0:** Console output of the final performance report.
</div>

### 5.4 Automated Graph Generation For 100,000 Player
<div align="center">

<img width="802" height="601" alt="image" src="https://github.com/user-attachments/assets/eb85915d-4b2f-44fa-97d2-a76555ba042e" />

**Figure 4.0:** Automated Graph Generation showing execution times.
</div>

### 5.5 Terminal Output For 1,000,000 Player

<div align="center">

<img width="394" height="459" alt="image" src="https://github.com/user-attachments/assets/d5e9aaa8-ae09-415d-bffe-fbab530c790f" />

**Figure 5.0:** Console output of the final performance report.
</div>

### 5.6 Automated Graph Generation For 1,000,000 Player
<div align="center">

<img width="799" height="600" alt="image" src="https://github.com/user-attachments/assets/55196d1b-f1f0-44b4-a189-967051cd2b73" />

**Figure 6.0:** Automated Graph Generation showing execution times.
</div>

### 5.7 Execution Time Analysis Across Different Dataset Sizes

To fully understand the efficiency of each execution method, the system was tested across three different dataset sizes: 1,000, 100,000, and 1,000,000 players. The results demonstrate the impact of "overhead"—the time it takes the Operating System to set up and manage parallel tasks.

**1. Small Dataset (1,000 Players): The Overhead Trap**
For a small number of players, **Sequential** execution is usually the fastest. This is because a single CPU core can process 1,000 calculations almost instantly. **Multiprocessing** performs the slowest here. Setting up separate processes, dividing the data, and sending it to different CPU cores requires time (overhead). For 1,000 players, the server spends more time organizing the work than actually doing the math.

**2. Medium Dataset (100,000 Players): The Turning Point**
As the data size increases to 100,000, the Sequential method begins to slow down noticeably because one core is doing all the heavy lifting. At this stage, **Multiprocessing** overtakes Sequential execution. The time saved by calculating the scores simultaneously across multiple cores finally outweighs the initial setup time (overhead) required by the Operating System. **Multithreading** remains slow due to Python's Global Interpreter Lock (GIL) preventing true parallel math calculations.

**3. Large Dataset (1,000,000 Players): True Parallelism**
At 1,000,000 players, the server is under extreme load. The Sequential method creates a massive bottleneck, taking a highly noticeable amount of time to finish. Here, **Multiprocessing** becomes the absolute fastest method by a wide margin. The initial overhead cost of spawning processes is now completely insignificant compared to the massive amount of time saved by dividing the heavy workload across 4 or 8 physical CPU cores. This proves that Multiprocessing is the only viable architecture for scaling high-load game servers.

---

## 6.0 Conclusion

This project successfully demonstrated how different execution models impact CPU-heavy server tasks. The results proved that **Sequential** execution is too slow for processing large-scale player data, while **Multithreading** fails to improve performance due to Python's Global Interpreter Lock (GIL). 

**Multiprocessing** emerged as the clear winner. By dividing the workload across multiple physical CPU cores, it bypassed the GIL to achieve true parallelism and drastically reduced execution time. Ultimately, for high-load game servers, a Multiprocessing architecture is the most effective way to eliminate bottlenecks and ensure a lag-free experience for users.

---

## 7.0 User Manual 

### 7.1 System Requirements

Before downloading and running the project, ensure that your local development environment meets the following minimum system requirements:

* **Operating System:** Windows 10/11, macOS, or any standard Linux distribution.
* **Python Version:** Python 3.6 or newer installed on your system.
* **Hardware:** A multi-core processor (CPU). *(Note: A system with at least 4 to 8 CPU cores is recommended to clearly observe the performance improvements generated by the Multiprocessing architecture).*
* **Required Libraries:** * `random`, `time`, `threading`, `multiprocessing` (These are pre-installed with standard Python).

### 7.2 Installation Steps

1. Clone or download the repository to your local machine.
2. Open your preferred IDE (e.g., Microsoft Visual Studio or VS Code) or terminal.
3. Ensure Python is installed by running: `python --version`.
4. Install the required visualization library by running the following command in your terminal:
   ```bash
   pip install matplotlib

### 7.3 How to Run the Program
1. Navigate to the project directory containing the source code.
2. Execute the main script via the terminal:
   ```bash
   python gamescore.py
   ```
3. Wait for the data generation to complete. The terminal will provide real-time status updates as it executes Test A, Test B, and Test C sequentially. 
4. Upon completion, review the terminal dashboard for the execution times and check the project directory for the generated log files and performance graph.

### 8.0 Source Code
```python
import random
import time
import threading
import multiprocessing
import matplotlib.pyplot as plt

# -------------------------------
# CONFIG
# -------------------------------
NUM_PLAYERS = 1000
NUM_THREADS = 4
NUM_PROCESSES = multiprocessing.cpu_count()

# -------------------------------
# DATA GENERATION
# -------------------------------
def generate_scores(n):
    return [random.randint(0, 1000) for _ in range(n)]

# -------------------------------
# CPU-HEAVY RANK FUNCTION
# -------------------------------
def assign_rank(score):
    for _ in range(200):  # CPU load
        score = (score * score + 123) % 1001

    if score < 200:
        return "Iron"
    elif score < 400:
        return "Bronze"
    elif score < 600:
        return "Silver"
    elif score < 800:
        return "Gold"
    elif score < 900:
        return "Platinum"
    else:
        return "Diamond"

# -------------------------------
# SEQUENTIAL
# -------------------------------
def sequential_ranking(scores):
    return [assign_rank(s) for s in scores]

# -------------------------------
# THREADING
# -------------------------------
def thread_worker(scores, results, index):
    results[index] = [assign_rank(s) for s in scores]

def threaded_ranking(scores):
    threads = []
    results = [None] * NUM_THREADS
    chunk_size = len(scores) // NUM_THREADS

    for i in range(NUM_THREADS):
        start = i * chunk_size
        end = len(scores) if i == NUM_THREADS - 1 else (i + 1) * chunk_size
        t = threading.Thread(target=thread_worker, args=(scores[start:end], results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return [item for sublist in results for item in sublist]

# -------------------------------
# MULTIPROCESSING
# -------------------------------
def process_worker(scores):
    return [assign_rank(s) for s in scores]

def multiprocessing_ranking(scores):
    chunk_size = len(scores) // NUM_PROCESSES

    chunks = []
    for i in range(NUM_PROCESSES):
        start = i * chunk_size
        end = len(scores) if i == NUM_PROCESSES - 1 else (i + 1) * chunk_size
        chunks.append(scores[start:end])

    with multiprocessing.Pool(NUM_PROCESSES) as pool:
        results = pool.map(process_worker, chunks)

    return [item for sublist in results for item in sublist]

# -------------------------------
# COUNT RANKS
# -------------------------------
def count_ranks(ranks):
    count = {
        "Iron": 0, "Bronze": 0, "Silver": 0,
        "Gold": 0, "Platinum": 0, "Diamond": 0
    }
    for r in ranks:
        count[r] += 1
    return count

# -------------------------------
# TIME MEASURE
# -------------------------------
def measure_time(func, scores):
    start = time.time()
    result = func(scores)
    end = time.time()
    return end - start, result

# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    print(f"\n[+] Generating {NUM_PLAYERS} player scores...\n")
    scores = generate_scores(NUM_PLAYERS)

    # SEQUENTIAL (used for rank display and as a baseline)
    seq_time, seq_result = measure_time(sequential_ranking, scores)
    rank_distribution = count_ranks(seq_result)

    # Measure Threading and Multiprocessing
    thread_time, _ = measure_time(threaded_ranking, scores)
    mp_time, _ = measure_time(multiprocessing_ranking, scores)

    # -------------------------------
    # OUTPUT: RANK DISTRIBUTION BOX
    # -------------------------------
    print("+" + "-"*35 + "+")
    print(f"| {'PLAYER RANK DISTRIBUTION':^33} |")
    print("+" + "-"*15 + "+" + "-"*19 + "+")
    print(f"| {'Rank':^13} | {'Count':^17} |")
    print("+" + "-"*15 + "+" + "-"*19 + "+")
    for rank, total in rank_distribution.items():
        print(f"| {rank:<13} | {total:<17} |")
    print("+" + "-"*15 + "+" + "-"*19 + "+")
    print(f"| {'Total Players':<13} | {sum(rank_distribution.values()):<17} |\n")

    # -------------------------------
    # OUTPUT: PERFORMANCE BOX
    # -------------------------------
    print("+" + "-"*45 + "+")
    print(f"| {'PERFORMANCE COMPARISON (' + str(NUM_PROCESSES) + ' Cores)':^43} |")
    print("+" + "-"*20 + "+" + "-"*24 + "+")
    print(f"| {'Method':<18} | {'Time (seconds)':<22} |")
    print("+" + "-"*20 + "+" + "-"*24 + "+")
    print(f"| {'Sequential':<18} | {seq_time:<22.4f} |")
    print(f"| {'Threading':<18} | {thread_time:<22.4f} |")
    print(f"| {'Multiprocessing':<18} | {mp_time:<22.4f} |")
    print("+" + "-"*20 + "+" + "-"*24 + "+\n")

    # -------------------------------
    # GRAPHING: SINGLE PERFORMANCE GRAPH
    # -------------------------------
    plt.figure(figsize=(8, 6))

    # Data for the plot
    methods = ["Sequential", "Threading", "Multiprocessing"]
    times = [seq_time, thread_time, mp_time]
    bar_colors = ['#ff9999', '#66b3ff', '#99ff99']

    # Generate the bar chart
    bars = plt.bar(methods, times, color=bar_colors, edgecolor='black')

    # Polish the graph
    plt.title(f"Execution Time Comparison ({NUM_PLAYERS} Players)")
    plt.xlabel("Execution Method")
    plt.ylabel("Time (seconds) - Lower is Better")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add specific time values on top of each bar
    for i, v in enumerate(times):
        plt.text(i, v + (max(times)*0.01), f"{v:.4f}s", ha='center')

    # Save and display
    plt.tight_layout()
    plt.savefig("performance_graph.png", dpi=300)
    print(f"[+] Graph saved as: performance_graph.png")
    plt.show()
```
