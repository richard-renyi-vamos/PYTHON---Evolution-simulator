import random

# Define a creature with traits
class Creature:
    def __init__(self, speed, strength):
        self.speed = speed
        self.strength = strength

    def fitness(self):
        # Fitness is determined by a combination of speed and strength
        return (self.speed + self.strength) / 2

# Generate initial population
def create_population(size):
    return [Creature(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(size)]

# Natural selection: choose the best-fit creatures to reproduce
def select_parents(population, selection_rate):
    population.sort(key=lambda creature: creature.fitness(), reverse=True)
    num_selected = int(len(population) * selection_rate)
    return population[:num_selected]

# Create offspring with mutation
def reproduce(parents, population_size, mutation_rate=0.1):
    offspring = []
    while len(offspring) < population_size:
        parent1, parent2 = random.sample(parents, 2)
        child_speed = (parent1.speed + parent2.speed) / 2 + random.uniform(-mutation_rate, mutation_rate)
        child_strength = (parent1.strength + parent2.strength) / 2 + random.uniform(-mutation_rate, mutation_rate)
        offspring.append(Creature(child_speed, child_strength))
    return offspring

# Run the evolution simulation
def run_simulation(generations, population_size, selection_rate=0.5, mutation_rate=0.1):
    population = create_population(population_size)
    for generation in range(generations):
        print(f"Generation {generation+1}")
        avg_fitness = sum([creature.fitness() for creature in population]) / len(population)
        print(f"  Average fitness: {avg_fitness:.2f}")
        
        # Select parents and create new population
        parents = select_parents(population, selection_rate)
        population = reproduce(parents, population_size, mutation_rate)

    return population

# Parameters
generations = 20
population_size = 100
selection_rate = 0.5
mutation_rate = 0.2

# Run the simulation
final_population = run_simulation(generations, population_size, selection_rate, mutation_rate)

# Display final population fitness
best_creature = max(final_population, key=lambda creature: creature.fitness())
print(f"Best creature's fitness: {best_creature.fitness():.2f}, speed: {best_creature.speed:.2f}, strength: {best_creature.strength:.2f}")
