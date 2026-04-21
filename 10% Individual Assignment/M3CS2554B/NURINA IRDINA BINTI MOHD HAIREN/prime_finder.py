import time
import math
from threading import Thread
from multiprocessing import Process, Manager, cpu_count

# -------------------------------
# Check if number is prime
# -------------------------------
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


# -------------------------------
# Sequential Method
# -------------------------------
def find_primes_sequential(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# -------------------------------
# Threading Method (Concurrency)
# -------------------------------
def worker_thread(start, end, result):
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    result.extend(local_primes)


def find_primes_threading(start, end, num_threads=4):
    threads = []
    result = []

    chunk = (end - start) // num_threads

    for i in range(num_threads):
        s = start + i * chunk
        e = start + (i + 1) * chunk if i != num_threads - 1 else end

        t = Thread(target=worker_thread, args=(s, e, result))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return result


# -------------------------------
# Multiprocessing Method (Parallelism)
# -------------------------------
def worker_process(start, end, result):
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    result += local_primes


def find_primes_multiprocessing(start, end):
    processes = []
    manager = Manager()
    result = manager.list()

    num_processes = cpu_count()
    chunk = (end - start) // num_processes

    for i in range(num_processes):
        s = start + i * chunk
        e = start + (i + 1) * chunk if i != num_processes - 1 else end

        p = Process(target=worker_process, args=(s, e, result))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return list(result)


# -------------------------------
# MAIN PROGRAM
# -------------------------------
def main():
    print("=== PRIME NUMBER FINDER ===")

    # User input
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    print("\nProcessing...\n")

    # Sequential
    t1 = time.time()
    primes_seq = find_primes_sequential(start, end)
    t2 = time.time()

    # Threading
    t3 = time.time()
    primes_thread = find_primes_threading(start, end)
    t4 = time.time()

    # Multiprocessing
    t5 = time.time()
    primes_proc = find_primes_multiprocessing(start, end)
    t6 = time.time()

    # Output
    print("Range:", start, "to", end)
    print("-" * 50)

    print(f"Sequential Time: {t2 - t1:.4f} seconds")
    print(f"Threading Time: {t4 - t3:.4f} seconds")
    print(f"Multiprocessing Time: {t6 - t5:.4f} seconds")

    print("-" * 50)
    print("Total Prime Numbers:", len(primes_seq))

    print("\nList of Prime Numbers:")
    print(primes_seq)


# Run program
if __name__ == "__main__":
    main()