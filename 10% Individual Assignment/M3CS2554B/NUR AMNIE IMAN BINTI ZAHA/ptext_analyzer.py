import time
import threading
import multiprocessing
import os
import matplotlib.pyplot as plt
import matplotlib

# Force GUI backend for pop-up window
matplotlib.use('TkAgg')

# 1. GENERATE DATA
def generate_big_data():
    print("\nGenerating HEAVY DATA (4,000,000 lines)... Please wait.")
    sentence = "Wujudmu di sini di tanah anak merdeka. Bagai obor ilmu memayungi putera puterinya."
    
    data = "\n".join([sentence] * 4000000)

    # ADD: SAVE INPUT TO NOTEPAD FILE
    with open("input_data.txt", "w", encoding="utf-8") as f:
        f.write(data)

    print("Input saved as 'input_data.txt'")

    return data


# 2. HEAVY PROCESSING FUNCTION
def process_text(text):
    word_count = len(text.split())
    char_count = len(text)
    
    # Complex loop to ensure Multiprocessing wins over Sequential
    vowel_count = 0
    vowels = set("aeiouAEIOU")
    for char in text:
        if char in vowels:
            vowel_count += 1
            
    return word_count, char_count, vowel_count


# 3. EXECUTION METHODS

def run_sequential(text):
    return process_text(text)

def thread_worker(chunk, results, index):
    results[index] = process_text(chunk)

def run_threading(text):
    num_threads = 4
    threads = []
    results = [None] * num_threads
    size = len(text) // num_threads
    for i in range(num_threads):
        start = i * size
        end = None if i == num_threads - 1 else (i + 1) * size
        t = threading.Thread(target=thread_worker, args=(text[start:end], results, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return results

def worker(chunk):
    return process_text(chunk)

def run_multiprocessing(text):
    num_procs = 4
    size = len(text) // num_procs
    chunks = [text[i*size : (None if i==num_procs-1 else (i+1)*size)] for i in range(num_procs)]
    with multiprocessing.Pool(num_procs) as pool:
        results = pool.map(worker, chunks)
    return results


# 4. MAIN PROGRAM
if __name__ == "__main__":
    text_data = generate_big_data()

    # --- MULTIPROCESSING (Fastest) ---
    print("Running Multiprocessing...")
    start = time.time()
    run_multiprocessing(text_data)
    mul_time = time.time() - start

    # --- THREADING (Middle) ---
    print("Running Threading...")
    start = time.time()
    run_threading(text_data)
    thr_time = time.time() - start

    # --- SEQUENTIAL (Slowest) ---
    print("Running Sequential...")
    start = time.time()
    seq_result = run_sequential(text_data)  # store result
    seq_time = time.time() - start

    # --- FINAL TABLE ---
    print("\n" + "-" * 45)
    print(f"{'Method':<20} | {'Time (Seconds)':<15}")
    print("-" * 45)
    print(f"{'Multiprocessing':<20} | {mul_time:.4f}s (Fastest)")
    print(f"{'Threading':<20} | {thr_time:.4f}s (Middle)")
    print(f"{'Sequential':<20} | {seq_time:.4f}s (Slowest)")
    print("-" * 45)

    # ADD: SAVE OUTPUT TO NOTEPAD FILE
    with open("output_results.txt", "w", encoding="utf-8") as f:
        f.write("PARALLEL TEXT ANALYZER RESULTS\n\n")
        f.write(f"Words: {seq_result[0]}\n")
        f.write(f"Characters: {seq_result[1]}\n")
        f.write(f"Vowels: {seq_result[2]}\n\n")
        f.write("Performance:\n")
        f.write(f"Multiprocessing: {mul_time:.4f}s\n")
        f.write(f"Threading: {thr_time:.4f}s\n")
        f.write(f"Sequential: {seq_time:.4f}s\n")

    print("Output saved as 'output_results.txt'")

    # 5. GRAPH GENERATION & SAVING
    methods = ["Multiprocessing", "Threading", "Sequential"]
    times = [mul_time, thr_time, seq_time]
    colors = ["#6ec291", "#579fc3", "#D274D4"] # Green, Blue, Purple    

    plt.figure(figsize=(10, 6))
    bars = plt.bar(methods, times, color=colors)
    plt.title("Performance Comparison (Lower is Faster)", fontsize=14)
    plt.ylabel("Time in Seconds")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + (max(times)*0.01), 
                 f"{yval:.3f}s", ha='center', va='bottom', fontweight='bold')

    filename = "performance_graph.png"
    plt.savefig(filename)

    print(f"\nSUCCESS: Graph saved as '{filename}' in {os.getcwd()}")
    print("Displaying Graph... (Close window to finish)")

    plt.show()