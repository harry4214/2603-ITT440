import time
import hashlib
import random
import string
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from tqdm import tqdm

# ---------------------------------------------------------
# FUNGSI KERJA
# ---------------------------------------------------------
def compute_heavy_hash(plate):
    """Simulasi beban CPU (Parallel)"""
    result = plate
    for _ in range(2000):  
        result = hashlib.sha256(result.encode()).hexdigest()
    return result

def verify_io(plate):
    """Simulasi beban Network/Waiting (Concurrent)"""
    time.sleep(0.01)
    return "AVAILABLE"

def worker_task(args):
    prefix, digits = args
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    plate = f"{prefix}{letters}{digits}"
    
    compute_heavy_hash(plate)
    verify_io(plate)
    return plate

# ---------------------------------------------------------
# FUNGSI PEMPROSESAN
# ---------------------------------------------------------

def run_sequential(tasks):
    print("\n[1/3] Generating in sequential...")
    results = []
    for t in tqdm(tasks, desc="Sequential Progress"):
        results.append(worker_task(t))
    return results

def run_concurrent(tasks):
    print("\n[2/3] Generating in concurrent (Threading)...")
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(tqdm(executor.map(worker_task, tasks), total=len(tasks), desc="Concurrent Progress"))
    return results

def run_parallel(tasks):
    print("\n[3/3] Generating in parellel (8 Cores Multiprocessing)...")
    # max_workers=8 memaksa penggunaan 8 core
    with ProcessPoolExecutor(max_workers=8) as executor:
        results = list(tqdm(executor.map(worker_task, tasks), total=len(tasks), desc="Parallel Progress  "))
    return results

# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=== JPJ PERFORMANCE BENCHMARK CONFIGURATION ===")
    
    # INPUT INTERAKTIF
    try:
        input_user = input("How many plate numbers do you want to generate? (cth: 500): ")
        jumlah_data = int(input_user)
        
        if jumlah_data <= 0:
            print("Please enter a number greater than 0.")
            exit()
    except ValueError:
        print("Error: Please enter number only")
        exit()

    # Setup Data berdasarkan input user
    TASKS = [("V", "2026") for _ in range(jumlah_data)]
    
    print("-" * 45)
    print(f"Target: {jumlah_data} plate number.")
    print(f"The system has {multiprocessing.cpu_count()} logical CPU cores.")
    print("-" * 45)

    # 1. SEQUENTIAL
    start_seq = time.time()
    run_sequential(TASKS)
    end_seq = time.time()

    # 2. CONCURRENT
    start_con = time.time()
    run_concurrent(TASKS)
    end_con = time.time()

    # 3. PARALLEL
    start_par = time.time()
    run_parallel(TASKS)
    end_par = time.time()

    # --- RUMUSAN PRESTASI ---
    time_seq = round(end_seq - start_seq, 4)
    time_con = round(end_con - start_con, 4)
    time_par = round(end_par - start_par, 4)

    print("\n" + "="*45)
    print(f"  Performance Results for {jumlah_data} DATA")
    print("="*45)
    print(f"1. Sequential      : {time_seq} seconds")
    print(f"2. Concurrent      : {time_con} seconds (Threading)")
    print(f"3. Parallel (8 Core): {time_par} seconds (Multiprocessing)")
    print("-" * 45)
    
    if time_par > 0:
        pantas_par = round(time_seq / time_par, 1)
        print(f"Conclusion: 8-core parallel processing is {pantas_par}x faster than sequential execution!")
    
    print("="*45)