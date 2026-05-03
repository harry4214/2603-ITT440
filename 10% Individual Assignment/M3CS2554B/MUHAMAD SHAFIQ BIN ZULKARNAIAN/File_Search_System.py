#!/usr/bin/env python3
"""
Parallel File Search System with GUI
- Generate thousands of random text files
- Search using sequential, threaded (concurrent), and multiprocessing (parallel) strategies
- Display results and performance metrics
"""

import os
import re
import random
import string
import time
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from typing import List, Tuple, Dict, Optional

# ------------------------------------------------------------
# Utility: Generate random text files
# ------------------------------------------------------------
def generate_random_files(directory: Path, count: int, avg_lines: int = 100, avg_words_per_line: int = 10):
    """Generate 'count' random text files in 'directory'."""
    directory.mkdir(parents=True, exist_ok=True)
    # Common words to make searches meaningful
    common_words = ["apple", "banana", "cherry", "dog", "cat", "mouse", "computer", "python",
                    "parallel", "thread", "process", "search", "file", "data", "result", "error",
                    "success", "performance", "speed", "fast", "slow", "benchmark", "unique"]
    
    for i in range(1, count + 1):
        file_path = directory / f"random_file_{i:05d}.txt"
        num_lines = random.randint(avg_lines // 2, avg_lines * 2)
        with open(file_path, 'w', encoding='utf-8') as f:
            for _ in range(num_lines):
                # Generate line with random words
                num_words = random.randint(avg_words_per_line // 2, avg_words_per_line * 2)
                line_words = [random.choice(common_words) for _ in range(num_words)]
                # Occasionally inject a special pattern for demonstration
                if random.random() < 0.05:   # 5% of lines contain "SPECIAL_PATTERN"
                    line_words.append("SPECIAL_PATTERN")
                f.write(" ".join(line_words) + "\n")
    return count

# ------------------------------------------------------------
# Core search function (used by all strategies)
# ------------------------------------------------------------
def search_in_file(file_path: Path, pattern: str, use_regex: bool = False) -> Tuple[Path, List[Tuple[int, str]]]:
    """
    Search a single file for pattern.
    Returns (file_path, list_of_(line_number, line_content)).
    """
    matches = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            if use_regex:
                regex = re.compile(pattern)
                for line_no, line in enumerate(f, start=1):
                    if regex.search(line):
                        matches.append((line_no, line.rstrip()))
            else:
                for line_no, line in enumerate(f, start=1):
                    if pattern in line:
                        matches.append((line_no, line.rstrip()))
    except (IOError, OSError) as e:
        matches.append((0, f"ERROR: {e}"))
    return file_path, matches

# ------------------------------------------------------------
# Search strategies
# ------------------------------------------------------------
def sequential_search(files: List[Path], pattern: str, use_regex: bool = False, progress_callback=None) -> Dict[Path, List]:
    results = {}
    total = len(files)
    for idx, f in enumerate(files):
        if progress_callback:
            progress_callback(idx + 1, total)
        path, matches = search_in_file(f, pattern, use_regex)
        if matches:
            results[path] = matches
    return results

def threaded_search(files: List[Path], pattern: str, use_regex: bool = False, max_workers: int = None, progress_callback=None) -> Dict[Path, List]:
    results = {}
    total = len(files)
    completed = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {executor.submit(search_in_file, f, pattern, use_regex): f for f in files}
        for future in as_completed(future_to_file):
            completed += 1
            if progress_callback:
                progress_callback(completed, total)
            path, matches = future.result()
            if matches:
                results[path] = matches
    return results

def parallel_search(files: List[Path], pattern: str, use_regex: bool = False, max_workers: int = None, progress_callback=None) -> Dict[Path, List]:
    results = {}
    total = len(files)
    completed = 0
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {executor.submit(search_in_file, f, pattern, use_regex): f for f in files}
        for future in as_completed(future_to_file):
            completed += 1
            if progress_callback:
                progress_callback(completed, total)
            path, matches = future.result()
            if matches:
                results[path] = matches
    return results

# ------------------------------------------------------------
# GUI Application
# ------------------------------------------------------------
class ParallelSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Parallel File Search System")
        self.root.geometry("900x700")
        
        self.directory = tk.StringVar()
        self.pattern = tk.StringVar()
        self.use_regex = tk.BooleanVar()
        self.num_files_to_generate = tk.IntVar(value=20000)
        
        self.search_strategies = {
            "Sequential": sequential_search,
            "Threaded (Concurrent)": threaded_search,
            "Process-based (Parallel)": parallel_search
        }
        self.selected_strategies = {name: tk.BooleanVar(value=True) for name in self.search_strategies}
        
        self.build_ui()
        
    def build_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # ----- File generation section -----
        gen_frame = ttk.LabelFrame(main_frame, text="Generate Test Files", padding="5")
        gen_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(gen_frame, text="Directory:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Entry(gen_frame, textvariable=self.directory, width=50).grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(gen_frame, text="Browse", command=self.browse_directory).grid(row=0, column=2, padx=5)
        
        ttk.Label(gen_frame, text="Number of files:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Spinbox(gen_frame, from_=100, to=30000, textvariable=self.num_files_to_generate, width=15).grid(row=1, column=1, sticky=tk.W, padx=5)
        ttk.Button(gen_frame, text="Generate Files", command=self.generate_files_thread).grid(row=1, column=2, padx=5)
        
        # Progress for generation
        self.gen_progress = ttk.Progressbar(gen_frame, mode='determinate')
        self.gen_progress.grid(row=2, column=0, columnspan=3, sticky=tk.EW, padx=5, pady=5)
        
        # ----- Search section -----
        search_frame = ttk.LabelFrame(main_frame, text="Search Configuration", padding="5")
        search_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(search_frame, text="Search pattern:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Entry(search_frame, textvariable=self.pattern, width=40).grid(row=0, column=1, padx=5, pady=2)
        ttk.Checkbutton(search_frame, text="Use regular expression", variable=self.use_regex).grid(row=0, column=2, padx=5)
        
        # Strategies selection
        ttk.Label(search_frame, text="Strategies:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        strat_frame = ttk.Frame(search_frame)
        strat_frame.grid(row=1, column=1, columnspan=2, sticky=tk.W)
        col = 0
        for name in self.search_strategies:
            ttk.Checkbutton(strat_frame, text=name, variable=self.selected_strategies[name]).grid(row=0, column=col, padx=10)
            col += 1
        
        ttk.Button(search_frame, text="Run Search", command=self.run_search_thread).grid(row=2, column=0, columnspan=3, pady=10)
        
        # Progress bar for search
        self.search_progress = ttk.Progressbar(search_frame, mode='determinate')
        self.search_progress.grid(row=3, column=0, columnspan=3, sticky=tk.EW, padx=5, pady=5)
        self.progress_label = ttk.Label(search_frame, text="")
        self.progress_label.grid(row=4, column=0, columnspan=3)
        
        # ----- Results display -----
        result_frame = ttk.LabelFrame(main_frame, text="Search Results & Performance", padding="5")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.result_text = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, width=100, height=20)
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Add a clear button
        ttk.Button(result_frame, text="Clear Results", command=self.clear_results).pack(pady=5)
        
    def browse_directory(self):
        dir_selected = filedialog.askdirectory()
        if dir_selected:
            self.directory.set(dir_selected)
    
    def clear_results(self):
        self.result_text.delete(1.0, tk.END)
    
    def log_message(self, msg):
        self.result_text.insert(tk.END, msg + "\n")
        self.result_text.see(tk.END)
        self.root.update_idletasks()
    
    def generate_files_thread(self):
        if not self.directory.get():
            messagebox.showerror("Error", "Please select a directory.")
            return
        thread = threading.Thread(target=self.generate_files, daemon=True)
        thread.start()
    
    def generate_files(self):
        try:
            count = self.num_files_to_generate.get()
            if count <= 0:
                raise ValueError
            dir_path = Path(self.directory.get())
            self.log_message(f"Generating {count} random files in {dir_path}...")
            self.gen_progress['maximum'] = count
            # We'll simulate progress by using a callback inside generate_random_files? 
            # For simplicity, we generate all then show progress as done.
            # But to show real progress, we'd need to modify generate_random_files.
            # Let's implement a simple progress update:
            dir_path.mkdir(parents=True, exist_ok=True)
            common_words = ["apple", "banana", "cherry", "dog", "cat", "mouse", "computer", "python",
                            "parallel", "thread", "process", "search", "file", "data", "result", "error",
                            "success", "performance", "speed", "fast", "slow", "benchmark", "unique",
                            "SPECIAL_PATTERN", "Network"]
            for i in range(1, count + 1):
                file_path = dir_path / f"random_file_{i:05d}.txt"
                num_lines = random.randint(50, 150)
                with open(file_path, 'w', encoding='utf-8') as f:
                    for _ in range(num_lines):
                        num_words = random.randint(5, 15)
                        line_words = [random.choice(common_words) for _ in range(num_words)]
                        f.write(" ".join(line_words) + "\n")
                self.gen_progress['value'] = i
                self.root.update_idletasks()
            self.log_message(f"Successfully generated {count} files.")
            self.gen_progress['value'] = 0
        except Exception as e:
            messagebox.showerror("Generation Error", str(e))
    
    def run_search_thread(self):
        # Validate
        if not self.directory.get():
            messagebox.showerror("Error", "Please select a directory containing files.")
            return
        if not self.pattern.get():
            messagebox.showerror("Error", "Please enter a search pattern.")
            return
        selected = [name for name, var in self.selected_strategies.items() if var.get()]
        if not selected:
            messagebox.showerror("Error", "Please select at least one search strategy.")
            return
        
        # Collect files
        dir_path = Path(self.directory.get())
        if not dir_path.is_dir():
            messagebox.showerror("Error", "Directory does not exist.")
            return
        files = list(dir_path.glob("*.txt"))
        if not files:
            messagebox.showerror("Error", f"No .txt files found in {dir_path}.")
            return
        
        self.log_message(f"\n{'='*60}")
        self.log_message(f"Searching {len(files)} files for pattern: '{self.pattern.get()}'")
        self.log_message(f"Regex: {self.use_regex.get()}")
        self.log_message(f"Selected strategies: {', '.join(selected)}")
        self.log_message(f"{'='*60}\n")
        
        # Run each selected strategy sequentially (to avoid resource conflict)
        baseline_time = None
        results = {}
        
        for strategy_name in selected:
            self.log_message(f"\n--- Running {strategy_name} ---")
            self.search_progress['value'] = 0
            self.progress_label.config(text=f"{strategy_name} in progress...")
            self.root.update_idletasks()
            
            strategy_func = self.search_strategies[strategy_name]
            start = time.perf_counter()
            
            # Run the strategy with progress callback
            if strategy_name == "Sequential":
                result_dict = strategy_func(files, self.pattern.get(), self.use_regex.get(),
                                            progress_callback=lambda curr, total: self.update_search_progress(curr, total))
            else:
                # Use max_workers = CPU count for simplicity
                import multiprocessing
                max_workers = multiprocessing.cpu_count()
                result_dict = strategy_func(files, self.pattern.get(), self.use_regex.get(),
                                            max_workers=max_workers,
                                            progress_callback=lambda curr, total: self.update_search_progress(curr, total))
            elapsed = time.perf_counter() - start
            results[strategy_name] = (elapsed, result_dict)
            
            self.log_message(f"Time: {elapsed:.3f} seconds")
            self.log_message(f"Files with matches: {len(result_dict)}")
            
            if strategy_name == "Sequential":
                baseline_time = elapsed
        
        # Show speedups
        if baseline_time:
            self.log_message("\n--- Speedup vs Sequential ---")
            for name, (t, _) in results.items():
                if name != "Sequential":
                    speedup = baseline_time / t
                    self.log_message(f"{name:25} speedup = {speedup:.2f}x")
        
        # Optionally display some matching lines (first 20)
        self.log_message("\n--- Sample Matches (first 20 lines) ---")
        shown = 0
        for strategy_name, (_, result_dict) in results.items():
            if shown >= 20:
                break
            self.log_message(f"\n[{strategy_name}]")
            for file_path, matches in list(result_dict.items())[:5]:  # limit files
                if shown >= 20:
                    break
                self.log_message(f"  {file_path.name}:")
                for line_no, line in matches[:3]:
                    self.log_message(f"    Line {line_no}: {line[:80]}")
                    shown += 1
                    if shown >= 20:
                        break
        self.search_progress['value'] = 0
        self.progress_label.config(text="")
    
    def update_search_progress(self, current, total):
        self.search_progress['maximum'] = total
        self.search_progress['value'] = current
        self.progress_label.config(text=f"Processed {current}/{total} files")
        self.root.update_idletasks()

# ------------------------------------------------------------
# Main entry point
# ------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ParallelSearchApp(root)
    root.mainloop()
