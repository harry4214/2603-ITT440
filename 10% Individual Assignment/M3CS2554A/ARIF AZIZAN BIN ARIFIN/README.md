# Poker Game Simulator

**Course Code:** ITT440  
**Lecturer:** Shahadan Bin Saad  
**YouTube Demo:** [Watch on YouTube](*youtube URL*)

## Overview

The Poker Game Simulator is a Python-based application designed to simulate poker games, evaluate poker hands, and compare execution performance using sequential, concurrent, and parallel processing techniques. This project combines game logic with performance analysis and is suitable for course work in ITT440.

## Problem Statement

Many card game simulators need to solve two challenges at once:

- Determine the best poker hand accurately from a set of available cards.
- Process large volumes of simulation results efficiently, especially when reading and analyzing log data.

This project tackles both by implementing correct poker hand ranking and then measuring how different computation techniques perform.

## Objective

The main objectives of the Poker Game Simulator are:

- Build a valid poker hand evaluator that ranks hands from High Card to Royal Flush.
- Simulate single games and multiple game runs with random shuffled decks.
- Save simulation results to a log file for later analysis.
- Compare sequential, concurrent, and parallel processing methods.
- Generate a clear report of hand frequencies and processing performance.

## Program Capabilities

The simulator supports:

- Interactive single-game play.
- Multiple-game simulations with log output.
- Automatic dealing of player and dealer cards.
- Best 5-card hand selection from 7 available cards.
- Hand ranking for all standard poker combinations.
- Log file analysis with threading.
- Performance comparison using multiprocessing.

## Techniques Used

- `random.shuffle` for deck randomization.
- `itertools.combinations` to evaluate all 5-card hand combinations from available cards.
- `collections.Counter` for rank counting and frequency analysis.
- `threading` for concurrent log reading.
- `multiprocessing` for parallel analysis across CPU cores.
- `time.perf_counter` for performance timing.
- `tqdm` for progress bars during data processing.

## System Requirements

- Operating System: Windows 10/11, macOS, or Linux
- Python 3.10 or newer
- At least 4 GB RAM recommended for simulation and multiprocessing
- Internet access for downloading Python and packages

## Required Python Package

- `tqdm`

Install it with:

```bash
pip install tqdm
```

## Installation Steps

1. Install Python 3.10+ from https://www.python.org/downloads/
2. Open a terminal or PowerShell window.
3. Navigate to the project folder:

```powershell
cd "C:\Users\ACoralReef\OneDrive\Documents\python code"
```

4. Install the required package:

```powershell
pip install tqdm
```

5. Confirm the main script is present:

- `Poker Simulator.py`
- `poker_simulation.log` (created after the first simulation)

## How to Run the Program

Run the main script using Python:

```powershell
python "Poker Simulator.py"
```

The program will prompt you to choose between:

- `single` — play one game interactively
- `simulations` — run multiple game simulations and analyze results

### Single Game Mode

1. Choose `single` when prompted.
2. Enter the number of players (between 2 and 22).
3. The program deals cards and displays:
   - Your hand
   - Dealer cards
   - Best 5-card hand
   - Poker hand ranking
4. After each game, it asks whether you want to play again.

### Simulations Mode

1. Choose `simulations` when prompted.
2. If `poker_simulation.log` exists, the program asks whether to overwrite it.
3. Enter the number of simulations to run.
4. Enter the number of players (including the user).
5. The program writes results to `poker_simulation.log`.
6. It reads the log file using threading, then analyzes it sequentially and in parallel.
7. Finally, it prints a report comparing execution times and hand frequencies.

## Sample Input / Output

### Sample Input

```text
Do you want to run a single game or run a simulations?
Enter 'single' for single game or 'simulations' for running simulations.
>>> single
[๑╹ᆺ  ╹] Enter number of players.
>>> 4
```

### Sample Output

```text
[๑╹ᆺ  ╹] Your hand: [(11, 'hearts'), (3, 'spades')]
[๑╹ᆺ  ╹] Dealer's cards: [(4, 'clubs'), (5, 'hearts'), (6, 'diamonds'), (7, 'spades'), (9, 'clubs')]
[๑╹ᆺ  ╹] Your best hand: [(3, 'spades'), (4, 'clubs'), (5, 'hearts'), (6, 'diamonds'), (7, 'spades')]
[๑╹ᆺ  ╹] Your poker hand: Straight
```

### Sample Simulation Output

```text
Completed 1000 simulations. Results saved to poker_simulation.log.

[๑╹ᆺ  ╹] Starting concurrent reader for poker_simulation.log...

[๑╹ᆺ  ╹] Starting sequential reading...
[๑╹ᆺ  ╹] Using Sequential Technique...

[๑╹ᆺ  ╹] Starting parallel reading...

[๑╹ᆺ  ╹] Parallel reading completed.

=============================================
 REPORT ON SIMULATION RESULTS AND TECHNIQUES 
=============================================

Poker hand results:
	Royal Flush: 0
	Straight Flush: 1
	Four of a Kind: 12
	Full House: 34
	Flush: 75
	Straight: 112
	Three of a Kind: 226
	Two Pair: 321
	One Pair: 589
	High Card: 630

Performance Comparison:
	Sequential Time: 1.23 seconds
	Parallel Time: 0.77 seconds
	Improvement: 1.60x faster
```

## Screenshots

Add visual screenshots to the repository under a `screenshots/` folder.

Recommended screenshot files:

- `screenshots/single_game_input.png`
- `screenshots/single_game_output.png`
- `screenshots/simulation_run.png`
- `screenshots/performance_report.png`

Embed images in GitHub markdown like this:

```markdown
![Single Game Output](screenshots/single_game_output.png)
```

## Source Code

The main program source file is:

- `Poker Simulator.py`

Important code sections:

- `pokerGame` class — deck creation, dealing, hand evaluation, and best-hand selection
- `runPokerSimulations()` — generates simulation results and writes to the log file
- `concurrentReader()` — reads log content using a separate thread
- `sequentialTech()` and `parallelTech()` — compare sequential and parallel log analysis
- `reportResult()` — prints summary counts and performance comparison

## Notes

- Replace the YouTube placeholder link with the actual project demo URL.
- Ensure `tqdm` is installed before running the script.
- The simulator writes output to `poker_simulation.log` in the same folder.
- For better performance benchmarking, use at least 1,000 simulations.
