import numpy as np


def calculate_entropy(probabilities):
    total_entropy = -np.sum(probabilities * np.log2(probabilities, where=(probabilities > 0)))
    return total_entropy

def main():
    # Данные по покупкам
    purchases = np.array([
        [20, 15, 10, 5],
        [30, 20, 15, 10],
        [25, 25, 20, 15],
        [20, 20, 25, 20],
        [15, 15, 30, 25]
    ])

    total_purchases = purchases.sum()

    # Вероятности для A (возрастные группы) и B (товары)
    P_A = purchases.sum(axis=1) / total_purchases  
    P_B = purchases.sum(axis=0) / total_purchases  
    P_AB = purchases / total_purchases             

    # Вычисление энтропии H(AB)
    H_AB = calculate_entropy(P_AB)

    # Вычисление энтропии H(A)
    H_A = calculate_entropy(P_A)

    # Вычисление энтропии H(B)
    H_B = calculate_entropy(P_B)

    # Условная энтропия H(B|A) и информация I(A, B)
    Ha_B = H_AB - H_A
    I_AB = H_B - Ha_B

    # Округление до второго знака
    results = [round(val, 2) for val in [H_AB, H_A, H_B, Ha_B, I_AB]]

    return results

# Запуск функции
if __name__ == "__main__":
    print(main())
