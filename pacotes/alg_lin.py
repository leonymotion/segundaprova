import numpy as np

def det(mat):
    return np.linalg.det(np.array(mat))

def inv(mat):
    return np.linalg.inv(np.array(mat))

def autovalores(mat):
    return np.linalg.eigvals(np.array(mat))
