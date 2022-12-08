from statistics import geometric_mean
n = int(input('Введите количество критериев (целое число): '))
m = []
for i in range(n):
    g = []
    for j in range(n):
        if i == j:
            a = 1
        elif i > j:
            a = 1 / m[j][i]
        else:
            while True:
                try:
                    a = float(input(f'Введите отношение критерия {i + 1} к критерию {j + 1}: '))
                    break
                except ValueError:
                    print('Ошибка ')
        g.append(a)
    m.append(g)
s = 0
sz = []

for c in range(n):
    r = geometric_mean(m[c])
    s += r
    sz.append(r)

for z in range(n):
    weight = sz[z] / s
    print(f'Весовой коэффициент {z + 1} критерия: {round(weight, 2)}')
