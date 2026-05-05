# NUR ANIS ALLYSHA BINTI SHAMSUL AZUAN

# ೀ⋆｡˚જ⁀➴PARALLEL PASSWORD STRENGTH ANALYZER ִֶ ೀ⋆｡˚જ⁀➴

**STUDENT NAME:** NUR ANIS ALLYSHA BINTI SHAMSUL AZUAN  
**STUDENT ID:** 2024645518  
**CLASS:** M3CS2554B  
**LECTURER:** SIR SHAHADAN BIN SAAD  
**VIDEO LINK:** [Watch the Demonstration ꕤ｡˚⋆](https://youtu.be/CRlZ2w8Vqu4)

---

### Introduction ⋅°❀⋆.ೃ࿔*:･
This project is a high-performance Python-based utility designed to audit the security strength of massive credential datasets. The core objective is to benchmark and compare three distinct execution models to determine the most efficient method for handling CPU-intensive security tasks:
* **Sequential:** 🐢 Standard single-threaded execution.
* **Threading (Concurrent):** 🧵 Multi-threaded execution managing tasks via time-slicing.
* **Multiprocessing (Parallel):** 🚀 Simultaneous execution across multiple CPU cores by bypassing the Global Interpreter Lock (GIL).

---

### Problem Statement ⋅°❀⋆.ೃ࿔*:･
**The Computational Challenge:** Auditing password strength using cryptographic hashing (SHA-256) is a **CPU-bound** task. When processing 600,000 records, a sequential approach results in a significant hardware bottleneck, causing unacceptably long execution times for real-world applications.

**The Technical Bottleneck:** Standard Python execution is restricted by the **Global Interpreter Lock (GIL)**, which prevents threads from utilizing multiple CPU cores for mathematical calculations. This project demonstrates how a Parallel architecture can overcome this limitation to fully utilize modern multi-core hardware. ⚡

---

### System Requirements ⋅°❀⋆.ೃ࿔*:･
* **OS:** Windows 11
* **Python:** Version 3.8 or higher.
* **Hardware:** Multi-core processor .
* **Editor:** Visual Studio Code.

---

### How to Run in VS Code ⋅°❀⋆.ೃ࿔*:･
1. **Open Terminal:** n VS Code, open the integrated terminal by pressing Ctrl +  ` (backtick). ✨
2. **Execute Script:** Run the program by typing the following command:
   ```bash
   python password_analyzer.py
3. **Data Generation:** The program will automatically generate 600,000 unique passwords in-memory to simulate a massive security database. 📦✨
4. **View Analysis:** The terminal will display a live dashboard comparing the execution speeds of all three methods (Sequential, Threading, and Parallel). 📊💖
5. **Final Summary:** Upon completion, the program displays the **Performance Gain** and total **System Throughput** (passwords processed per second). 🚀🍭

---

### Sample Output ⋅°❀⋆.ೃ࿔*:･
<img width="619" height="340" alt="image" src="https://github.com/user-attachments/assets/0575383f-7133-4d88-9a76-4e07cdfa1a7e" />

---

### Source code ⋅°❀⋆.ೃ࿔*:･
<img width="842" height="787" alt="image" src="https://github.com/user-attachments/assets/62f333f4-ba52-4d74-9409-c9d740038e7b" />
/
<img width="882" height="680" alt="image" src="https://github.com/user-attachments/assets/1eb3d2d4-bf36-4c71-90d5-a1f3b4ddf574" />

---

### Conclusion ⋅°❀⋆.ೃ࿔*:･
The development and execution of the **Parallel Password Strength Analyzer** successfully highlight how system architecture impacts high-volume data processing. Through benchmarking **600,000 records**, several key technical insights were established:

* **The Parallel Advantage:** By utilizing `multiprocessing`, the application successfully bypassed Python’s **Global Interpreter Lock (GIL)**. This allowed the workload to be distributed across all available CPU cores, resulting in a significant performance gain (approximately **6x to 8x faster** than sequential processing).
  
* **Concurrency vs. Parallelism:** The results confirm that **Threading** is insufficient for CPU-bound tasks like cryptographic hashing. While threads are excellent for I/O operations, they remain bottlenecked by the GIL during mathematical calculations. True parallelism via separate processes is the only way to unlock the hardware's full potential.

* **Scalability:** The use of **batch chunking** proved essential for handling massive datasets. It minimized the overhead of inter-process communication, allowing for a throughput of tens of thousands of passwords per second.

In summary, this project proves that standard sequential programming is a major bottleneck for modern security audits. To build scalable, high-performance network tools, we must leverage **parallel architectures** to ensure that computational resources are used to their absolute max! 🚀🍭✨

---

### Video Demonstration ⋅°❀⋆.ೃ࿔*:･
(https://youtu.be/CRlZ2w8Vqu4)
