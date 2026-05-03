# 🚀 **Parallel Genetic Algorithm Optimizer**

**Course Code:** ITT440 Network Programming

**Student Name:** Irdina Sofea binti Yoni

**Lecturer**: Shahadan bin Saad

**Youtube Link**: 


# 🛡️ **1. Mission Objective**

In computational problems, speed is critical. Traditional sequential execution becomes slow when processing large datasets or repetitive calculations.

This project implements a **Genetic Algorithm Optimizer** and compares three execution approaches:
- Sequential execution
- Threading (concurrent execution)
- Multiprocessing (parallel execution)

The goal is to demonstrate how **parallel computing improves performance** for CPU-intensive tasks. 


# ⚠️ **2. Problem Statement**

Traditional sequential programs process data one step at a time, which leads to slow performance when handling computationally intensive tasks such as genetic algorithms. 

In this project, the fitness evaluation of individuals requires repeated calculations across multiple generations. This becomes inefficient when executed sequentially.

Therefore, there is a need to explore more efficient approaches such as **concunrrent and parallel programming** to reduce execution time and improve performance. 


# 💻 **3. Hardware & Environment**
**1.** Processor: Multi-core CPU (recommended)

**2.** Memory: Minimum 4GB RAM 

**3.** Operating System: Kali Linux / Windows / macOS

**4.** Programming Language: Python 3.x


# ⚙️ **Developmet Guide**

**A. Setup**

Ensure Python is installed:

```bash
python3 --version
```

**B. Run Program**

Execute the program:

```bash
python3 parallel_genetic_optimizer.py
```

# 📸 **5. Program Execution**

Below is the output of the program:

<img width="1073" height="1009" alt="Screenshot 2026-04-22 223223" src="https://github.com/user-attachments/assets/8a9b9fc3-00b2-4f28-bd6c-d6c12de942a3" />

# 📊 **6. Performance Benchmark**

**Execution Time Results:**

**1.** Sequential: 9.3088 seconds

**2.** Threading: 8.6377 seconds

**3.** Multiporceessing: 4.0243 seconds

👉 **Multiprocessing** is the fastest method.

# 🧠 **7. How It Works (The Logic)**

The system uses a **Genetic Algorithm** to find optimal solutions:

**1.** Generate a random population

**2.** Evaluate fitness of each individual

**3.** Select the best individual

**4.** Perform crossover and mutation

**5.** Repeat for multiple generations

Parallelism is applied during the fitness evaluation stage, which is the most computationally intensive part.

# ⚡ **Execution Methods Explained**

**Sequential**
- Processess individuals one by one → slow

**Threading**
- Runs tasks concurrently but limited by Python's **Global Interpreter Lock (GIL)** → little improvement

**Multiprocessing**
- Uses multiple CPU core → true parallel execution → fastest

# 🏁 **8. Final Verdict**

### This project proves that:
👉 Multiprocessing significantly improves performance for CPU-bound tasks

Threading does not provid major improvement due to Python limitations, while sequential execution is the slowest.

# 🎉 **Final Result**

### ✔ Sequential: Slow
### ✔ Threading: Limited improvement
### ✔ Multiprocessing: Fastest

# 🚀 **Status: System Working Successfully**
