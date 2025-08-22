import numpy as np

def rand_vec (tam, seed=None):
    if seed: np.random.seed(seed)
    return np.random.rand(tam)

def rand_int (tam, min=0, max=100, seed=None):
    if seed: np.random.seed(seed)
    return np.random.randint(min, max, tam)

def escolher (lista, tam=3, seed=None):
    if seed: np.random.seed(seed)
    return np.random.choice(lista, tam)