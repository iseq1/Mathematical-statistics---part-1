import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
mpl.use('TkAgg')

def load_data():
    return pd.read_excel('D:/failiki/university/2 курс/ТВИМС/5/r1z1.xlsx')

sample = load_data()['X']

def Sample(): #Объём выборки
    return load_data()['X'].count()

def Minimum(): #Минимум
    giant = 9999
    df = load_data()['X'].tolist()
    df.sort()
    dfbett = df.__len__()
    for i in range(0, dfbett):
        if giant>df[i]:
            giant=df[i]
    return giant

def Maximum(): #Максимум
    giant = 0
    df = load_data()['X'].tolist()
    df.sort()
    dfbett = df.__len__()
    for i in range(0, dfbett):
        if giant<df[i]:
            giant=df[i]
    return giant

def Range(): #Размах
    return Maximum() - Minimum()

def Average(): #Среднее
    giant=0
    df = load_data()['X'].tolist()
    df.sort()
    dfbett = df.__len__()
    for i in range(0, dfbett):
        giant+=df[i]
    return giant/Sample()

def Shifted_dispersion(): #Смещённая дисперсия
    giant = 0
    df = load_data()['X'].tolist()
    df.sort()
    dfbett = df.__len__()
    for i in range(0, dfbett):
        giant+= (df[i]-Average())**2
    return giant/Sample()

def Unshifted_dispersion(): #Несмещённая дисперсия
    giant = 0
    df = load_data()['X'].tolist()
    df.sort()
    dfbett = df.__len__()
    for i in range(0, dfbett):
        giant+= (df[i]-Average())**2
    return giant/(Sample()-1)

def Standard_deviation(): #Стандартное отклонение
    return math.sqrt(Shifted_dispersion())

def Asymmetry(): #Асимметрия
    giant = 0
    df = load_data()['X'].tolist()
    df.sort()
    dfbett = df.__len__()
    for i in range(0, dfbett):
        giant += (df[i] - Average()) ** 3
    return giant/(Sample()*(Standard_deviation()**3))

def Median(): #Медиана
    df = load_data()['X'].tolist()
    df.sort()
    dfbett = df.__len__()
    if Sample()%2!=0:
        return df[int((Sample())/2)]
    if Sample()%2==0:
        return (df[int((Sample()/2))] + df[int(Sample()/2+1)])/2

def Helper(q):
    df = load_data()['X'].tolist()
    df.sort()
    dfbett = df.__len__()
    if (dfbett-1)*q == int((dfbett-1)*q):
        return df[int((dfbett-1)*q+1)]
    if (dfbett-1)*q > int((dfbett-1)*q):
        return (df[int((dfbett-1)*q)+1] + df[int((dfbett-1)*q)+2])/2

def Interquartile_latitude(): #Интерквартильная широта
    return Helper(0.75)-Helper(0.25)

def Kurtosis_coefficient(): #Коэффициент экцесса
    df = load_data()['X'].tolist()
    df.sort()
    dfbett = df.__len__()
    coefficient = 0
    for i in df:
        coefficient += (i-Average())**4
    return (coefficient/(Sample()*(Standard_deviation()**4))) - 3



def plot_histogramm(sample):
    sns.displot(data=sample, x=sample, col=int(Sample()/10), kde=True)
    plt.title('Гистограмма')
    plt.xlabel('Выборка')
    plt.ylabel('Частота')
    plt.show()

def plot_empirical_cdf(sample):
    hist, edges = np.histogram(sample, bins=len(sample))
    Y = hist.cumsum()
    for i in range(len(Y)):
        plt.plot([edges[i], edges[i+1]],[Y[i]/Sample(), Y[i]/Sample()], c="blue")
    plt.title('Эмпирическая функция распределения')
    plt.xlabel('Выборка')
    plt.ylabel('Частота')
    plt.show()

print("Объем выборки: \t", Sample(),
      "\nМинимум: ", Minimum(),
      "\nМаксимум: ", Maximum(),
      "\nРазмах: ", Range(),
      "\nСреднее: ", Average(),
      "\nСмещённая дисперсия: ", Shifted_dispersion(),
      "\nНесмещённая дисперсия: ", Unshifted_dispersion(),
      "\nСтандартное отклонение: ", Standard_deviation(),
      "\nАсимметрия: ", Asymmetry(),
      "\nМедиана: ", Median(),
      "\nИнтерквартильная широта: ", Interquartile_latitude(),
      "\nКоэффициент экцесса: ", Kurtosis_coefficient())

plot_histogramm(sample)
plot_empirical_cdf(sample)