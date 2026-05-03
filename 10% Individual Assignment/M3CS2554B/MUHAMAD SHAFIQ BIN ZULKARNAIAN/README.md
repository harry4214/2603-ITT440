# MUHAMAD SHAFIQ BIN ZULKARNAIAN
# Parallel File Search System


# ITT440: Individual Assignment Report
**Course:** ITT440 - Network Programming  
**Group:** M3CS2554B  
**Name:** Muhamad Shafiq Bin Zulkarnaian  
**Student ID:** 2024412498  
**Lecturer:** Sir Shahadan Bin Saad   
**Video Link:** https://youtu.be/GWPKBKbuGR0?si=lYoU5lfdlZzbahfg


# 🔍 Parallel File Search System

## 📌 Description
The **Parallel File Search System** is a Python-based application designed to improve the efficiency of searching for keywords within a large number of files.

This project demonstrates the use of:
- Sequential processing  
- Concurrent programming (Threading)  
- Parallel programming (Multiprocessing)  

to compare performance and identify the most efficient method.

---

## 🎯 Objectives
- To develop a file search system using Python  
- To implement sequential, threading, and multiprocessing approaches  
- To compare execution time of each method  
- To determine the most efficient technique  

---

## 🧰 Tools and Technologies
- **Programming Language**
  - Python 3.9+  

- **Libraries**
  - `os` – file handling  
  - `time` – execution time measurement  
  - `concurrent.futures` – threading  
  - `multiprocessing` – parallel processing  

- **Development Tools**
  - Visual Studio Code (VS Code)  
  - Git & GitHub  

- **Operating System**
  - Windows 10 / Windows 11  

---

## ⚙️ System Overview
The system consists of two main modules:

1. **File Generator**
   - Generates thousands of text files (10,000 – 30,000 files)  
   - Some files contain a keyword (e.g., *"network"*)  

2. **Search System**
   - Searches for keywords using three methods:
     - Sequential  
     - Threading  
     - Multiprocessing  

---

## 🔍 Search Methods

### 1. Sequential
- Processes files one by one  
- Uses a single execution flow  
- Slow for large datasets  

### 2. Threading (Concurrent)
- Uses multiple threads  
- Processes multiple files simultaneously  
- Best for I/O-bound tasks  

### 3. Multiprocessing (Parallel)
- Uses multiple CPU cores  
- Executes tasks in parallel  
- Suitable for CPU-intensive tasks  

---

