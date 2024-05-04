import numpy as np

def calculate(list):
    a = np.array(list)
    if len(a) != 9:
        raise ValueError("List must contain nine numbers.")


    matrix = a.reshape((3,3))

    mean = [np.mean(matrix, axis=0).tolist(),np.mean(matrix, axis=1).tolist(), np.mean(matrix)]
    variance = [np.var(matrix, axis=0).tolist(),np.var(matrix, axis=1).tolist(), np.var(matrix)]
    std = [np.std(matrix, axis=0).tolist(),np.std(matrix, axis=1).tolist(), np.std(matrix)]
    max = [np.max(matrix, axis=0).tolist(),np.max(matrix, axis=1).tolist(), np.max(matrix)]
    min = [np.min(matrix, axis=0).tolist(),np.min(matrix, axis=1).tolist(), np.min(matrix)]
    sum = [np.sum(matrix, axis=0).tolist(),np.sum(matrix, axis=1).tolist(), np.sum(matrix)]

    calculations = {'mean': mean,
            'variance': variance,
            'standard deviation': std,
            'max': max,
            'min': min,
            'sum': sum}

    return calculations