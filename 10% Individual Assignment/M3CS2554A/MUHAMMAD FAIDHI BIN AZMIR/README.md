# 🚀 Scalable File Download Simulator: Performance Analysis Using Sequential, Concurrent, and Parallel Programming   
**Lecturer:** Shahadan Bin Saad  

**NAME:** MUHAMMAD FAIDHI BIN AZMIR

**STUDENT ID:** 2024666708

**CLASS:** M3CS2554A

**COURSE CODE:** ITT440 Network Programming

---

# 🎯 1. Mission Objective  
In modern computing systems, performance and efficiency are critical when handling large-scale tasks. Traditional sequential execution becomes a bottleneck when processing thousands of operations.

This project introduces a **Scalable File Download Simulator**, designed to evaluate and compare three execution models:
- Sequential Programming  
- Concurrent Programming (ThreadPool)  
- Parallel Programming (ProcessPool)  

---

# 💻 2. Hardware & Environment  
- **Processor:** Multi-core CPU  
- **Memory:** Minimum 4GB RAM  
- **Operating System:** Windows / Linux / macOS  
- **Programming Language:** Python 3.x  

### 📦 Libraries Used:
- concurrent.futures  
- multiprocessing  
- matplotlib (optional)

---

# 🛠️ 3. Deployment Guide  

## A. Setup Environment  
```bash
mkdir parallel_download_simulator
cd parallel_download_simulator
python -m venv venv
venv\Scripts\activate
pip install matplotlib
```
---
# 🛠️ 4. Launch Program
```bash
python parallel_download_simulator_pool.py
```
---
# 📊 5. Performance Analytics  

## 🔹 Example (5000 Tasks)

| Method | Execution Time |
|--------|--------------|
| ThreadPool | 7.88s |
| ProcessPool | 13.84s |
| Sequential | 159.47s |

### 🚀 Performance Insight
- ThreadPool is the fastest for this workload  
- ProcessPool is faster than Sequential but slower than ThreadPool  
- Sequential is the slowest  

---

## 🔹 Example (Large Scale)

| Method | Performance |
|--------|------------|
| ThreadPool | Fastest ⚡ |
| ProcessPool | Moderate 🚀 |
| Sequential | Slowest 🐢 |

---

# 📈 6. Performance Graph  

After running the program, a graph will be generated automatically:



📸 Insert your graph below after running:

![Performance Graph](performance_graph.png)

---

# 🧠 7. How It Works  

The system simulates file download tasks using both I/O and CPU workload:

- `time.sleep()` → simulates I/O delay  
- Loop computation → simulates CPU work  

---

## 🔹 Execution Models

### 🧍 Sequential  
- Executes tasks one by one  
- No optimization  

### 🧵 ThreadPool (Concurrent)  
- Uses multiple threads  
- Best for I/O-bound tasks  
- Allows overlapping execution  

### ⚡ ProcessPool (Parallel)  
- Uses multiple CPU cores  
- Executes tasks simultaneously  
- Suitable for CPU-bound tasks  

---

# 🔍 Key Insight  

ThreadPool performed the best because the workload is primarily **I/O-bound**, allowing threads to overlap waiting time efficiently.

ProcessPool introduces additional overhead, making it less efficient for this specific scenario.

---

# 🏁 8. Conclusion  

- Sequential execution is inefficient for large-scale tasks  
- Concurrent programming improves performance significantly  
- Parallel programming is powerful but depends on workload type  

### 🎯 Final Verdict  
Choosing the correct execution model is essential for achieving optimal performance.

---

# 💡 9. Future Improvements  

- Add real-time monitoring  
- Increase number of tasks (100,000+)  
- Combine threading and multiprocessing  
- Improve graph visualization  

---

# 🎥 10. YouTube Demonstration  

[(link here)](https://youtu.be/iVtJImSHK0Q)
