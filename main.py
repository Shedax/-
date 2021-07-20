import matplotlib.pyplot as plt #подключаем библиотеки
from random import randint
from config import *
x = list() #список значений х
y = list() #список значений у
x.append(0)
y.append(0)
for j in range(4):
    matrix = fractal(3) #получаем текущую таблицу
    for i in range(1, 15000): #количество точек
        # случайное число от 1 до 100, реализует вероятность
        p = randint(1, 100)
        # T1
        if p<matrix[0][6]*100:
            x.append(matrix[0][0] * (x[i-1]) + matrix[0][1] * (y[i-1])+matrix[0][4])
            y.append(matrix[0][2] * (x[i-1]) + matrix[0][3] * (y[i-1])+matrix[0][5])
        # T2
        if p >=matrix[0][6]*100 and p <= matrix[1][6]*100+matrix[0][6]*100:
            x.append(matrix[1][0]* (x[i-1]) + matrix[1][1] * (y[i-1])+matrix[1][4])
            y.append(matrix[1][2] * (x[i-1]) + matrix[1][3] * (y[i-1])+matrix[1][5])
        # T3
        if len(matrix)>2 and p > matrix[1][6]*100+matrix[0][6]*100 and p <= round(matrix[1][6]*100+matrix[0][6]*100+matrix[2][6]*100):
            x.append(matrix[2][0] * (x[i-1]) + matrix[2][1] * (y[i-1])+matrix[2][4])
            y.append(matrix[2][2] * (x[i-1]) + matrix[2][3] * (y[i-1])+matrix[2][5])
        # T4
        if len(matrix)>3 and p > matrix[1][6]*100+matrix[0][6]*100+matrix[2][6]*100 and p <= round(matrix[1][6]*100+matrix[0][6]*100+matrix[2][6]*100+matrix[3][6]*100):
            x.append(matrix[3][0] * (x[i-1]) + matrix[3][1] * (y[i-1]) + matrix[3][4])
            y.append(matrix[3][2] * (x[i-1]) + matrix[3][3] * (y[i-1]) + matrix[3][5])
    newx, newy = afin(j, x, y)#получаем х и у преобразования
    x+=newx#заносим их в список
    y+=newy
    plt.scatter(x, y, s=0.05, edgecolor='purple')
    plt.show()#отображение изображения
    x = list()#сбрасываем значения х и у для следующего фрактала
    y = list()
    x.append(0)
    y.append(0)
