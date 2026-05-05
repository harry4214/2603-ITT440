# NURAINI HUSNA BINTI ROSMAN
# DISCOUNT PRICE CALCULATOR
# INDIVIDUAL ASSIGNMENT: ITT440 NETWORK PROGRAMMING
1. Project Title: Discount Price Calculator
2. Student Name: Nuraini Husna binti Rosman
3. Student ID: 2024298464
4. Group: M3CS2554B
# 1. PROBLEM STATEMENT
The retail and e-commerce industries often need to process price updates for millions of products simultaneously during promotional events. A standard sequential approach is inefficient for such large volumes of data. This Discount Price Calculator project demonstrates how to optimize high-volume data processing using Concurrent and Parallel programming in Python, comparing their efficiency against a traditional Sequential approach across 6,000,000 retail items.
# 2. SYSTEM REQUIREMENTS
1. Operating System: Windows/Linux/macOS (Optimized for GitHub Codespaces/Ubuntu)
2. Programming Language: Python 3.x
3. Libraries Required:
   1. time, threading, multiprocessing, random (Standard Python libraries)
   2. matplotlib (For performance visualization and benchmarking)
# 3. KEY FEATURES
1. Dynamic User Input: The program allows users to manually define the discount and tax percentages at runtime.
2. Multi-Category Processing: Processes 1,000,000 items each for six categories: Top, Bottom, Accessories, Footwear, Outerwear, and Bags.
3. Scalable Performance: Utilizes multiple CPU cores to handle 6 million calculations efficiently.
# 4. INSTALLATION AND USAGE
1. Clone the repository to your local machine or open it in GitHub Codespaces.
2. Install the visualization library:
   pip install matplotlib
3. Run the program:
   python3 main.py
4. Provide Input: When prompted, enter your desired discount and tax rates (e.g., 50 for 50%, 6 for 6%).
# 5. SAMPLE OUTPUT
File: results.txt
The program outputs 10 detailed calculations for every category to verify the mathematical accuracy of the calculator.
<img width="739" height="373" alt="Screenshot 2026-05-03 174018" src="https://github.com/user-attachments/assets/46a575bb-11de-4e0f-ae35-b3db1ee74800" />
# 6. PERFORMANCE BENCHMARKING
Based on the execution results:
1. Parallel Execution: Achieves the lowest execution time by distributing tasks across all available CPU cores.
2. Concurrent Execution: Performance is improved via multi-threading but remains limited by the Global Interpreter Lock (GIL).
3. Sequential Execution: The slowest method as it processes items one by one.
The results are visually summarized in the automatically generated (performance_graph.png)
# 7. SCREENSHOTS
1. Terminal Output:
<img width="928" height="206" alt="Screenshot 2026-05-03 173930" src="https://github.com/user-attachments/assets/e784dd5d-fe14-45cb-9cc3-8324359234cf" />
2. Generated Graph: 
<img width="766" height="456" alt="Screenshot 2026-05-03 174838" src="https://github.com/user-attachments/assets/c03dc73a-17e3-45ea-aeef-e9602b0b205c" />
3. Source Code:
i) Sequential approach:
<img width="539" height="90" alt="Screenshot 2026-05-03 181748" src="https://github.com/user-attachments/assets/0560982d-4233-476d-ba7d-e011f11ef628" />
ii) Concurrent Approach (Threading):
<img width="1261" height="181" alt="Screenshot 2026-05-03 181810" src="https://github.com/user-attachments/assets/246f8657-bfcc-4751-86fb-547ffff5e21d" />
iii) Parallel Approach (Multiprocessing):
<img width="663" height="140" alt="Screenshot 2026-05-03 181824" src="https://github.com/user-attachments/assets/c45d28fb-a65a-4cdf-b5b2-6064797aff8b" />
# 8. DEMOSTRATION VIDEO
https://youtu.be/p0HczyRtDzY
The video covers the dynamic input feature, the generation of 6 million price calculations, and a comparison of the three computing techniques.
