# 🔐📊Password Generator and Analysis System
#### Student Name: NUR SHAHAINA BINTI MAT RASHID
#### Student ID: 2024421182
#### Group: M3CS2554B


## 1. Introduction

This project is about developing a simple password generator using Python. The program can generate a large number of passwords and check their strength. The strength is divided into three levels which are Weak, Medium, and Strong.

In this project, I also applied different programming techniques which are sequential, threading, and multiprocessing. The purpose is to understand how these methods work and compare their performance.

---

## 2. Problem Statement

When a program needs to process many tasks, doing everything one by one can be slow. In real systems, we can use concurrency and parallel programming to improve performance.

Therefore, this project is created to simulate how multiple tasks can be processed using different approaches in Python.

---

## 3. Objectives

The objectives of this project are:

- To develop a password generator using Python  
- To classify password strength into Weak, Medium, and Strong  
- To implement threading as a concurrent programming technique  
- To implement multiprocessing as a parallel programming technique  
- To compare the execution time between different methods  

---

## 4. System Description

The program works as follows:

1. The user enters the number of passwords to generate  
2. The system generates passwords using sequential method  
3. The system generates passwords using threading (concurrent) 
4. The system generates passwords using multiprocessing (parallel) 
5. The system displays the results and compares execution time  

Each generated password is also checked to determine whether it is Weak, Medium, or Strong.

---

## 5. System Requirements

- Python 3.x  
- Visual Studio Code (or any Python IDE)  
- Operating System: Windows / Mac / Linux  

---

## 6. Installation Steps

1. Install Python from https://www.python.org  
2. Install Visual Studio Code  
3. Download or clone the project from GitHub  
4. Open the project folder in VS Code 

---

## 7. How to Run the Program

Open terminal in VS Code and run:
python main.py

---

## 8. Sample Input
<img width="420" height="94" alt="image" src="https://github.com/user-attachments/assets/b106d9bc-c1e4-4c53-9082-05f284427f05" />

---

## 9. Sample Output
<img width="672" height="1058" alt="image" src="https://github.com/user-attachments/assets/d3876051-5ab2-4df0-ab8a-85a8911eba31" />




#### Bar Graph to Differentiate Three Method Performance
<img width="797" height="601" alt="image" src="https://github.com/user-attachments/assets/dbf98b9d-4782-40c5-963f-01e9e26f41b0" />





---

## 10. Source Code

### main.py :
<img width="857" height="1068" alt="image" src="https://github.com/user-attachments/assets/49bad76e-e6e3-440b-b1a2-33de0fa95eea" />
<img width="557" height="634" alt="image" src="https://github.com/user-attachments/assets/e106ec1b-31f2-441a-b02e-fd1e26d115ae" />

### multiprocessing_ver.py :
<img width="424" height="371" alt="image" src="https://github.com/user-attachments/assets/2ee3ab27-cb4c-4c4e-b376-43ebdeee209f" />

### password.py :
<img width="340" height="445" alt="image" src="https://github.com/user-attachments/assets/2a21897b-47ca-4bb6-bd89-b013ca40cd84" />

### sequential.py :
<img width="269" height="237" alt="image" src="https://github.com/user-attachments/assets/ae6a0d43-18ce-4821-8ff2-8fd77fcb0541" />

### threading_ver.py :
<img width="449" height="368" alt="image" src="https://github.com/user-attachments/assets/412e0d8d-7636-44c4-a18c-c124960ea81f" />


---

## 11. Conclusion
In conclusion, sequential, concurrent, and parallel programming are important concepts in modern computing. Sequential execution processes tasks one by one, which is simple but may be slower when handling many tasks.

Concurrent programming, such as threading, allows multiple tasks to run at the same time within a single program. This improves efficiency, especially when tasks involve waiting or input/output operations.

Parallel programming, such as multiprocessing, allows tasks to run on multiple CPU cores simultaneously. This can significantly improve performance for larger and more complex tasks.

However, the effectiveness of each approach depends on the type of task. For smaller tasks, the overhead of managing threads or processes may reduce performance. Therefore, choosing the right approach is important depending on the problem.

Overall, understanding these three techniques helps in designing more efficient and scalable programs.

---

## 12. Links  
YouTube Demo: https://youtu.be/QavcjYqufm8
