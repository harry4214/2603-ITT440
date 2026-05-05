# Plate Number Generator

**Course code: ITT440 Network Programming**

**Lecturer: Shahadan Bin Saad**

**Youtube Link: https://youtu.be/-7gy8-rRrdM**

# 1. Objective 
The objective of this project is to develop a plate number generator system that implements sequential, concurrent, and parallel processing techniques. The system aims to evaluate and compare the performance of these processing methods by measuring execution time and efficiency in generating large volumes of plate numbers. This study highlights the advantages and limitations of each approach, particularly in terms of resource utilization and processing speed.

# 2. System Environment

1. Processor: Quad-Core / Octa-Core CPU

2. Memory: 8GB RAM minimum

3. OS: Windows 11

4. Development tool:

   - Visual Studio Code
   - Python Extension for Visual Studio Code
5. Programming Language: Python

# 3. Result

<img width="801" height="378" alt="WhatsApp Image 2026-05-03 at 3 47 28 PM" src="https://github.com/user-attachments/assets/654f9468-70af-440b-a5d2-6b99e4ff972e" />
     
| Method      | Time Taken | CPU Usage |
|-------------|-----------|----------|
| Sequential  | 125.6s      | Low      |
| Concurrent  | 20.6s      | Medium   |
| Parallel    | 17.4s      | High     |

<img width="587" height="455" alt="image" src="https://github.com/user-attachments/assets/fbb4d604-354c-4cda-bf96-0398edeaf854" />

# 4. Conclusion

Sequential processing was the simplest to implement but showed the slowest performance, as tasks were executed one at a time without utilizing multiple CPU resources. Concurrent processing improved overall efficiency by allowing multiple tasks to be handled in an overlapping manner, resulting in better responsiveness compared to the sequential approach.

Parallel processing achieved the best performance among the three methods by distributing tasks across multiple CPU cores, enabling true simultaneous execution. This significantly reduced execution time, especially for CPU-intensive operations such as large-scale plate number generation.

Overall, the project highlights the importance of selecting an appropriate processing method based on the nature of the task. While sequential processing is suitable for simple and low-volume operations, concurrent and parallel processing provide substantial performance improvements for more complex and large-scale applications.
# MUHAMMAD MUSLIHUDDIN BIN MUHAMMAD
PLATE NUMBER GENERATOR
