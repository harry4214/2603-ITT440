import time
import csv
import random
import tkinter as tk
from tkinter import ttk, messagebox
import multiprocessing
from multiprocessing import Pool, cpu_count
from threading import Thread
import os
import sys

# -------------------------------
# DATA LOGIC
# -------------------------------

def load_answer_scheme():
    answers = []
    with open("answer_scheme.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            answers.append(row["Answer"])
    return answers

def generate_answer(correct, level):
    options = ['A', 'B', 'C', 'D']
    result = []

    for c in correct:
        if level == "high":
            result.append(c if random.random() < 0.8 else random.choice(options))
        elif level == "medium":
            result.append(c if random.random() < 0.5 else random.choice(options))
        else:
            result.append(c if random.random() < 0.2 else random.choice(options))

    return result

def generate_students(n, correct):
    first = ["Ali","Aina","Hafiz","Siti","Daniel","Amir","Nadia","Farah","Irfan","Lina",
             "Hakim","Aisyah","Zul","Faiz","Rashid","Nabil","Syafiq","Azim","Izzat","Arif"]

    last = ["Ahmad","Rahman","Hassan","Ismail","Yusof","Razak","Hamid","Karim",
            "Salleh","Jamal","Aziz","Mahmud","Noor","Kadir","Samad"]

    students = []

    for i in range(n):
        name = f"{random.choice(first)} {random.choice(last)}_{i+1}"
        sid = f"2026{100000+i}"

        level = random.choices(["high","medium","low"], weights=[0.2,0.5,0.3])[0]
        ans = generate_answer(correct, level)

        students.append((name, sid, ans))

    return students

# -------------------------------
# MARKING
# -------------------------------

def mark(ans, correct):
    return sum(1 for i in range(len(correct)) if ans[i] == correct[i])

# 🔥 FIXED HEAVY MODE (NO SCORE CHANGE)
def mark_heavy(ans, correct):
    score = 0
    for i in range(len(correct)):
        if ans[i] == correct[i]:
            score += 1

        # heavy computation (does NOT affect score)
        dummy = 0
        for _ in range(300):
            dummy += (i * i) % 7

    return score

# -------------------------------
# PROCESSING METHODS
# -------------------------------

def run_sequential(students, correct, mode):
    func = mark_heavy if mode == "heavy" else mark
    return [(n, s, func(a, correct)) for n, s, a in students]

def thread_worker(students, results, start, end, correct, mode):
    func = mark_heavy if mode == "heavy" else mark
    for i in range(start, end):
        n, s, a = students[i]
        results[i] = (n, s, func(a, correct))

def run_threading(students, correct, mode):
    results = [None] * len(students)
    threads = []
    chunk = len(students) // 4

    for i in range(4):
        start = i * chunk
        end = len(students) if i == 3 else (i + 1) * chunk
        t = Thread(target=thread_worker,
                   args=(students, results, start, end, correct, mode))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return results

def evaluate_chunk(data):
    chunk, correct, mode = data
    func = mark_heavy if mode == "heavy" else mark
    return [(n, s, func(a, correct)) for n, s, a in chunk]

def run_multiprocessing(students, correct, mode):
    processes = min(4, cpu_count())

    chunk_size = len(students) // processes
    chunks = []

    for i in range(processes):
        start = i * chunk_size
        end = len(students) if i == processes - 1 else (i + 1) * chunk_size
        chunks.append((students[start:end], correct, mode))

    with Pool(processes=processes) as pool:
        results = pool.map(evaluate_chunk, chunks)

    final = []
    for r in results:
        final.extend(r)

    return final

# -------------------------------
# SAVE CSV
# -------------------------------

def save_results(results):
    filename = "final_results.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Rank","Name","StudentID","Score"])
        for i, r in enumerate(results, start=1):
            writer.writerow((i,) + r)
    return filename

# -------------------------------
# GUI
# -------------------------------

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Evaluation System")
        self.root.geometry("1000x720")
        self.root.configure(bg="#1e1e2f")

        self.results = []
        self.mode = tk.StringVar(value="normal")

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="PARALLEL QUIZ EVALUATION SYSTEM",
                 font=("Arial", 20, "bold"),
                 bg="#1e1e2f", fg="white").pack(pady=15)

        btn_frame = tk.Frame(self.root, bg="#1e1e2f")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="RUN SYSTEM", bg="#00c853", fg="white",
                  padx=20, pady=10, command=self.run_thread).grid(row=0, column=0, padx=10)

        tk.Button(btn_frame, text="EXPORT CSV", bg="#2962ff", fg="white",
                  padx=20, pady=10, command=self.export).grid(row=0, column=1, padx=10)

        tk.Button(btn_frame, text="CLEAR", bg="#d50000", fg="white",
                  padx=20, pady=10, command=self.clear).grid(row=0, column=2, padx=10)

        tk.Radiobutton(self.root, text="Normal Mode",
                       variable=self.mode, value="normal",
                       bg="#1e1e2f", fg="white").pack()

        tk.Radiobutton(self.root, text="Heavy Mode (Demo)",
                       variable=self.mode, value="heavy",
                       bg="#1e1e2f", fg="white").pack()

        self.progress = ttk.Progressbar(self.root, length=500, mode="indeterminate")
        self.progress.pack(pady=10)

        columns = ("Rank","Name","StudentID","Score")
        self.tree = ttk.Treeview(self.root, columns=columns,
                                 show="headings", height=10)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")

        self.tree.pack(pady=10)

        self.output = tk.Text(self.root, height=12, width=110,
                              bg="#2b2b3d", fg="white")
        self.output.pack(pady=10)

    def clear(self):
        self.output.delete("1.0", tk.END)
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.results = []
        self.progress.stop()

    def run_thread(self):
        Thread(target=self.run).start()

    def run(self):
        self.progress.start()
        self.output.delete("1.0", tk.END)

        correct = load_answer_scheme()

        # balanced size
        students = generate_students(80000 if self.mode.get()=="heavy" else 200000, correct)

        mode = self.mode.get()

        start = time.time()
        run_sequential(students, correct, mode)
        t1 = time.time() - start

        start = time.time()
        run_threading(students, correct, mode)
        t2 = time.time() - start

        start = time.time()
        self.results = run_multiprocessing(students, correct, mode)
        t3 = time.time() - start

        self.progress.stop()

        avg = sum(s for _,_,s in self.results)/len(self.results)
        sorted_r = sorted(self.results, key=lambda x: x[2], reverse=True)

        pass_mark = 10
        pass_count = sum(1 for _,_,s in self.results if s >= pass_mark)
        fail_count = len(self.results) - pass_count

        for i in self.tree.get_children():
            self.tree.delete(i)

        for i in range(10):
            self.tree.insert("", "end", values=(i+1, *sorted_r[i]))

        self.output.insert(tk.END, "QUIZ SYSTEM PERFORMANCE REPORT\n\n")
        self.output.insert(tk.END, f"Total Students: {len(students)}\n\n")

        self.output.insert(tk.END, "--- EXECUTION TIME ---\n")
        self.output.insert(tk.END, f"Sequential: {t1:.4f}s\n")
        self.output.insert(tk.END, f"Threading: {t2:.4f}s\n")
        self.output.insert(tk.END, f"Multiprocessing: {t3:.4f}s\n\n")

        self.output.insert(tk.END, f"Average Student Quiz Score: {avg:.2f}\n\n")
        self.output.insert(tk.END, f"PASS: {pass_count}\nFAIL: {fail_count}\n")

    def export(self):
        if not self.results:
            messagebox.showwarning("Warning", "No data to export!")
            return

        sorted_r = sorted(self.results, key=lambda x: x[2], reverse=True)
        filename = save_results(sorted_r)

        try:
            if sys.platform == "win32":
                os.startfile(filename)
        except:
            pass

        self.output.insert(tk.END, f"\nOpened: {filename}\n")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
