import numpy as np
import os

Q_TABLE_PATH = os.path.join("data", "q_table.npy")

def save_q_table(q_table):
    """Guarda la tabla Q en un archivo .npy"""
    np.save(Q_TABLE_PATH, q_table, allow_pickle=True)

def load_q_table():
    """Carga la tabla Q desde archivo, si existe"""
    if os.path.exists(Q_TABLE_PATH):
        return np.load(Q_TABLE_PATH, allow_pickle=True).item()
    else:
        return {}  # Si no existe, devuelve una tabla vacía
