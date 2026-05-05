# MUHAMMAD EZAIRY DANIEL BIN FARZIS HAIREI
# Parallel Online Quiz Evaluation System for Massive Student Submissions

---

## 1. Introduction

The Parallel Quiz Evaluation System is a Python-based application developed to simulate and evaluate quiz results for a large number of students. The system uses a graphical user interface (GUI) built with Tkinter to provide an interactive experience.

The main objective of this project is to compare three different processing techniques:

- Sequential Processing  
- Multithreading  
- Multiprocessing  

---

## 2. Problem Statement

Traditional quiz evaluation systems rely on sequential processing, which becomes inefficient when handling large datasets. Also quiz marking becomes inefficient when handling a large number of students.

The main issues are:

- Slow processing time  
- Inefficient CPU utilization  
- Lack of scalability  

This project addresses these issues by implementing parallel processing techniques and analyzing their performance.

---

## 3. System Requirements

### Hardware:
- Processor: Intel i5 / Ryzen 5 or higher  
- RAM: Minimum 8GB
- Storage: At least 200MB free space
- Display: Any standard monitor (for GUI display) 

### Software:
- Python 3.9+
- Operating System: Window / macOS / Linux
- Libraries: tkinter, multiprocessing, threading, csv, random, time, os, sys  

---

## 4. Installation Steps

1. Install Python  
2. Verify installation:
```
   python --version
````

3. Create a project folder
4. Add:

   * `main.py`
   * `answer_scheme.csv`

---

## 5. How to Run

1. Open terminal
2. Navigate to project folder
3. Run:

   ```bash
   python main.py
   ```
4. Select mode (Normal / Heavy)
5. Click **Run System**

---

## 6. Sample Input / Output

###  Input (answer_scheme.csv)

![Input CSV](https://github.com/user-attachments/assets/bc36d9e3-6de9-4d2f-acd4-1a3c466979ae)

---

###  Output (Normal Mode)

![Normal Mode Output](https://github.com/user-attachments/assets/e219f704-f938-4d43-b807-441926fc5369)

---

###  Output (Heavy Mode)

![Heavy Mode Output](https://github.com/user-attachments/assets/63ae3e3a-cfcf-49b7-8da3-3d0d9215af35)

---

###  Output Final Results (CSV)

![Final CSV](https://github.com/user-attachments/assets/1e354aa1-a7a8-4553-93af-9faf33dd95c1)

---

## 7. Source Code

Main file:

* `main.py`

Contains:

* Student generation
* Answer simulation
* Marking logic
* Sequential, threading, multiprocessing implementations
* GUI system

![Source Code](https://github.com/user-attachments/assets/2906c0e0-e07f-4af2-87ec-097c9e52b42b)

---

## 8. Execution Analysis (Normal Mode vs Heavy Mode)

### Normal Mode (Lightweight Task)

In Normal Mode, the marking process only involves simple answer comparison.

#### Results Observation:

* Sequential is fastest
* Threading is slightly slower
* Multiprocessing is the slowest

#### Explanation:

**Sequential Processing**

* Executes tasks one by one
* No overhead
* Best for simple tasks

**Multithreading**

* Uses multiple threads
* Slight overhead from thread management
* Limited by the Global Interpreter Lock (GIL)

**Multiprocessing**

* Creates multiple processes
* Requires data splitting and communication
* High overhead makes it slower for small tasks

**Conclusion:**
Parallel processing is not efficient because overhead > actual computation.

---

### Heavy Mode (CPU-Intensive Task)

In Heavy Mode, additional computations are added, making the task CPU-intensive.

#### Results Observation:

* Multiprocessing becomes fastest
* Threading improves slightly but still limited
* Sequential becomes slow

#### Explanation:

**Sequential Processing**

* Handles heavy computation alone
* Cannot use multiple CPU cores
* Slower execution

**Multithreading**

* Still limited by GIL
* Cannot achieve true parallelism

**Multiprocessing**

* Uses multiple processes
* Bypasses GIL
* Fully utilizes CPU cores
* Achieves true parallel execution

**Conclusion:**
Multiprocessing performs best for CPU-intensive tasks.

---

## 9. Video Demonstration

🔗 [https://youtu.be/Osp_X5ONVtI?feature=shared]

---
