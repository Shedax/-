import math
def fractal(current): #функция, возвращающая таблицу значений текущего фрактала
    #Лист папоротника
    if current == 1 :
        matrix=[[0.0,0.0,0.0,0.16,0.0,0.0,0.01],
         [0.85,0.04,-0.04,0.85,0.0,1.6,0.85],
         [0.2,-0.26,0.23,0.22,0.0,1.6,0.07],
        [-0.15,0.28,0.26,0.24,0.0,0.44,0.07]]

    #Салфетка Серпинского
    elif current == 2:
        matrix = [[0.5, 0.0, 0.0,  0.5, 0.0, 0.0, 1/3],
               [0.5, 0.0, 0.0,  0.5, 0.5, 0.0, 1/3],
               [0.5, 0.0, 0.0,  0.5, 0.25, math.sqrt(3)/4, 1/3]]

    #Кривая Коха
    elif current == 3:
        matrix = [[1/3, 0.0, 0.0,  1/3, 0.0, 0.0, 0.25],
           [1/6, math.sqrt(3)/6, -math.sqrt(3)/6,  1/6, 1/3, 0.0, 0.25],
           [1/6, -math.sqrt(3)/6, math.sqrt(3)/6,  1/6, 0.5, -math.sqrt(3)/6, 0.25],
           [1/3, 0.0, 0.0,  1/3, 2/3, 0.0, 0.25]]

    #Контур двойного дракона Хартера-Хэйтуэя
    elif current ==4:
        matrix = [[0.25, -0.25, 0.25, 0.25, 0.0, 0.0, 0.205],
        [0.5, 0.5, -0.5, 0.5, 0.25, 0.25, 0.590],
        [1/(4*math.sqrt(2)), -math.sqrt(3)/(4*math.sqrt(2)), math.sqrt(3)/(4*math.sqrt(2)), 1/(4*math.sqrt(2)), 0.75, -0.25, 0.205]]

    #Дракон Хартера-Хейтуэя
    elif current ==5:
        matrix = [[0.5, 0.5, -0.5, 0.5, -1.0, 0.0, 0.5],
           [-0.5, 0.5, -0.5, -0.5, 0.0, 1.0, 0.5]]
    return matrix

def afin(j, x, y): #функция, возвращающая значения х и у в аффинных преобразованиях
    newx = x.copy()
    newy = y.copy()
    cos = math.cos(math.radians(60))
    sin = math.sin(math.radians(60))
    if j == 1 or j == 3:
        for i in range(len(newy)):
            newy[i] *= -1
            y.append(newy[i])
            newy[i] *= -1
            x.append(newx[i])
    if j == 2 or j == 3:
        for i in range(len(newx)):
            x.append(cos * newx[i] - sin * newy[i])
            y.append(sin * newx[i] + cos * newy[i])
        for i in range(len(newx)):
            x.append(cos * newx[i] + sin * newy[i] + 0.5)
            y.append(-sin * newx[i] + cos * newy[i] + math.sqrt(3) / 2)
    return x, y
