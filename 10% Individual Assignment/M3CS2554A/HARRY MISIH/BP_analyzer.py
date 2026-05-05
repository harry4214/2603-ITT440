import random
import time
import threading
import multiprocessing as mp

# ============================
#  --- CONFIGURATION ---
# ============================

# Generate a large dataset of patients with random blood pressure readings
TOTAL_PATIENTS = 10_000_000 

def generate_patients(count):
    print(f"Creating {count:,} patient records...")
    patients = []
    for i in range(1, count + 1):
        # (ID, Systolic, Diastolic, Complexity)
        p = (i, random.randint(80, 160), random.randint(50, 100), random.randint(100, 300))
        patients.append(p)
    return patients

# ====================================
# --- ALGORITHM and CPU WORKLOAD ---
# ====================================

def check_bp(patient):
    p_id, sys, dia, complexity = patient
    
    # 1. Simple BP Status
    if sys > 140 or dia > 90:
        status = "High"
    elif sys < 90 or dia < 60:
        status = "Low"
    else:
        status = "Normal"

    # Simulated CPU work to make the task "heavy" enough
    dummy_math = 0
    for i in range(complexity):
        dummy_math += (i + sys) % 5 
        
    return status

# ===========================
#  --- THE METHODS ---
# ===========================

# 1. SEQUENTIAL
def run_sequential(data):
    start = time.perf_counter()
    [check_bp(p) for p in data]
    return time.perf_counter() - start

# 2. THREADING
def run_threading(data):
    start = time.perf_counter()
    threads = []
    num_threads = 6 
    chunk_size = len(data) // num_threads

    def worker(chunk):
        for p in chunk:
            check_bp(p)

    for i in range(num_threads):
        chunk = data[i * chunk_size : (i + 1) * chunk_size]
        t = threading.Thread(target=worker, args=(chunk,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    return time.perf_counter() - start

# 3. MULTIPROCESSING
def run_parallel(data):
    start = time.perf_counter()
    with mp.Pool(processes=6) as pool:
        pool.map(check_bp, data, chunksize=1000)
    return time.perf_counter() - start

# ============================
#  --- DISPLAY RESULTS ---
# ============================

if __name__ == "__main__":
    print("=== BLOOD PRESSURE ANALYZER ===")
    
    all_patients = generate_patients(TOTAL_PATIENTS)
    
    print("\nStarting benchmarks...")
    
    # 1. Sequential
    start_seq = time.perf_counter()
    final_results = [check_bp(p) for p in all_patients]
    t_seq = time.perf_counter() - start_seq
    print(f"Sequential  : {t_seq:.4f}s")
    
    # 2. Threading
    t_thr = run_threading(all_patients)
    print(f"Threading   : {t_thr:.4f}s")
    
    # 3. Multiprocessing
    t_par = run_parallel(all_patients)
    print(f"Parallel    : {t_par:.4f}s")
    
    #============================
    #  --- SUMMARY ---  
    #============================
    
    print("\n" + "="*40)
    print("        PATIENT HEALTH SUMMARY")
    print("="*40)
    print(f"High Blood Pressure  : {final_results.count('High'):,}")
    print(f"Normal Blood Pressure: {final_results.count('Normal'):,}")
    print(f"Low Blood Pressure   : {final_results.count('Low'):,}")
    print("-" * 40)
    print(f"Total Processed      : {len(final_results):,}")
    print("="*40)