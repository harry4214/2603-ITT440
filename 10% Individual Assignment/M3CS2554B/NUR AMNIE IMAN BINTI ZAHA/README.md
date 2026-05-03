# 2603-ITT440
# NUR AMNIE IMAN BINTI ZAHA (2024272968)
# M3CS2554B
# 📊 Parallel Text Processing Performance Analyzer

---

## 📌 PROJECT TITLE
Parallel Text Processing Performance Analyzer

---

## 📖 INTRODUCTION
This project is developed to compare the performance of different programming approaches in processing large-scale data using Python. It focuses on sequential processing, threading and multiprocessing techniques.

A large dataset of 4,000,000 text lines is generated and processed to measure execution time for each method. The results are then displayed in a table and visualized using a graph.

The main goal of this project is to show how parallel programming can improve performance compared to traditional sequential execution when handling big data.

---

## ❗ PROBLEM STATEMENT
Modern systems process large volumes of data and choosing the right execution method is critical for performance. Sequential processing can be slow when handling large datasets, while concurrent and parallel techniques may improve execution time.

This project aims to analyze and compare the performance of three approaches: sequential processing, threading and multiprocessing in Python. The system processes a large dataset (millions of text lines) and measures execution time to determine the most efficient method.


**The problem addressed is:**  
👉 Which processing method provides the best performance when handling large-scale text data?

---

## 💻 SYSTEM REQUIREMENTS
- Operating System: Windows / macOS / Linux  
- Python Version: Python 3.8 or higher  
- Recommended IDE: Visual Studio Code  
- Libraries: matplotlib (for data visualization)  
- RAM: Minimum 8GB (recommended for large dataset processing)  
- CPU: Multi-core processor (recommended for multiprocessing)

---

## ⚙️ INSTALLATION STEPS

### 1. Install Python
- Download Python from official website  
- Ensure Python is added to PATH  

### 2. Install required library
Run in terminal:
```bash
python -m pip install matplotlib
```

### 3. (Optional) Install Visual Studio Code
- Download and install Visual Studio Code
- Install Python extension

---

## ▶️ HOW TO RUN THE PROGRAM

### Step 1: Open Project
Open the project folder in Visual Studio Code


### Step 2: Open Terminal
Press:
```bash
Ctrl+
```

### Step 3: Install Required Library (First Time Only)
```bash
pip install matplotlib
```

### Step 4: Run the Program
```bash
ptext_analyzer.py
```

---

## ⏳ PROGRAM EXECUTION FLOW

### 1. Data Generation
The program generates a large dataset:
```bash
Generating HEAVY DATA (4,000,000 lines)... Please wait.
```

### 2. Execution Methods
The system runs three processing methods:
```bash
Running Multiprocessing...
Running Threading...
Running Sequential...
```


### 3. Performance Results

The terminal will display a comparison table:

```bash
- Method               | Time (Seconds)
--------------------------------------
- Multiprocessing      | fastest
- Threading            | medium
- Sequential           | slowest
```


### 4. Graph Output

- A performance graph will appear in a pop-up window  
- The graph will also be saved automatically as:
```bash
  performance_graph.png
```

  ---

  ## 📥 SAMPLE INPUT 

The system automatically generates a large dataset consisting of 4,000,000 lines of repeated text:
- Wujudmu di sini di tanah anak merdeka. Bagai obor ilmu memayungi putera puterinya.
(repeated 4,000,000 times)
<img width="1280" height="761" alt="image" src="https://github.com/user-attachments/assets/0b3bb1f3-7873-47c1-a518-55bbdd12865c" />


---

## 📤 SAMPLE OUTPUT

### Terminal Output
<img width="1232" height="576" alt="image" src="https://github.com/user-attachments/assets/11715cfe-f964-4925-b7e5-5ec83e58622e" />


### Real Output
<img width="963" height="338" alt="image" src="https://github.com/user-attachments/assets/ed9752f4-c5ef-411e-aead-f661c2b69585" />
<img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/dac8ce13-b2cd-48ad-8b4a-6621a7b6bccf" />



---

## 💻 SOURCE CODE

The full source code for this project is provided:
<img width="1280" height="725" alt="image" src="https://github.com/user-attachments/assets/c35c1c32-6c5e-4783-af5e-20f0fd077f76" />
<img width="1273" height="991" alt="image" src="https://github.com/user-attachments/assets/f2351721-c69a-48d8-8a17-f0dc64336b91" />
<img width="1280" height="849" alt="image" src="https://github.com/user-attachments/assets/daaac9f1-09e1-42b6-976f-d80ea2d01273" />
<img width="1280" height="858" alt="image" src="https://github.com/user-attachments/assets/f5f7d21d-1b58-41c9-b57d-fac798d527ce" />
<img width="1280" height="498" alt="image" src="https://github.com/user-attachments/assets/db1f8987-0e4b-49d2-9a23-1f86e5385210" />


It includes:
- Data generation
- Sequential processing
- Threading implementation
- Multiprocessing implementation
- Performance comparison
- Graph visualization

---

## 📌 CONCLUSION

This project successfully demonstrates the performance differences between sequential, threading and multiprocessing approaches when handling large-scale data consisting of millions of text lines.

Based on the results obtained, multiprocessing achieved the best performance with an execution time of 4.5262 seconds, making it the fastest method. Threading showed moderate performance at 10.4273 seconds, while sequential processing was the slowest at 11.2694 seconds.

The significant improvement in multiprocessing performance is due to its ability to utilize multiple CPU cores for true parallel execution. In contrast, threading is limited by Python’s Global Interpreter Lock (GIL), which restricts full parallelism for CPU-intensive tasks. Sequential processing, which executes tasks one by one, results in the longest execution time.

Overall, the results clearly prove that parallel programming, particularly multiprocessing, greatly enhances efficiency and performance when processing large-scale, CPU-intensive data.

---

## 🎥 VIDEO DEMONSTRATION

👉 Insert your YouTube video link here:
https://youtu.be/-wmzA3Xqhcs


