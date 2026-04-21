import time
import threading
from concurrent.futures import ThreadPoolExecutor
from password import generate_password, check_strength


def thread_task(i):
    password = generate_password()
    strength = check_strength(password)
    thread_name = threading.current_thread().name
    return (i + 1, password, strength, thread_name)


def run_threading(n):
    start = time.time()

    with ThreadPoolExecutor(max_workers=4) as executor:
        result = list(executor.map(thread_task, range(n)))

    end = time.time()
    return result, end - start