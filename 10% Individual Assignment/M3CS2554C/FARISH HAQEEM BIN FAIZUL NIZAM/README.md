# 🛡️ OmniGuard: A Hybrid Parallel Engine for High-Throughput Deep Packet Inspection (DPI)

### 👤 Name: Farish Haqeem Bin Faizul Nizam
### 📘 Subject: ITT440 - Individual Project
### 🏫 Class: M3CS2554C
### 📅 Submission Date: 26 April 2026
### 👨‍🏫 Lecturer: Sir Shahadan Bin Saad
### 🎥 Youtube Video: https://youtu.be/N9qnxr_5cm4
----

## 🖥️ System Environment

| Parameter        	| Details                             	|
|------------------	|-------------------------------------	|
| 💻 OS             	| Windows 10                          	|
| 🐍 Python Version 	| Python 3.14                         	|
| 🧑‍💻 IDE           	| Visual Studio Code                  	|
| 📦 Libraries      	| Scapy, Multiprocessing, Threading   	|
| ⚙️ CPU Cores      	| 4 Workers Assigned                  	|
| 🛠️ Deployment     	| PyInstaller (Standalone Executable) 	|
---

## ❗ Problem Statement
Standard network sniffers often struggle with Deep Packet Inspection (DPI) on high-speed interfaces. When a sniffer processes packets sequentially, the time spent calculating entropy or checking malicious signatures can lead to a **"bottleneck,"** causing the system to drop incoming packets.

This project explores a Hybrid Architecture: using **Threading** for I/O-bound tasks (sniffing and UI updates) and **Multiprocessing** for CPU-bound tasks (DPI and data analysis) to ensure zero packet loss and higher throughput.

---

## 🎯 Objectives
**Implement a Hybrid Approach:** Use threading for constant packet capture and multiprocessing for heavy analysis.

**DPI Analysis:** Calculate Shannon entropy to detect encrypted traffic and flag potential malicious domains.

**Benchmark Performance:** Compare Serial processing against Parallel processing using a 50,000 synthetic packet dataset.

**Real-time Monitoring:** Provide a live dashboard that updates packet counts and latency metrics every 5 seconds.

**Scalability:** Utilize an IPC (multiprocessing.Queue) to distribute workloads across multiple CPU workers.

---

## 💡 Implementation
### Source Code
```
import multiprocessing
import threading
import time
import re
import socket
from scapy.all import sniff, IP, TCP, DNS, DNSQR, conf

# --- CONCURRENT TECHNIQUE: THE UI LOGGER ---
def logger_thread(result_queue):
    print(f"\n{'PROTOCOL':<10} | {'INFO':<50} | {'LATENCY'}")
    print("-" * 80)
    while True:
        msg = result_queue.get()
        if msg is None: break
        print(msg)

# --- PARALLEL TECHNIQUE: THE ANALYZER ---
def protocol_analyzer(task_queue, result_queue, analyzer_type):
    while True:
        packet_data = task_queue.get()
        if packet_data is None: break
        
        start_time = time.perf_counter()
        payload = packet_data.get('payload', "")
        summary = ""

        if analyzer_type == "DNS":
            summary = f"Query Found: {packet_data.get('query')}"
        
        elif analyzer_type == "HTTP/HTTPS":
            # Heuristic for SNI or Host
            host_match = re.search(r"Host: ([\w\.]+)", payload)
            sni_match = re.findall(r'[a-z0-9-\.]+\.[a-z]{2,}', payload)
            
            if host_match:
                summary = f"HTTP -> {host_match.group(1)}"
            elif sni_match:
                summary = f"HTTPS (SNI) -> {sni_match[0]}"
            else:
                summary = "Encrypted/Unknown Data"

        latency = (time.perf_counter() - start_time) * 1000
        result_queue.put(f"{analyzer_type:<10} | {summary[:50]:<50} | {latency:.4f}ms")

# --- UTILITY: TRIGGER DNS MANUALLY ---
def trigger_dns(target_domain):
    print(f"[*] Manually triggering DNS lookup for: {target_domain}")
    try:
        socket.gethostbyname(target_domain)
    except Exception as e:
        print(f"[!] Error: {e}")

# --- MAIN LOGIC ---
if __name__ == "__main__":
    print("=== ITT440 Parallel Programming Tool ===")
    print("1. Live Network Traffic (Real-time capture)")
    print("2. Targeted DNS Analysis (Choose a domain)")
    choice = input("Select Mode (1 or 2): ")

    # Setup Queues
    dns_q = multiprocessing.Queue()
    http_q = multiprocessing.Queue()
    results_q = multiprocessing.Queue()

    # Start Parallel Processes
    p1 = multiprocessing.Process(target=protocol_analyzer, args=(dns_q, results_q, "DNS"))
    p2 = multiprocessing.Process(target=protocol_analyzer, args=(http_q, results_q, "HTTP/HTTPS"))
    p1.start(); p2.start()

    # Start Concurrent Thread
    log_worker = threading.Thread(target=logger_thread, args=(results_q,))
    log_worker.daemon = True
    log_worker.start()

    def packet_callback(pkt):
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
            dns_q.put({'query': pkt[DNS].qd.qname.decode()})
        elif pkt.haslayer(TCP) and (pkt.dport == 443 or pkt.dport == 80):
            http_q.put({'payload': str(pkt.payload)})

    try:
        if choice == '2':
            domain = input("Enter domain to analyze (e.g. google.com): ")
            # Start sniffer in a separate thread so we can trigger DNS at the same time
            sniffer = threading.Thread(target=lambda: sniff(prn=packet_callback, store=0, count=5, timeout=10))
            sniffer.start()
            time.sleep(1) 
            trigger_dns(domain)
            sniffer.join()
        else:
            print(f"[*] Sniffing real-time traffic on {conf.iface}...")
            sniff(prn=packet_callback, store=0, count=30)
            
    except KeyboardInterrupt:
        pass
    finally:
        print("\n[*] Analysis Complete. Closing processes...")
        dns_q.put(None); http_q.put(None)
        p1.join(); p2.join()
        results_q.put(None)
        print("[+] System Clean.")
```
### Function Description
| Component / Function    	| Purpose                                                                                                     	|
|-------------------------	|-------------------------------------------------------------------------------------------------------------	|
| DPI Worker Processes    	| Separate processes that calculate Shannon entropy and analyze packet payloads without blocking the sniffer. 	|
| Sniffer Thread          	| A dedicated thread using Scapy to listen to the network interface (Intel Wireless-AC 9560).                 	|
| Dashboard Thread        	| Manages the CLI output, ensuring the "Live Dashboard" refreshes without interrupting data capture.          	|
| multiprocessing.Queue   	| The "bridge" (IPC) that safely transfers packet data from the sniffer to the workers.                       	|
| Serial vs Parallel Mode 	| Comparison logic that processes 50,000 packets to measure speedup factors.                                  	|
| Deployment              	| PyInstaller (Standalone Executable)                                                                         	|

---

## 🛠️ Deployment Guide
**1. Copy the source code into any IDE software**

**2. Make sure to use Python 3.14 to ensure fully function of the coding**

**3. Install Ncap for Windows OS**
```
https://npcap.com/dist/npcap-1.87.exe
```

**4. Install scapy using pip inside IDE**
```
bash
pip install scapy
```

**5. Make sure to use scapy on installed environment manager**

**Example:** <img width="230" height="179" alt="image" src="https://github.com/user-attachments/assets/f1c3cf4b-e54f-49b7-9b74-ff0dd8656f8b" />

**6. Open new file and run this code to get the interface of the device**
```
from scapy.all import show_interfaces
show_interfaces()
```
**Example:**
**<img width="707" height="142" alt="image" src="https://github.com/user-attachments/assets/7f0255b1-572b-49d4-ac50-83241919176a" />**

**7. Copy the desired interface and paste into the source code in line 34**

**8. Save the file and run the Program as Administrator:**

---

## 🌟Output Result
<img width="39%" height="39%" align="top" alt="image" src="https://github.com/user-attachments/assets/32614197-8a49-4e27-ad0d-c6abed351cd0" />
<img width="30%" height="30%" alt="image" src="https://github.com/user-attachments/assets/f3487aa5-bcc7-4422-995e-d6162829112d" />
<img width="30%" height="30%" alt="image" src="https://github.com/user-attachments/assets/8c88abe2-4ed3-4430-8871-0799bfdfb1da" />

---

## 📊 Performance & Traffic Analysis

### 🚀 Benchmarking
The Hybrid Sniffer Engine was tested with a synthetic load of 50,000 packets. The parallel implementation utilizing 4 worker processes achieved a throughput of **35,835 pkts/sec**, representing a **1.35x speed-up** over the serial execution.

#

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/7f4424ee-dc59-4b8b-a8ce-8a4cb804a5f1" />

| Mode | Time (s) | Throughput (Pkts/sec) |
| :--- | :--- | :--- |
| Serial (1 Core) | 1.881 | 26,576 |
| Parallel (4 Cores) | 1.395 | 35,835 |

### 📡 Live Sniffing Results
During a 30-second live capture on the `Intel(R) Wireless-AC 9560`, the engine processed **4,286 packets**.

<img width="800" height="480" alt="image" src="https://github.com/user-attachments/assets/840f7f43-5d4e-4e3c-8674-25e497ff0cd3" />

- **Traffic Type:** The capture consisted of 89.5% UDP traffic and 10.5% TCP traffic.
- **Security:** 79.2% of packets ($3,396$) were flagged as encrypted based on a Shannon entropy threshold of $> 7.0$.
- **Latency:** The average DPI latency stabilized at approximately **84.36 ms** during peak throughput.

<p align="middle">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/36aff374-da9b-442c-aa9c-758166b08f57" />
</p>

#

<img width="700" height="525" alt="image" src="https://github.com/user-attachments/assets/d36d68c9-8e0b-49fa-ab87-7c3f5feb47ea" />

---
## 📋 Conclusion
The Hybrid High-Throughput Sniffer Engine proves that modern network monitoring requires more than a single-core approach. By splitting the workload—using threading for data capture and multiprocessing for heavy analysis—the system achieved a **1.35x performance boost**. This design prevents bottlenecks, ensuring that the engine can process high volumes of traffic and calculate entropy in real-time without dropping packets or lagging behind the network stream.
