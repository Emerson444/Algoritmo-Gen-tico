import math
import random
import matplotlib.pyplot as plt
import csv

def ler_tsp(texto: str):
    linhas = [ln.strip() for ln in texto.splitlines() if ln.strip() != ""]
    coordenadas = {}
    tipo_distancia = None
    lendo_secao = False

    for ln in linhas:
        up = ln.upper()

        if up.startswith("EDGE_WEIGHT_TYPE"):
            tipo_distancia = ln.split(":")[1].strip()

        if up.startswith("NODE_COORD_SECTION"):
            lendo_secao = True
            continue

        if lendo_secao:
            if up.startswith("EOF"):
                break

            partes = ln.split()
            if len(partes) >= 3:
                idx = int(partes[0])
                x = float(partes[1])
                y = float(partes[2])
                coordenadas[idx] = (x, y)

    return coordenadas, tipo_distancia

def distancia_att(a: int, b: int, coord: dict) -> int:
    (x1, y1) = coord[a]
    (x2, y2) = coord[b]

    dx = x1 - x2
    dy = y1 - y2

    rij = math.sqrt((dx * dx + dy * dy) / 10.0)
    dij = math.ceil(rij)

    return dij

def construir_matriz_distancia(coord: dict, tipo: str):
    cidades = sorted(coord.keys())
    matriz = {i: {} for i in cidades}

    for i in cidades:
        for j in cidades:
            if i == j:
                matriz[i][j] = 0
            else:
                if tipo.upper() == "ATT":
                    matriz[i][j] = distancia_att(i, j, coord)
                else:
                    dx = coord[i][0] - coord[j][0]
                    dy = coord[i][1] - coord[j][1]
                    matriz[i][j] = int(round(math.hypot(dx, dy)))

    return matriz


def calcular_custo(caminho: list, matriz: dict) -> int:
    total = 0
    tamanho = len(caminho)

    for i in range(tamanho):
        a = caminho[i]
        b = caminho[(i + 1) % tamanho]  # circular
        total += matriz[a][b]

    return total



def individuo_aleatorio(cidades: list) -> list:
    copia = cidades.copy()
    random.shuffle(copia)
    return copia

def selecao_torneio(populacao: list, k: int) -> dict:
    candidatos = random.sample(populacao, k)
    return min(candidatos, key=lambda x: x["custo"])

def crossover_ox(pai1: list, pai2: list) -> list:
    tamanho = len(pai1)
    filho = [None] * tamanho

    a, b = sorted(random.sample(range(tamanho), 2))

    filho[a:b+1] = pai1[a:b+1]

    idx2 = 0
    for i in range(tamanho):
        if filho[i] is None:
            while pai2[idx2] in filho:
                idx2 += 1
            filho[i] = pai2[idx2]

    return filho

def mutacao_swap(individuo: list, taxa: float) -> list:
    novo = individuo.copy()
    tamanho = len(novo)

    for i in range(tamanho):
        if random.random() < taxa:
            j = random.randrange(tamanho)
            novo[i], novo[j] = novo[j], novo[i]

    return novo

def algoritmo_genetico(coordenadas: dict,
                       tipo_distancia: str,
                       tamanho_pop=150,
                       geracoes=500,
                       k_torneio=5,
                       taxa_crossover=0.9,
                       taxa_mutacao=0.08,
                       elitismo=True):

    cidades = sorted(coordenadas.keys())
    matriz = construir_matriz_distancia(coordenadas, tipo_distancia)

    populacao = []
    for _ in range(tamanho_pop):
        ind = individuo_aleatorio(cidades)
        populacao.append({
            "caminho": ind,
            "custo": calcular_custo(ind, matriz)
        })

    melhor = min(populacao, key=lambda x: x["custo"]).copy()
    historico = [melhor["custo"]]

    for gen in range(1, geracoes + 1):
        nova_pop = []

        if elitismo:
            nova_pop.append(melhor.copy())

        while len(nova_pop) < tamanho_pop:
            p1 = selecao_torneio(populacao, k_torneio)["caminho"]
            p2 = selecao_torneio(populacao, k_torneio)["caminho"]

            if random.random() < taxa_crossover:
                filho = crossover_ox(p1, p2)
            else:
                filho = p1.copy()

            filho = mutacao_swap(filho, taxa_mutacao)

            nova_pop.append({
                "caminho": filho,
                "custo": calcular_custo(filho, matriz)
            })

        populacao = nova_pop
        atual = min(populacao, key=lambda x: x["custo"])

        if atual["custo"] < melhor["custo"]:
            melhor = {
                "caminho": atual["caminho"].copy(),
                "custo": atual["custo"]
            }

        historico.append(melhor["custo"])

        if gen % 50 == 0:
            print(f"Geração {gen} — melhor custo: {melhor['custo']}")

    return melhor, historico, matriz

def plotar_progresso(hist):
    plt.plot(hist)
    plt.title("Evolução do Custo")
    plt.xlabel("Gerações")
    plt.ylabel("Melhor Custo")
    plt.grid()
    plt.show()


def plotar_caminho(caminho, coord):
    xs = [coord[n][0] for n in caminho] + [coord[caminho[0]][0]]
    ys = [coord[n][1] for n in caminho] + [coord[caminho[0]][1]]

    plt.plot(xs, ys, marker='o')
    for n in caminho:
        plt.text(coord[n][0], coord[n][1], str(n))

    plt.title("Melhor Caminho Encontrado")
    plt.grid()
    plt.show()

if __name__ == "__main__":

    with open("att48.tsp", "r") as f:
        texto = f.read()

    coordenadas, tipo = ler_tsp(texto)

    melhor, historico, matriz = algoritmo_genetico(
        coordenadas,
        tipo,
        tamanho_pop=150,
        geracoes=700,
        taxa_mutacao=0.08,
        taxa_crossover=0.9
    )

    print("\nMelhor rota encontrada:", melhor["caminho"])
    print("Custo:", melhor["custo"])

    plotar_progresso(historico)
    plotar_caminho(melhor["caminho"], coordenadas)
