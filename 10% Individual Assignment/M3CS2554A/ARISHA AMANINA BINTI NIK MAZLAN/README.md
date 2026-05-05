# ARISHA AMANINA BINTI NIK MAZLAN
# QUIZ SCORE COLLECTOR CALCULATOR 

# INTRODUCTION
In today’s digital learning environment, thousands of students submit quiz scores simultaneously through online platforms. Processing these scores sequentially can be slow and inefficient, especially when calculating averages, rankings, and identifying top performers. To address this challenge, parallel programming techniques can be applied to improve performance and scalability. This project demonstrates how concurrent programming (threading/asyncio) and parallel programming (multiprocessing) in Python can be used to efficiently process large volumes of quiz scores.

# PROBLEM STATEMENT
Traditional sequential processing struggles when handling large datasets of quiz scores. As the number of students increases, the time required to compute averages, rankings, and statistics grows significantly.
The problem is:
- How can we efficiently process large volumes of quiz scores?
- How can we demonstrate the performance differences between sequential, concurrent, and parallel approaches?

# OBJECTIVES 
- To design a Python program that simulates large-scale quiz score processing.
- To implement concurrent programming for score collection and validation.
- To implement parallel programming for heavy computations (average, median, ranking).
- To compare execution times between sequential, concurrent, and parallel approaches.
- To provide a clear demonstration of efficiency gains using parallel programming.

# METHODOLOGY 
- Data Simulation: Generate thousands of random quiz scores.
- Sequential Approach: Process scores one by one.
- Concurrent Approach: Use threading/asyncio to collect and validate scores simultaneously.
- Parallel Approach: Use multiprocessing to compute averages and rankings across multiple CPU cores.
- Performance Measurement: Record execution times for each approach.
- Comparison: Present results in tabular/graphical form.

# CODING
import random
import time
import threading
import asyncio
import multiprocessing

# Data Generation (FAST + MEMORY SAFE)
```ssh
def generate_scores(num_scores):
    return [random.randint(0, 100) for _ in range(num_scores)]
```

# Validation
```ssh
def validate_scores(scores):
    return [s for s in scores if 0 <= s <= 100]
```

# Threading
```def threaded_validation(scores):
    chunk_size = len(scores) // 4
    threads = []
    results = []
    lock = threading.Lock()

    def worker(chunk):
        valid = validate_scores(chunk)
        with lock:
            results.extend(valid)

    for i in range(4):
        chunk = scores[i * chunk_size:(i + 1) * chunk_size]
        t = threading.Thread(target=worker, args=(chunk,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return results
```

# Asyncio (SAFE LIMIT - NO OVERLOAD)
```async def async_validate(score):
    return score if 0 <= score <= 100 else None

async def async_validation(scores):
    tasks = []
    for s in scores:
        tasks.append(async_validate(s))
        if len(tasks) > 50000:   # limit chunk (IMPORTANT)
            break

    results = await asyncio.gather(*tasks)
    return [r for r in results if r is not None]
```

# Statistics (FAST VERSION)
```def compute_statistics(scores):
    return {
        "average": sum(scores) / len(scores),
        "min": min(scores),
        "max": max(scores),
        "total_students": len(scores)
    }
```

# Multiprocessing (OPTIMIZED)
```def compute_chunk(chunk):
    return {
        "sum": sum(chunk),
        "min": min(chunk),
        "max": max(chunk),
        "count": len(chunk)
    }

def parallel_statistics(scores):
    chunk_size = len(scores) // 4
    chunks = [scores[i * chunk_size:(i + 1) * chunk_size] for i in range(4)]

    with multiprocessing.Pool(4) as pool:
        results = pool.map(compute_chunk, chunks)

    total_sum = sum(r["sum"] for r in results)
    total_count = sum(r["count"] for r in results)

    return {
        "average": total_sum / total_count,
        "min": min(r["min"] for r in results),
        "max": max(r["max"] for r in results)
    }
```

# Grade (NO FULL PRINT LOOP)
```def calculate_grade(score):
    if score >= 80:
        return "A"
    elif score >= 65:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"
```

# MAIN
```if __name__ == "__main__":

    SIZE = 30_000_000   # 🔥 30 MILLION DATA

    print("\n--- QUIZ SCORE COLLECTOR SYSTEM (10 MILLION DATA) ---\n")

    # Sequential
    start = time.time()
    scores = generate_scores(SIZE)
    seq_valid = validate_scores(scores)
    seq_stats = compute_statistics(seq_valid)
    print("Sequential:", seq_stats, "Time:", round(time.time() - start, 2))

    # Threading
    start = time.time()
    thr_valid = threaded_validation(scores)
    thr_stats = compute_statistics(thr_valid)
    print("Threading:", thr_stats, "Time:", round(time.time() - start, 2))

    # Asyncio (limited sample)
    start = time.time()
    async_valid = asyncio.run(async_validation(scores))
    async_stats = compute_statistics(async_valid)
    print("Asyncio (sample):", async_stats, "Time:", round(time.time() - start, 2))

    # Multiprocessing
    start = time.time()
    par_stats = parallel_statistics(scores)
    print("Multiprocessing:", par_stats, "Time:", round(time.time() - start, 2))

    # Sample output ONLY (NOT FULL 30M)
    print("\nSample Grades (first 5 only):")
    for i in range(5):
        print(f"Score: {scores[i]} -> Grade: {calculate_grade(scores[i])}")
```

# CODING EXPLANATION 
- generate_scores(num_scores): This function generates a list of random quiz scores between 0 and 100. It simulates student marks data, and in this system it can generate up to 30 million records.
- validate_scores(scores): This function checks whether each score is within the valid range (0–100). It removes any invalid values to ensure data accuracy before processing.
- threaded_validation(scores): This function uses threading to validate scores concurrently. The dataset is divided into 4 parts, and each thread processes one part. A lock is used to prevent data conflict when multiple threads update the same list.
- async_validation(scores): This function uses asynchronous programming to validate scores. However, it limits the number of tasks (50,000) to avoid system overload. It is mainly used to demonstrate async concept, not for full large-scale processing.
- compute_statistics(scores): This function calculates basic statistics including average score, minimum score, maximum score, and total number of students.
- parallel_statistics(scores): This function uses multiprocessing to process data in parallel. The dataset is split into chunks and distributed across multiple processes to improve performance.
- compute_chunk(chunk): This helper function calculates partial results (sum, min, max, count) for each chunk of data. The results are later combined to produce final statistics.
- multiprocessing.Pool(): This is used to create multiple worker processes. It distributes the workload across CPU cores, making the computation faster for large datasets.
- calculate_grade(score): This function assigns a grade (A, B, C, F) based on the score range.
- time.time(): This function is used to measure execution time for each method (sequential, threading, asyncio, multiprocessing) to compare their performance.

# RESULTS AND OUTPUT
## 📊 Performance Comparison

| Method           | Execution Time (s) | Total Quiz Score |
|------------------|-------------------|------------------|
| Sequential       | 8.39              | 30,000,000       |
| Threading        | 2.12              | 30,000,000       |
| Multiprocessing  | 1.84              | 30,000,000       |

<img width="882" height="369" alt="Screenshot 2026-04-28 232631" src="https://github.com/user-attachments/assets/8ac18f7b-52fa-4ec4-8199-2806a9898ca4" />


# CONCLUSION
This project successfully demonstrates the efficiency of parallel programming in Python. By comparing sequential, concurrent, and parallel approaches, it is evident that parallel processing significantly reduces execution time when handling large datasets. The Quiz Score Collector Calculator provides a practical example of how concurrency and parallelism can be applied in educational data processing, making it a unique and relevant project for academic approval.

# YOUTUBE LINK
https://youtu.be/1iSecyRYlXU
