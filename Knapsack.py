import numpy as np
import matplotlib.pyplot as plt

# Problem setup
weights = [3,   2,  4,  1,  5,  3,  6,  8,  2]
values  = [10,  5,  12, 7,  8,  9,  20, 10, 5]
capacity = 10
num_items = len(weights)

# GA Parameters
population_size = 10
num_generations = 100
mutation_rate = 0.2
crossover_rate = 0.4

np.random.seed(0)

class Newborn:
    """
    Represents a solution to the Knapsack Problem.
    DNA is a binary list indicating whether each item is selected.
    """
    def __init__(self, dna):
        self.dna = dna
        self.fit = self.fitness()

    def fitness(self):
        total_weight = sum(weights[i] for i in range(num_items) if self.dna[i] == 1)
        total_value  = sum(values[i]  for i in range(num_items) if self.dna[i] == 1)
        return total_value if total_weight <= capacity else 0

    def mutate(self):
        """
        Mutate by flipping each gene with a small chance.
        """
        new_dna = [1 - gene if np.random.rand() < 0.1 else gene for gene in self.dna]
        return Newborn(new_dna)

def crossover(dna1, dna2):
    """
    Single-point crossover between two parents.
    """
    pattern = np.random.randint(2, size=num_items)
    child_dna = [dna1[i] if pattern[i] == 0 else dna2[i] for i in range(num_items)]
    return Newborn(child_dna)

def main():
    # Initialize population
    population = [Newborn(np.random.randint(2, size=num_items).tolist()) for _ in range(population_size)]
    
    best_fitnesses = []

    for gen in range(num_generations):
        # Mutation
        num_mutations = round(mutation_rate * population_size)
        for i in range(num_mutations):
            population.append(population[i].mutate())

        # Crossover
        num_crossovers = int((crossover_rate * population_size) // 2 * 2)  # Ensure even number
        for i in range(0, num_crossovers, 2):
            child = crossover(population[i].dna, population[i+1].dna)
            population.append(child)

        # Selection: keep top N
        population = sorted(population, key=lambda x: x.fit, reverse=True)
        population = population[:population_size]

        best_fit = population[0].fit
        best_fitnesses.append(best_fit)
        print(f"Generation {gen+1:02d} | Best fitness: {best_fit}")

    # Final Result
    best = population[0]
    print("\n🏆 Best solution found:")
    print("DNA:", best.dna)
    print("Total value:", best.fit)
    total_weight = sum(weights[i] for i in range(num_items) if best.dna[i] == 1)
    print("Total weight:", total_weight)

    # Plot fitness over generations
    plt.plot(range(1, num_generations+1), best_fitnesses, marker='o', color='blue')
    plt.title("Fitness Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
