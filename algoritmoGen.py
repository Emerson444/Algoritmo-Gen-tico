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
        
        

