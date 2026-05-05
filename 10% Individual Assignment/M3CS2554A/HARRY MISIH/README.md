
# Blood Pressure Analyzer
NAME: HARRY MISIH

STUDENT ID: 2025129703

# Introduction
In modern healthcare systems, the ability to process massive amounts of patient data from wearable devices is critical for real-time health monitoring. This project 
focuses on the computational efficiency of analyzing a dataset of 10,000,000 patient records. The system categorizes patients into health risk groups (High, Normal, or 
Low Blood Pressure) based on simulated systolic and diastolic readings.

The primary goal is to demonstrate how Sequential, Concurrent, and Parallel utilize hardware resources differently, especially on multi-core consumer hardware.

# System
## Demonstration System

Operating System: Windows 11

Python Version: 3.14

CPU Cores: 6 cores

RAM: 8GB DDR5

## User Manual

### 1. System Requirements
Operating System: Windows 10/11

Language: Python 3.8 or higher

Hardware: Minimum 4GB RAM (8GB+ recommended for 10 million records)

Libraries: Standard Python libraries (`random`, `time`, `threading`, `multiprocessing`)

### 2. Installation Steps
1.  **Install Python**: Download and install the latest version of Python from [python.org](https://www.python.org/).
2.  **Download the Project**:
    *   Clone this repository or download the `BP_analyzer.py` file directly to your computer.
3.  **Setup Environment**: No external libraries are required as the project uses built-in Python modules.

### 3. How to Run the Program
1.  Open your **Command Prompt (CMD)** or **Terminal**.
2.  Navigate to the folder where you saved the file.
3.  Run the program using the following command:
    ```bash
    python BP_analyzer.py
    ```

# Objectives
1. To develop a functional Blood Pressure Analyzer capable of processing 10 million records.

2. To evaluate the performance impact of Python’s Global Interpreter Lock (GIL) on multi-threaded execution.

3. To measure the speedup achieved by leveraging a 6-core CPU architecture through multiprocessing.

4. To provide a statistical summary of patient health risks within the generated dataset.

# Methodology
The system generates a population of 10,000,000 patients. Each record consists of:

1. Patient ID: Unique identifier.

2. Systolic Pressure: Randomly generated between 80 and 160 mmHg.

3. Diastolic Pressure: Randomly generated between 50 and 100 mmHg.
### The Algorithm
The check_bp function classifies each patient using standard clinical thresholds:

  High (Hypertension): Systolic > 140 or Diastolic > 90.

  Low: Systolic < 90 or Diastolic < 60.

  Normal: All other cases.

  ```
  def check_bp(patient):
    p_id, sys, dia, complexity = patient
    
    # 1. Simple BP Status
    if sys > 140 or dia > 90:
        status = "High"
    elif sys < 90 or dia < 60:
        status = "Low"
    else:
        status = "Normal"

    return status
```
# Performance Result
The following results were captured by running the analyzer across three different paradigms:
| Method     | Time (s) |
| :--------- | :------- |
| Sequential | 68.9123s |
| Threading  | 70.7889s |
| Parallel   | 19.4627s |

Screenshot:
<img width="399" height="200" alt="image" src="https://github.com/user-attachments/assets/d0d9afdc-d5c6-4709-8937-24401fb85d62" />


# Patient Health Summary
The analyzer successfully processed the entire dataset with the following distribution:

  High Blood Pressure: **3,947,156**

  Normal Blood Pressure: **3,827,593**

  Low Blood Pressure: **2,225,251**

  Total Processed: **10,000,000**

  Screenshot: 
<img width="414" height="202" alt="image" src="https://github.com/user-attachments/assets/4add2399-c8ca-4ea8-a45f-ee7b42940e95" />

# Conclusion
The findings confirm that for CPU-bound tasks like medical data analysis, Multiprocessing (Parallel) is significantly more efficient than Sequential or Threaded execution.
  This project highlights the importance of choosing the right concurrency model when developing high-performance network and data-processing applications in a real-world scenarios.

# YouTube Demonstration
Link: [Demo Video](https://youtu.be/1OH_vF4c38M)

