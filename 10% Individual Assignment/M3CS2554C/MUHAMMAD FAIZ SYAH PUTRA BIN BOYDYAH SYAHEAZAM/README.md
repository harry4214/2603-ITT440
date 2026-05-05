# MUHAMMAD FAIZ SYAH PUTRA BIN BOYDYAH SYAHEAZAM
# Parallel Text Sentiment Analyzer for Massive Social Media Comments 

YOUTUBE LINK: https://youtu.be/7_M8wvo6wsY

Name: MUHAMMAD FAIZ SYAH PUTRA BIN BOYDYAH SYAHEAZAM

Student ID: 2025240108

Course Code: ITT440 // Network Programming

Lecturer: Shahadan Bin Saad

Project Objective :
To develop a program that can analyze sentiment of social media comments (Positive, Negative, Neutral).

Project Overview :
The program generates 50,000 random comments using predefined word lists.
Each comment is analyzed using a sentiment function based on word scoring.
The program runs using three different approaches:
Sequential (one by one)
Threading (multi-thread)
Multiprocessing (multi-core)
Execution time for each method is recorded and compared.
Results are saved into .txt files and a simple report is generated.

Hardware:
Computer/Laptop with multi-core CPU
Minimum 8GB RAM

# HOW IT WORKS

How It Works

Step 1: Generate Dataset

The program creates 50,000 random comments using predefined word lists (positive, negative, neutral).
Each comment contains 5–15 words with uneven distribution (more positive words).

Step 2: Sentiment Analysis

Each comment is passed into analyze_sentiment().
The function:
Adds +1 for positive words
Subtracts −1 for negative words
Final classification:
Positive → score > 0
Negative → score < 0
Neutral → score = 0

Step 3: Run Different Methods
The same dataset is processed using three approaches:

Sequential → processes comments one by one
Threading → uses multiple threads to process simultaneously
Multiprocessing → uses multiple CPU cores for parallel execution

Step 4: Measure Performance

The program records execution time (seconds) for each method.
It also counts total results using Counter (Positive, Negative, Neutral).

Step 5: Save Output

Results are saved into text files:
seq.txt
thread.txt
multi.txt
Each line shows:
comment → sentiment

Step 6: Generate Report

A report file (report.txt) is created containing:
Execution time
Speed comparison
Observations and conclusion

# PROGRAM DEPLOYMENT

Program Deployment

1. Setup Environment

Install Python (version 3.x).
Use any editor like Visual Studio Code or IDLE.
No external libraries needed (only built-in modules).

2. Save the Program

Save your code as a Python file, for example:
comment_analiser.py

3. Run the Program

Open terminal / command prompt.
Navigate to the file location.
Run command:
python comment_analiser.py

# RESULT ANALYTICS

<img width="1187" height="362" alt="image" src="https://github.com/user-attachments/assets/1d03197a-045b-4bd8-88d3-7c57fbe02df3" />

All report files (.txt) will be generated for each:
- Sequential
- Threading
- Multiprocessing

<img width="618" height="142" alt="image" src="https://github.com/user-attachments/assets/418283eb-930f-4cf7-b4bb-64a0d7d7f71e" />

<img width="1431" height="744" alt="image" src="https://github.com/user-attachments/assets/bf7543df-72ed-449d-8f14-c4aa1c3ef5e6" />
<img width="1424" height="740" alt="image" src="https://github.com/user-attachments/assets/1fab2b6b-cd17-4ddb-aafa-c8f9fc3c78c6" />
<img width="1431" height="741" alt="image" src="https://github.com/user-attachments/assets/ecabcd0d-cc8b-49b3-9100-68f51e03e69e" />

# CONCLUSION

The program successfully demonstrates how sentiment analysis can be performed on a large dataset using different processing methods. It shows that sequential execution is the slowest because it processes data one by one, while threading provides only slight improvement due to limitations in handling CPU-intensive tasks.

Among all methods, multiprocessing gives the best performance because it utilizes multiple CPU cores to run tasks in parallel, significantly reducing execution time.

Overall, this project proves that choosing the right processing method is important for improving efficiency, especially when handling large-scale data.




