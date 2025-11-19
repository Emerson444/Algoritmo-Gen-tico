import random

distance = [
    [0, 2, 9, 10],
    [2, 0, 7, 1],
    [9, 7, 0, 6],
    [10, 1, 6, 0]
]

num_cities = len(distance)

def random_solution():
    sol = list(range(num_cities))
    random.shuffle(sol)
    return sol

def total_distance(solution):
    dist = 0
    for i in range(num_cities):
        dist += distance[solution[i]][solution[(i+1) % num_cities]]
    return dist

def selection(population):
    population.sort(key=total_distance)
    return population[:2]

def parents_fix(parent1,parent2):
    cut = num_cities // 2
    childprocess = parent1[:cut] + parent2[cut:]

def mutate(solution):
    i, j = random.sample(ranger(num_cities), 2)
    solution[i], solution[j] = solution[j], solution[i]
population = [random_solution() for _ in range(10)]