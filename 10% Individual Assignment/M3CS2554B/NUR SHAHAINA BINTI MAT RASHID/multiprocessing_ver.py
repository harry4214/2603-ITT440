import time
import os
from multiprocessing import Pool, cpu_count
from password import generate_password, check_strength


def process_task(i):
    password = generate_password()
    strength = check_strength(password)
    process_id = os.getpid()
    return (i + 1, password, strength, process_id)


def run_multiprocessing(n):
    start = time.time()

    with Pool(processes=4) as pool:
        result = pool.map(process_task, range(n))

    end = time.time()
    return result, end - start