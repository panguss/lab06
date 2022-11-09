import numpy as np  # Нужен для создания матрицы
import pandas as pd  # нужен для нормальной работы numpy

# Пользователь вводит количество критериев
while True:
    try:
        number = int(input('Сколько критериев Вы желаете рассмотреть?\n''Введите количество: '))
    except ValueError as e:
        print("Введите число, а не текст!")
    else:
        break

def matrix(n):
    # Создаем матрицу
    M = np.ones([n, n])
    for i in range(0, n):
        for j in range(0, n):
            if i < j:
                while True:
                    try:
                        mij = input(f'\nНасколько критерий {i}  приоритетнее критерия {j}?\n''Введите коэффициент: ')
                    except ValueError as e:
                        print("Введите число, а не текст/ноль!")
                    else:
                        break

                M[i, j] = float(mij)
                M[j, i] = 1 / float(mij)  # Добавление обратных элементов (под главной диагональю)

    # Чтобы вывести весовые коэффициенты, необходимо вычислить собственный вектор матрицы М.
    # Для этого воспользуемся функцией numpy.linalg.eig(М)[1][:,0]

    vector = np.linalg.eig(M)[1][:, 0]
    # пронормируем вектор
    norm_vector = vector / vector.sum()
    return norm_vector


norm_vector = matrix(number)
# выводим результат
for x in range(len(norm_vector)):
    res = norm_vector[x]
    print(f'Коэффициент критерия {x}: {res:.2f}')  # округление до сотых