import numpy as np
import json

def relation_matrix(ranking, n):
    Y = np.zeros((n, n), dtype=int)
    np.fill_diagonal(Y, 1) 

    for idx, idx2 in enumerate(ranking):
        if isinstance(idx2, int):
            idx2 = [idx2]

        for i in idx2:
            for j in idx2:
                Y[i - 1][j - 1] = 1

        for i in idx2:
            for prev in ranking[:idx]:
                if isinstance(prev, int):
                    prev = [prev]
                for j in prev:
                    Y[j - 1][i - 1] = 1
    return Y

def algoritm(A_matrix, B_matrix):

    # Логическое умножение A и B
    step1 = np.logical_and(A_matrix, B_matrix)

    # Логическое умножение транспонированных матриц
    step2 = np.logical_and(A_matrix.T, B_matrix.T)

    # Логическое сложение результатов шагов 1 и 2
    result_matrix = np.logical_or(step1, step2)


    return result_matrix.astype(int)

def main(file_path1, file_path2, n):
    """Основная функция, возвращающая ядро противоречий."""
    # Загружаем JSON из файлов
    with open(file_path1, 'r', encoding='utf-8') as file1:
        ranking1 = json.load(file1)
    
    with open(file_path2, 'r', encoding='utf-8') as file2:
        ranking2 = json.load(file2)

    A_matrix = relation_matrix(ranking1, n)
    B_matrix = relation_matrix(ranking2, n)
    result = algoritm(A_matrix, B_matrix)

    return result


print(main("test1.json", "test2.json", 10))
