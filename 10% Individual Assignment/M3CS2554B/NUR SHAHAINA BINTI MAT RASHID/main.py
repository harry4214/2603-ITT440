from sequential import run_sequential
from threading_ver import run_threading
from multiprocessing_ver import run_multiprocessing


def print_summary(results, mode_name):
    weak = 0
    medium = 0
    strong = 0

    for item in results:
        strength = item[2]
        if strength == "Weak":
            weak += 1
        elif strength == "Medium":
            medium += 1
        else:
            strong += 1

    print(f"\n{mode_name} Summary:")
    print("Weak   :", weak)
    print("Medium :", medium)
    print("Strong :", strong)


def main():
    print("=" * 45)
    print(" SIMPLE PARALLEL PASSWORD GENERATOR ")
    print("=" * 45)

    n = int(input("Enter number of passwords: "))

    print("\n[1] SEQUENTIAL MODE")
    seq_res, seq_time = run_sequential(n)
    for item in seq_res[:7]:
        task_num, password, strength = item
        print(f"Task {task_num} -> Password: {password} | Strength: {strength}")
    print_summary(seq_res, "Sequential")

    print("\n[2] THREADING MODE")
    th_res, th_time = run_threading(n)
    for item in th_res[:7]:
        task_num, password, strength, thread_name = item
        print(f"[{thread_name}] Task {task_num} -> Password: {password} | Strength: {strength}")
    print_summary(th_res, "Threading")

    print("\n[3] MULTIPROCESSING MODE")
    mp_res, mp_time = run_multiprocessing(n)
    for item in mp_res[:7]:
        task_num, password, strength, process_id = item
        print(f"[PID {process_id}] Task {task_num} -> Password: {password} | Strength: {strength}")
    print_summary(mp_res, "Multiprocessing")

    print("\n" + "=" * 45)
    print(" TIME COMPARISON ")
    print("=" * 45)
    print(f"Sequential      : {seq_time:.6f} seconds")
    print(f"Threading       : {th_time:.6f} seconds")
    print(f"Multiprocessing : {mp_time:.6f} seconds")


if __name__ == "__main__":
    main()