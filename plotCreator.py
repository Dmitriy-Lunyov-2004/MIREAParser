
import matplotlib.pyplot as plt
import numpy as np

def create_plot(x, y):
    plt.title('Распределение абитуриентов по баллам')
    plt.xlabel('баллы ВИ')
    plt.ylabel('число абитуриентов')
    plt.grid()
    plt.plot(x, y)
    plt.show()