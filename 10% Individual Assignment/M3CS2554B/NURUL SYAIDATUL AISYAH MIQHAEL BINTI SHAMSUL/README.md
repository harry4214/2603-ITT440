# 🎬 Movie Recommendation Analyzer: A High-Performance Implementation Using Python

---

## 📌 Introduction
This system focuses on the performance differences between Sequential, Concurrent, and Parallel programming models using Python. By processing a large dataset of 3,000,000 movie ratings, the system shows how using multiple CPU cores can significantly reduce execution time, especially for tasks that require heavy computation.

---

## ❗ Problem Statement

Processing large datasets using sequential execution is time-consuming and inefficient, especially with modern multi-core processors.

Although concurrency using threading allows multiple tasks to run at the same time, it is limited by the Global Interpreter Lock (GIL) in Python because it cannot fully use multiple CPU cores for heavy calculations.

Therefore, this system aims to:
- Identify the performance limitations of sequential and concurrent methods  
- Measure the performance improvement when using multiprocessing  
- Determine the speedup achieved when distributing workload across multiple CPU cores  

---

## ⚙️ System Requirements

To ensure the system runs smoothly, the following requirements were met:

| Component           | Details |
|---------------------|--------|
| Software            | Python 3.14 |
| Libraries           | multiprocessing, threading, collections, statistics, time, matplotlib |
| Development Tool    | VS Code (Visual Studio Code) |
| Operating System    | Windows (Local Environment) |
| Hardware            | Multi-core processor (12 cores) |

---

## 🛠️ Installation Steps

### Step 1: Install Python
Ensure Python 3.14 is installed on your system.

### Step 2: Install Required Library
Run the following command in terminal:

```bash
python3.14 -m pip install matplotlib --break-system-packages
```
### Step 3: Setup Project Directory
Ensure all source files are placed in the same project folder, for example:

Documents/ITT440/Movie Recommendation Analyzer

## ▶️ How To Run

### Step 1: Open Project Folder
Launch VS Code and open the project directory:
`Documents/ITT440/Movie Recommendation Analyzer`

---

### Step 2: Open Terminal
Open the terminal in VS Code.  
Make sure the terminal path is the same as your project folder.

---

### Step 3: Run the Program
Enter the following command:

```bash
python3.14 source_code.py
```

### Step 4: Monitor Process Generation
Observe the terminal as the system generates **3,000,000 records** and saves them into `input.txt`.

---

### Step 5: Verify Concurrent Responsiveness
Look for the **"Ping" messages** from the concurrent UI thread.  
These messages show that the system remains responsive even while processing heavy data.

---

### Step 6: View Final Performance Results
Once the analysis is complete:
- The terminal will display the **Final Performance Benchmark results**
- The file `output.txt` will be generated
- A pop-up window will appear showing the **Benchmark Results chart**

## 📊 Sample Input / Output

### 🖥️ Terminal Output
The system displays the time taken for each mode:

![Terminal Output](images/terminal.png)

- Sequential: ~148.06s  
- Concurrent: ~34.51s  
- Parallel: ~33.69s  

---

### 📄 Input File (`input.txt`)
Contains 3,000,000 generated movie rating records including:

![Input File](images/input.png)

- Movie title  
- Rating  

---

### 📄 Output File (`output.txt`)
Contains:

![Output File](images/output.png)

- Top 100 ranked movies  
- Genre classification  
- Average rating scores  

---

### 📈 Visual Output
A bar chart titled:

**"Performance Comparison: Processing 3,000,000 Records"**

Saved as `BenchmarkResults.png`

![Performance Chart](images/chart.png)

## 💻 Source Code

The system is implemented in Python and includes:

- Data generation for large-scale dataset  
- Sequential processing  
- Concurrent threading (UI responsiveness)  
- Parallel multiprocessing (multi-core execution)  
- Data aggregation and ranking  
- Performance visualization using matplotlib  

![Source Code](images/source_code.png)

---

## ✅ Conclusion

The results show that parallel programming is the most efficient approach for processing large datasets.

Sequential execution required over 148 seconds, while the parallel method reduced execution time to approximately 33 seconds by using all available CPU cores.

Although threading improves system responsiveness, it does not significantly improve performance for heavy calculations due to Python’s GIL. Therefore, multiprocessing is the most suitable method to achieve better performance when handling large amounts of data.



