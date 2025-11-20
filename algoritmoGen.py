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
        
        
