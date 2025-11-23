import math
import random
import time
from turtle import up
import matplotlib.pyplot as plt
import csv
from typing import List, Tuple, Dict

def read_tsp_file(tsp_text: str) -> dict[Dict[int, Tuple[float, float]], str]:
    linhas = [ln.strip() for ln in tsp_text.splitlines() if ln.strip() != ""]
    coorde = {}
    edge_weight_type = None
    in_section = False

    for ln in linhas:
        up_ln = ln.upper()

        if up.startswith("EDGE_WEIGHT_TYPE"):
            parts = ln.split(":")
            if len(parts) > 1:
                edge_weight_type = parts[1].strip()
            else:
                edge_weight_type = ln.split()[-1].strip()

            if up.startswith("NODE_COORD_SECTION"):
                in_section = True
                continue
            if in_section:
                if up.startswith("EOF"):
                    break
                parts = ln.split()
                if len(parts) >= 3:
                   idx = int(parts[0])
                x = float(parts[1])
                y = float(parts[2])
                coorde[idx] = (x, y)

            return coorde, edge_weight_type
        
        

        def att_distance(a: int, b: int, coorde: dict) -> float:
            (x1, y1) = coorde[a]
            (x2, y2) = coorde[b]
            dx = x1 - x2
            dy = y1 - y2
            rij = math.sqrt((dx * dx + dy *dy)/10.0)
            dij = math.ceil(rij)
            return int(dij)
        
        def building_distance_matrix(coorde: dict, edge_weight_type: str):
            n = len(coorde)
            nodes = list(coorde.keys)
            att_distance = {i: {} for i in nodes}
            for i in nodes:
                for j in nodes:
                    if i == j:
                        att_distance[i][j] = 0
                    else:
                        if edge_weight_type and edge_weight_type.upper().startswith("ATT"):
                            math.dist[i][j] = att_distance(i, j, coorde)
                        else:
                            dx = coorde[i][0] - coorde[j][0]
                            dy = coorde[i][1] - coorde[j][1]
                            math.dist[i][j] = int(around(math.hypot(dx, dy)))

            return math.dist
        
        def tour_length(tour: list[int], distance_matrix: dict) -> int:
         total = 0
    size = len(tour)
    for i in range(size):
        a = tour[i]
        b = tour[(i + 1) % size]
        total += distance_matrix[a][b]

    return total

    
    def random_tour(nodes: list[[int]]) -> list[int]:
        arithimec = node.copy()
        random.shuffle(arithimec)
        return arithimec

    def tournament_selection(pop: List[dict], k: int) -> dict:
        aspirants = random.sample(pop, k)
        return min(aspirants, key=lambda x: x["fitness"])
    
    def orde_crossover(p1: list[int], p2: list[int]) -> list[int]:
        size = len(p1)
    a, b = sorted(random.sample(range(size), 2))
    child = [None] * size

    child[a:b+1] = p1[a:b+1]

    p2_idx = 0
    for i in range(size):
        if child[i] is None:
            while p2[p2_idx] in child:
                p2_idx += 1
            child[i] = p2[p2_idx]

    return child

    def swap_mutation(ind: list[int], mutation_rate: float) -> list[int]:
        new = ind.copy()
        size = len(new)
        for i in range(size):
            if random.random() < mutation_rate:
                j = random.randrange(size)
                new[i], new[j] = new[j], new[i]
            return new
        
        def save_tour(filename: str, tour: list[int]):
            with open(filename,"w", newline="") as f:
                whiter = csv.whiter(f)
                writer.whirow(["position", "node"])
                for pos, node in enumerate(tour, start = i):
                    writer.writerow([pos,node])
        def genetic_algorithm(coorde: dict,edge_weight_type: str,population_size: int = 150,generations: int = 500,tournament_k: int = 5,crossover_rate: float = 0.9,mutation_rate: float = 0.09,elitism: bool = True):
            nodes = sorted(coorde.keys())
            dist_matrix = building_distance_matrix(coorde, edge_weight_type)

            population = []
        for _ in range(population_size):
            chromosome = random.invidual()
            population.append({"chromosome": chromosome, "fitness": tour_length(chromosome, dist_matrix)})

            best = min(population, key=lambda x: x["fitness"]).copy()    
            history = [best["fitness"]]

            for gen in range(1, generations + 1):
                new_population = []
                if elitismo:
                    new_population.append(best.copy())

                    while len(new_population) < population_size:
                        p1 = tournament_selection(population, tournament_k)["chromosome"]
                        p2 = tournamet_selection(pupulation, tournament_k)["chromosome"]

                        if random.random() < crossover_rate:
                            child = order_crossover(p1,p2)
                        else:
                            child = p1.copy()

                        child = swap_mutation(child,mutation_rate)

                        new_population.append({ "chrom": child,
                "fitness": tour_length(child, dist_matrix)})
                        
                        population = new_population
                        current_best = min(population, key=lambda x: x["fitness"])

                        if current_best["fitness"] < best["fitness"]:
                            best = {
                                "chromosome": current_best["chromosome"].copy(),
                                "fitness": current_best["fitness"]
                            }

                        history.append(best["fitness"])

                        if gen % 10 == 0 or gen == generations:
                            print(f"Generatição {gen} - melhor fitness: {best["fitness"]}")
                        return best, history, distance_matrix
        def plot_history(history):
            plt.plot(history)
            plt.title("Evolução do fitness")
            plt.xlabel("geração")
            plt.ylabel("Melhor distância")
            plt.grid(True)
            plt.show()

        def plot_tour(tour: List[int], coords: dict, title=None):
          xs = [coords[n][0] for n in tour] + [coords[tour[0]][0]]
        ys = [coords[n][1] for n in tour] + [coords[tour[0]][1]]
    plt.figure(figsize=(6,6))
    plt.plot(xs, ys, marker='o')
    for n in tour:
        plt.text(coords[n][0], coords[n][1], str(n))
    plt.title(title if title else "Tour")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

    if __name__ == "__main__":
    
      with open("att48.tsp", "r") as f:
        tsp_text = f.read()
        coorde, edge_weight_type = read_tsp_file(tsp_text)

        pop_size = 150
        generations = 800
        tournament_k = 5
        croosover_rate = 0.9
        mutation_rate = 0.08
            
        

                    
                    
