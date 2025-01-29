import random
import math


def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Hill Climbing


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    hill_climb_solution = [random.uniform(b[0], b[1]) for b in bounds]
    hill_climb_value = func(hill_climb_solution)

    for _ in range(iterations):
        neighbor = [
            max(min(x + random.uniform(-0.1, 0.1), b[1]), b[0])
            for x, b in zip(hill_climb_solution, bounds)
        ]
        neighbor_value = func(neighbor)

        if neighbor_value < hill_climb_value:
            hill_climb_solution = neighbor
            hill_climb_value = neighbor_value

        if abs(neighbor_value - hill_climb_value) < epsilon:
            break

    return hill_climb_solution, hill_climb_value

# Random Local Search


def random_local_search(func, bounds, iter=1000, epsilon=1e-6):
    local_best_solution = [random.uniform(b[0], b[1]) for b in bounds]
    local_best_value = func(local_best_solution)

    for _ in range(iter):
        rnd_solution = [random.uniform(b[0], b[1]) for b in bounds]
        rnd_value = func(rnd_solution)

        if rnd_value < local_best_value:
            local_best_solution = rnd_solution
            local_best_value = rnd_value

        if abs(rnd_value - local_best_value) < epsilon:
            break

    return local_best_solution, local_best_value

# Simulated Annealing


def simulated_annealing(func, bounds, iter=1000, temp=1000, cooling=0.95, epsilon=1e-6):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    best_solution = current_solution[:]
    best_value = current_value

    for _ in range(iter):
        neighbor = [
            max(min(x + random.uniform(-0.1, 0.1), b[1]), b[0])
            for x, b in zip(current_solution, bounds)
        ]
        neighbor_value = func(neighbor)
        delta = neighbor_value - current_value
        probability = math.exp(-delta / temp) if delta > 0 else 1

        if random.random() < probability:
            current_solution = neighbor
            current_value = neighbor_value

        if current_value < best_value:
            best_solution = current_solution[:]
            best_value = current_value

        temp *= cooling

        if temp < epsilon:
            break

    return best_solution, best_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
