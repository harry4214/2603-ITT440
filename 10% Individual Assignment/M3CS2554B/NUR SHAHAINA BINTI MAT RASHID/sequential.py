import time
from password import task

def run_sequential(n):
    result = []
    start = time.time()

    for i in range(n):
        item = task(i)
        result.append(item)

    end = time.time()
    return result, end - start