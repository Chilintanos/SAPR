import pandas as pd
import csv
from scipy.stats import entropy
import numpy as np
import math

def task(file_path):
    with open(file_path, newline='') as csvfile:
        datareader = csv.reader(csvfile)
        ext_length_matrix = [list(map(float, row)) for row in datareader]

    n = len(ext_length_matrix)  # количество узлов
    k = len(ext_length_matrix[0])  # количество отношений


    probabilities = [[val / (n-1) for val in row] for row in ext_length_matrix]     # Вычисляем вероятности

    entropy = 0
    for row in probabilities:
        for val in row:
            if val > 0:
                entropy -= val * math.log2(val)

    return round(entropy, 1)



file_path = "C:/Users/n8122/Downloads/task3.csv"  # Путь к файлу с csv-строкой
result = task(file_path)
print("\n", result)