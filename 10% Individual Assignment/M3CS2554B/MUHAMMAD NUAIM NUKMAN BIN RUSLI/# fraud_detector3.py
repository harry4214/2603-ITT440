# fraud_detector.py
# Parallel Bank Transaction Fraud Detector
# Concurrent technique  : asyncio
# Parallel technique    : multiprocessing
# Total transactions    : 10,000,000

import asyncio
import time
import multiprocessing
import random

# ============================================================
# CONFIGURATION
# ============================================================
NUM_BRANCHES        = 100
TRANSACTIONS_EACH   = 100_000
TOTAL_TRANSACTIONS  = NUM_BRANCHES * TRANSACTIONS_EACH  # 10,000,000

LARGE_AMOUNT_LIMIT  = 50_000
RAPID_TX_LIMIT      = 5

# FIX 1: Fixed seed so BLACKLISTED_IDS is the same in every process
random.seed(42)
BLACKLISTED_IDS     = {f"ACC{random.randint(1000,9999)}" for _ in range(50)}

TX_TYPES            = ["TRANSFER", "WITHDRAWAL", "DEPOSIT",
                       "PAYMENT", "REFUND", "PURCHASE"]
BRANCH_NAMES        = [f"Branch_{i+1:03d}" for i in range(NUM_BRANCHES)]

# ============================================================
# GENERATE DATA
# ============================================================
def generate_transaction(i, seed):
    random.seed(seed + i)
    return {
        "id"         : i,
        "account_id" : f"ACC{random.randint(1000, 9999)}",
        "type"       : random.choice(TX_TYPES),
        "amount"     : round(random.uniform(1, 100_000), 2),
        "location"   : random.choice(["Local", "International", "Online"]),
        "consecutive": random.randint(1, 10),
    }

def generate_all_transactions():
    print(f"Generating {TOTAL_TRANSACTIONS:,} raw bank transactions...")
    print("(This might take a moment)")
    start = time.time()
    all_branches = {}
    for idx, branch in enumerate(BRANCH_NAMES):
        seed = idx * 1000
        all_branches[branch] = {
            "branch"      : branch,
            "transactions": [generate_transaction(i, seed)
                             for i in range(TRANSACTIONS_EACH)]
        }
    duration = round(time.time() - start, 2)
    print(f"Data generation complete in {duration} seconds.")
    return all_branches

# ============================================================
# FRAUD DETECTION
# ============================================================
def is_fraud(tx):
    return (
        tx["amount"] > LARGE_AMOUNT_LIMIT or
        tx["consecutive"] > RAPID_TX_LIMIT or
        tx["account_id"] in BLACKLISTED_IDS or
        (tx["location"] == "International" and tx["amount"] > 10_000)
    )

def analyze_branch(branch_data):
    transactions  = branch_data["transactions"]
    fraud_count   = 0
    large_amount  = 0
    rapid_tx      = 0
    blacklisted   = 0
    international = 0
    total_amount  = 0

    for tx in transactions:
        total_amount += tx["amount"]
        # FIX 2: Track each category separately, count fraud once per transaction
        if tx["amount"] > LARGE_AMOUNT_LIMIT:
            large_amount += 1
        if tx["consecutive"] > RAPID_TX_LIMIT:
            rapid_tx += 1
        if tx["account_id"] in BLACKLISTED_IDS:
            blacklisted += 1
        if tx["location"] == "International" and tx["amount"] > 10_000:
            international += 1
        if is_fraud(tx):
            fraud_count += 1  # counted once per transaction, not per rule

    return {
        "branch"       : branch_data["branch"],
        "total_tx"     : len(transactions),
        "fraud_count"  : fraud_count,
        "large_amount" : large_amount,
        "rapid_tx"     : rapid_tx,
        "blacklisted"  : blacklisted,
        "international": international,
        "total_amount" : round(total_amount, 2),
    }

# ============================================================
# APPROACH 1 — Sequential
# ============================================================
def run_sequential(all_data):
    print("=" * 55)
    print("--- TEST A: Sequential Processing ---")
    print("=" * 55)
    print(f"Processing {TOTAL_TRANSACTIONS:,} transactions one by one...")
    start    = time.time()
    branches = list(all_data.values())
    results  = [analyze_branch(b) for b in branches]
    duration = round(time.time() - start, 2)
    print(f"[TEST A COMPLETE] Sequential Time: {duration} seconds")
    return results, duration

# ============================================================
# APPROACH 2 — Concurrent using asyncio
# ============================================================
async def fetch_branch_async(branch_name, all_data):
    await asyncio.sleep(0)
    return analyze_branch(all_data[branch_name])

async def run_concurrent_async(all_data):
    tasks = [fetch_branch_async(b, all_data) for b in BRANCH_NAMES]
    return await asyncio.gather(*tasks)

def run_concurrent(all_data):
    print("=" * 55)
    print("--- TEST B: Concurrent Processing (asyncio) ---")
    print("=" * 55)
    print(f"Processing {TOTAL_TRANSACTIONS:,} transactions concurrently...")
    start    = time.time()
    results  = asyncio.run(run_concurrent_async(all_data))
    duration = round(time.time() - start, 2)
    print(f"[TEST B COMPLETE] Concurrent Time: {duration} seconds")
    return results, duration

# ============================================================
# APPROACH 3 — Parallel using multiprocessing
# ============================================================
def run_parallel(all_data):
    cores = multiprocessing.cpu_count()
    print("=" * 55)
    print("--- TEST C: Parallel Processing (multiprocessing) ---")
    print("=" * 55)
    print(f"Processing {TOTAL_TRANSACTIONS:,} transactions in parallel...")
    print(f"Using {cores} CPU cores simultaneously...")
    start    = time.time()
    branches = list(all_data.values())
    with multiprocessing.Pool(processes=cores) as pool:
        results = pool.map(analyze_branch, branches)
    duration = round(time.time() - start, 2)
    print(f"[TEST C COMPLETE] Parallel Time: {duration} seconds")
    return results, duration

# ============================================================
# SAVE ALL 10,000,000 TRANSACTIONS TO FILE
# ============================================================
def save_results(all_data, results_c, time_a, time_b, time_c):
    speedup_b = round(time_a / time_b, 1) if time_b > 0 else 0
    speedup_c = round(time_a / time_c, 1) if time_c > 0 else 0
    fastest   = "Concurrent" if time_b < time_c else "Parallel"

    total_fraud  = sum(r["fraud_count"]   for r in results_c)
    total_large  = sum(r["large_amount"]  for r in results_c)
    total_rapid  = sum(r["rapid_tx"]      for r in results_c)
    total_black  = sum(r["blacklisted"]   for r in results_c)
    total_intl   = sum(r["international"] for r in results_c)
    total_amount = sum(r["total_amount"]  for r in results_c)

    print(f"\nSaving all {TOTAL_TRANSACTIONS:,} transaction records to file...")
    print("Please wait — this may take a few minutes...")

    with open("fraud_detection_results.txt", "w") as f:

        # Header
        f.write("=" * 55 + "\n")
        f.write("   PARALLEL BANK TRANSACTION FRAUD DETECTOR\n")
        f.write("=" * 55 + "\n\n")

        # Performance report
        f.write("FINAL PERFORMANCE REPORT\n")
        f.write("=" * 55 + "\n")
        f.write(f"  Bank branches           : {NUM_BRANCHES}\n")
        f.write(f"  Transactions per branch : {TRANSACTIONS_EACH:,}\n")
        f.write(f"  Total transactions      : {TOTAL_TRANSACTIONS:,}\n")
        f.write(f"  CPU cores available     : {multiprocessing.cpu_count()}\n\n")
        f.write(f"  Sequential Time         : {time_a}s\n")
        f.write(f"  Concurrent Time         : {time_b}s  ({speedup_b}x faster than sequential)\n")
        f.write(f"  Parallel Time           : {time_c}s  ({speedup_c}x faster than sequential)\n\n")
        f.write(f"  Fastest approach        : {fastest}\n")
        f.write("=" * 55 + "\n\n")

        # Fraud summary
        f.write("FRAUD DETECTION SUMMARY\n")
        f.write("=" * 55 + "\n")
        f.write(f"  Total fraud detected      : {total_fraud:,}\n")
        f.write(f"  Large amount flags        : {total_large:,}\n")
        f.write(f"  Rapid transaction flags   : {total_rapid:,}\n")
        f.write(f"  Blacklisted accounts      : {total_black:,}\n")
        f.write(f"  Suspicious international  : {total_intl:,}\n")
        f.write(f"  Total transaction value   : ${total_amount:,.2f}\n")
        f.write("=" * 55 + "\n\n")

        # All 10,000,000 transactions
        f.write("ALL 10,000,000 TRANSACTION RECORDS\n")
        f.write("=" * 55 + "\n")
        f.write(f"  {'No.':<10} {'Branch':<15} {'Account':<10} "
                f"{'Type':<12} {'Amount':>12} {'Location':<15} {'Fraud':<6}\n")
        f.write(f"  {'-' * 80}\n")

        counter = 1
        # FIX 3: Write in chunks of 10,000 lines for much faster file output
        CHUNK_SIZE = 10_000
        buffer = []
        for branch_name, branch_data in all_data.items():
            for tx in branch_data["transactions"]:
                fraud_flag = "YES" if is_fraud(tx) else "NO"
                buffer.append(
                    f"  {counter:<10} {branch_name:<15} {tx['account_id']:<10} "
                    f"{tx['type']:<12} ${tx['amount']:>11,.2f} "
                    f"{tx['location']:<15} {fraud_flag:<6}\n"
                )
                counter += 1
                if len(buffer) >= CHUNK_SIZE:
                    f.writelines(buffer)
                    buffer = []

            # Show progress every 10 branches
            if int(branch_name.split("_")[1]) % 10 == 0:
                print(f"  Writing... {counter-1:,} / {TOTAL_TRANSACTIONS:,} records done")

        # Flush any remaining lines
        if buffer:
            f.writelines(buffer)

        f.write("\n")
        f.write(f"  Total records written: {counter-1:,}\n")
        f.write("=" * 55 + "\n")

    print(f"Done! All {counter-1:,} records saved to 'fraud_detection_results.txt'")


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print()
    print("=" * 55)
    print("   PARALLEL BANK TRANSACTION FRAUD DETECTOR")
    print("=" * 55)
    print()

    all_data = generate_all_transactions()
    print()

    results_a, time_a = run_sequential(all_data)
    print()
    results_b, time_b = run_concurrent(all_data)
    print()
    results_c, time_c = run_parallel(all_data)
    print()

    # Print to terminal
    speedup_b = round(time_a / time_b, 1) if time_b > 0 else 0
    speedup_c = round(time_a / time_c, 1) if time_c > 0 else 0
    fastest   = "Concurrent" if time_b < time_c else "Parallel"

    print()
    print("=" * 55)
    print("FINAL PERFORMANCE REPORT")
    print("=" * 55)
    print(f"  Bank branches           : {NUM_BRANCHES}")
    print(f"  Transactions per branch : {TRANSACTIONS_EACH:,}")
    print(f"  Total transactions      : {TOTAL_TRANSACTIONS:,}")
    print(f"  CPU cores available     : {multiprocessing.cpu_count()}")
    print()
    print(f"  Sequential Time         : {time_a}s")
    print(f"  Concurrent Time         : {time_b}s  ({speedup_b}x faster than sequential)")
    print(f"  Parallel Time           : {time_c}s  ({speedup_c}x faster than sequential)")
    print()
    print(f"  Fastest approach        : {fastest}")
    print("=" * 55)
    print()

    # Save all 10,000,000 transactions to file
    save_results(all_data, results_c, time_a, time_b, time_c)
    print()
    input("Press any key to continue . . . ")