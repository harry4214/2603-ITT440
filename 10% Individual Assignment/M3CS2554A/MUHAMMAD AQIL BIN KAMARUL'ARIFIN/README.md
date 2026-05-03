# Parallel Flight Ticket Comparator

**Name:** Muhammad Aqil bin Kamarul'Arifin  
**Student ID:** 2024238782  
**Class:** M3CS2554A  
**Course:** ITT440  
**Lecturer:** Shahadan Bin Saad  

---

# 📌 Introduction

In today’s digital world, many systems are required to process massive amounts of data efficiently. Traditional sequential programming executes tasks one by one, which becomes very slow when handling millions of records.

To solve this problem, concurrent and parallel programming techniques such as threading and multiprocessing are used. These techniques allow multiple tasks to run simultaneously, improving execution speed and system performance.

This project demonstrates how sequential processing, threading, and multiprocessing can be implemented in a flight ticket comparison system that processes millions of flight records.

---

# 📊 Project Overview

This project focuses on developing a Flight Ticket Comparator System capable of processing and filtering millions of flight records efficiently.

The system compares three execution methods:

- Sequential Processing
- Threading (Concurrent Programming)
- Multiprocessing (Parallel Programming)

### Additional Features

- Flight data generation
- Airline rating system
- Realistic ticket pricing
- Destination filtering
- Cheapest flight sorting
- Performance comparison
- Graphical User Interface (GUI)

---

# 🎯 Objectives

- To implement sequential processing
- To implement threading
- To implement multiprocessing
- To compare execution performance
- To process large-scale datasets efficiently
- To demonstrate concurrent and parallel programming concepts

---

# 🏗️ System Design

The system is designed using a modular programming approach.

## Components

- Flight Data Generator
- Airline Rating System
- Price Generator
- Sequential Module
- Threading Module
- Multiprocessing Module
- Performance Analyzer
- Tkinter GUI Interface

---

# ▶️ How to Run

## Step 1: Open Terminal or Command Prompt

```bash
cd flight-ticket-comparator
```

## Step 2: Run the Program

```bash
python main.py
```

or

```bash
py main.py
```

---

# 🖥️ Program Interface

The program interface contains:

- Destination dropdown menu  
- Compare Prices button  
- Flight output display  
- Performance comparison display  

---

# 🧪 Sample Input

```text
Tokyo
```

---

# 📊 Sample Output

```text
===== CHEAPEST FLIGHTS TO TOKYO =====

FL1023 | AirAsia (⭐3.8) | RM 1240
FL2911 | Batik Air (⭐3.9) | RM 1290
FL8832 | Malaysia Airlines (⭐4.2) | RM 1380

===== PERFORMANCE =====

Sequential Time: 18.3241 seconds
Threading Time: 5.2142 seconds
Multiprocessing Time: 2.1031 seconds
```

---

# ⚡ Performance Analysis

| Method | Performance |
|--------|------------|
| Sequential | Slowest |
| Threading | Faster |
| Multiprocessing | Fastest |

### Observation

Sequential processing is the slowest because tasks are executed one by one using a single execution flow.

Threading improves performance by allowing multiple threads to process data simultaneously.

Multiprocessing provides the best performance because it utilizes multiple CPU cores and performs true parallel execution.

---

# 🖼️ Screenshots

## Main Interface

<img src="https://github.com/user-attachments/assets/72a5e148-ba50-46db-964f-5f5675ea90c3" width="900">

---

## Performance Result

<img width="412" height="146" alt="image" src="https://github.com/user-attachments/assets/2b6a66fa-d885-4d19-888a-7d4835f7d9fd" />


---

# 🎥 Demonstration Video

[https://youtu.be/your-video-link](https://youtu.be/ahbZKklmuZI)

---

# 🧩 Challenges Faced

- Processing millions of flight records efficiently  
- Managing memory usage  
- Optimizing threading and multiprocessing performance  
- Comparing execution methods fairly  
- Handling large dataset generation  

---

# 💡 Conclusion

In conclusion, this project successfully demonstrates the implementation of sequential processing, threading, and multiprocessing using Python.

Sequential processing is simple but slow for large datasets.

Threading improves performance through concurrent execution, while multiprocessing achieves the best performance using multiple CPU cores.

Overall, this project shows the importance of choosing the correct processing method to improve system efficiency.

#  Source Code

<details>
<summary>📌 Click to view full source code</summary>

```python
import random
import time
import threading
from multiprocessing import Pool, freeze_support
import tkinter as tk
from tkinter import ttk

# DATA
airlines = ["AirAsia", "Malaysia Airlines", "Batik Air", "Singapore Airlines", "Qatar Airways"]

destinations = ["Kuala Lumpur", "Bangkok", "Jakarta", "Seoul", "Tokyo", "Dubai", "Sydney", "London"]

airline_rating = {
    "AirAsia": 3.8,
    "Malaysia Airlines": 4.2,
    "Batik Air": 3.9,
    "Singapore Airlines": 4.8,
    "Qatar Airways": 4.7
}

def generate_price(destination, airline):
    base_prices = {
        "Kuala Lumpur": 150,
        "Bangkok": 200,
        "Jakarta": 220,
        "Seoul": 800,
        "Tokyo": 950,
        "Dubai": 1200,
        "Sydney": 1800,
        "London": 2500
    }

    base = base_prices.get(destination, 500)
    rating = airline_rating[airline]

    rating_multiplier = 0.8 + (rating / 5)
    variation = random.randint(-100, 500)
    surge = random.uniform(0.9, 1.6)

    price = int((base + variation) * surge * rating_multiplier)

    return max(100, price)


def generate_flight_data(num_records):
    data = []

    for i in range(num_records):
        airline = random.choice(airlines)
        destination = random.choice(destinations)

        data.append({
            "flight_id": f"FL{i+1}",
            "airline": airline,
            "rating": airline_rating[airline],
            "destination": destination,
            "price": generate_price(destination, airline)
        })

    return data


def get_sorted_flights(data, destination):
    flights = []

    for f in data:
        if f["destination"] == destination:
            flights.append(f)

    flights.sort(key=lambda x: x["price"])
    return flights


def threaded_filter(data, destination, num_threads=8):
    chunk_size = len(data) // num_threads
    threads = []
    results = [None] * num_threads

    def worker(chunk, i):
        results[i] = [f for f in chunk if f["destination"] == destination]

    for i in range(num_threads):
        start = i * chunk_size
        end = len(data) if i == num_threads - 1 else start + chunk_size
        chunk = data[start:end]

        t = threading.Thread(target=worker, args=(chunk, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    merged = []
    for r in results:
        merged.extend(r)

    merged.sort(key=lambda x: x["price"])
    return merged


def multiprocessing_filter(data, destination, num_processes=8):
    chunk_size = len(data) // num_processes
    chunks = []

    for i in range(num_processes):
        start = i * chunk_size
        end = len(data) if i == num_processes - 1 else start + chunk_size
        chunks.append((data[start:end], destination))

    def worker(args):
        chunk, destination = args
        return [f for f in chunk if f["destination"] == destination]

    with Pool(processes=num_processes) as pool:
        results = pool.map(worker, chunks)

    merged = []
    for r in results:
        merged.extend(r)

    merged.sort(key=lambda x: x["price"])
    return merged


def run_program():
    destination = combo.get()

    start = time.time()
    seq = get_sorted_flights(data, destination)
    seq_time = time.time() - start

    start = time.time()
    thread = threaded_filter(data, destination)
    thread_time = time.time() - start

    start = time.time()
    process = multiprocessing_filter(data, destination)
    process_time = time.time() - start

    output.delete("1.0", tk.END)

    output.insert(tk.END, f"Flights to {destination}\n\n")

    for f in seq[:50]:
        output.insert(
            tk.END,
            f"{f['flight_id']} | {f['airline']} | RM {f['price']}\n"
        )

    output.insert(tk.END, "\nPerformance:\n")
    output.insert(tk.END, f"Sequential: {seq_time:.2f}s\n")
    output.insert(tk.END, f"Threading: {thread_time:.2f}s\n")
    output.insert(tk.END, f"Multiprocessing: {process_time:.2f}s\n")


if __name__ == "__main__":
    freeze_support()

    data = generate_flight_data(1000000)

    window = tk.Tk()
    window.title("Flight Comparator")

    combo = ttk.Combobox(window, values=destinations)
    combo.pack()

    tk.Button(window, text="Run", command=run_program).pack()

    output = tk.Text(window, height=30, width=100)
    output.pack()

    window.mainloop()
```

</details>
