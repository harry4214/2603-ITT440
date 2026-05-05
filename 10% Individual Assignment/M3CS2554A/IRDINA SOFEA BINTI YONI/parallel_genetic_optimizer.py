import random
import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# =========================
# Configuration
# =========================
POPULATION_SIZE = 200
GENERATIONS = 40
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
ELITE_COUNT = 4

X_MIN, X_MAX = -10.0, 10.0
Y_MIN, Y_MAX = -10.0, 10.0

THREAD_WORKERS = 4
PROCESS_WORKERS = 4


# =========================
# Individual creation
# =========================
def create_individual():
	"""Create one random individual [x, y]."""
	return [
		random.uniform(X_MIN, X_MAX),
		random.uniform(Y_MIN, Y_MAX)
	]

def create_population(size):
	"""Create a full population."""
	return [create_individual() for _ in range(size)]


# =========================
# Fitness function
# =========================
def fitness(individual):
	"""
	Heavy fitness function.
	We want to maximize this value.
	"""
	x, y = individual
	
	score = 0.0
	# Artificially heavy computation so timing differences are visible
	for i in range(1, 4000):
		part1 = math.sin(x * i * 0.001) * math.cos(y * i * 0.001)
		part2 = math.exp(-(x * x + y * y) / 50.0)
		part3 = math.sin((x + y) * 0.05 * i)
		score += part1 + part2 + (part3 * 0.2)

	return score

# =========================
# Evaluation methods
# =========================
def evaluate_population_sequential(population):
	"""Evaluate fitness one by one."""
	return [(individual, fitness(individual)) for individual in population]

def evaluate_population_threading(population, workers=4):
	"""Evaluate fitness using threads."""
	with ThreadPoolExecutor(max_workers=workers) as executor:
		fitness_value = list(executor.map(fitness, population))
	return list(zip(population, fitness_value))

def evaluate_population_multiprocessing(population, workers=4):
	"""Evaluate fitness using processess."""
	with ProcessPoolExecutor(max_workers=workers) as executor:
		fitness_value = list(executor.map(fitness, population))
	return list(zip(population, fitness_value))

# =========================
# Genetic operators
# =========================
def tournament_selection(evaluated_population, tournament_size=3):
	"""Select one parent using tournament selection."""
	competitors = random.sample(evaluated_population, tournament_size)
	competitors.sort(key=lambda item: item[1], reverse=True)
	return competitors[0][0]

def crossover(parent1, parent2):
	"""Blend crossover between two parents."""
	if random.random() > CROSSOVER_RATE:
		return parent1[:], parent2[:]

	alpha = random.random()

	child1 = [
		alpha * parent2[0] + (1 - alpha) * parent1[0],
		alpha * parent2[1] + (1 - alpha) * parent1[1]
	]

	child2 = [
                  alpha * parent2[0] + (1 - alpha) * parent1[0],
                  alpha * parent2[1] + (1 - alpha) * parent1[1]
        ]


	return child1, child2

def mutate(individual):
	"""Randomly mutate x and y."""
	if random.random() < MUTATION_RATE:
		individual[0] += random.uniform(-1.0, 1.0)

	if random.random() < MUTATION_RATE:
		individual[1] += random.uniform(-1.0, 1.0)

	# Keep values in bounds
	individual[0] = max(X_MIN, min(X_MAX, individual[0]))
	individual[1] = max(Y_MIN, min(Y_MAX, individual[1]))

	return individual

# =========================
# GA runner
# =========================
def run_genetic_algorithm(evaluation_mode="sequential", workers=4):
	"""
	Run the full genetic algorithm using one evaluation method.
	evaluation_mode:
		- 'sequential'
		- 'threading'
		- 'multiprocessing'
	"""
	population = create_population(POPULATION_SIZE)

	start_time = time.perf_counter()

	best_individual = None
	best_fitness = float("-inf")

	for generation in range(GENERATIONS):
		# Evaluate population
		if evaluation_mode == "sequential":
			evaluated = evaluate_population_sequential(population)
		elif evaluation_mode == "threading":
			evaluated = evaluate_population_threading(population, workers)
		elif evaluation_mode == "multiprocessing":
			evaluated = evaluate_population_multiprocessing(population, workers)
		else:
			raise ValueError("Invalid evaluation mode.")

	# sort by fitness descending
	evaluated.sort(key=lambda item: item[1], reverse=True)

	# Track best solution
	current_best_individual, current_best_fitness = evaluated[0]

	if current_best_fitness > best_fitness:
		best_fitness = current_best_fitness
		best_individual = current_best_individual[:]

	print(
		f"[{evaluation_mode.upper():15}]"
		f"Generation {generation + 1:02d}/{GENERATIONS} | "
		f"Best Fitness: {current_best_fitness: .4f}"
	)

	# Elitism: keep top individuals
	new_population = [item[0][:] for item in evaluated[:ELITE_COUNT]]

	# Fill the rest of population
	while len(new_population) < POPULATION_SIZE:
		parent1 = tournament_selection(evaluated)
		parent2 = tournament_selection(evaluated)

		child1, child2 = crossover(parent1, parent2)

		child1 = mutate(child1)
		child2 = mutate(child2)

		new_population.append(child1)
		if len(new_population) < POPULATION_SIZE:
			new_population.append(child2)

	population = new_population

	end_time = time.perf_counter()
	elapsed_time = end_time - start_time

	return {
		"mode": evaluation_mode,
		"best_individual": best_individual,
		"best_fitness": best_fitness,
		"time": elapsed_time
}

# =========================
# Result printing
# =========================
def print_summary(result):
	x, y = result["best_individual"]
	print("\n" + "=" * 50)
	print(f"Mode               : {result['mode']}")
	print(f"Best x             : {x:.6f}")
	print(f"Best y             : {y:.6f}")
	print(f"Best fitness       : {result['best_fitness']:.6f}")
	print(f"Execution time     : {result['time']:.4f} seconds")
	print("=" * 50)

# =========================
# Main program
# =========================
def main():
	print("Parallel Genetic Algorithm Optimizer")
	print("-" * 50)
	print(f"Population Size     : {POPULATION_SIZE}")
	print(f"Generations         : {GENERATIONS}")
	print(f"Mutation Rate       : {MUTATION_RATE}")
	print(f"Thread Workers      : {THREAD_WORKERS}")
	print(f"Process Workers     : {PROCESS_WORKERS}")
	print("-" * 50)

	# Sequential
	sequential_result = run_genetic_algorithm("sequential")
	print_summary(sequential_result)

	# Threading
	threading_result = run_genetic_algorithm("threading", THREAD_WORKERS)
	print_summary(threading_result)

	# Multiprocessing
	multiprocessing_result = run_genetic_algorithm("multiprocessing", PROCESS_WORKERS)
	print_summary(multiprocessing_result)

	# Final comparison
	print("\nFINAL PERFORMANCE COMPARISON")
	print("-" * 50)
	print(f"Sequential         : {sequential_result['time']:.4f} seconds")
	print(f"Threading          : {threading_result['time']:.4f} seconds")
	print(f"Multiprocessing    : {multiprocessing_result['time']:.4f} seconds")
if __name__ == "__main__":
	main()
