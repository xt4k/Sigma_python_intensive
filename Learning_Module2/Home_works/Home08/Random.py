# ------------------------ Statistical learning: regression models  -------------------------------

'''

МОДЕЛЬ:
законів розподілу випадкових величин (ВВ).

Довідковий матеріал:
https://numpy.org/doc/stable/reference/random/generator.html
https://www.w3schools.com/python/numpy/numpy_random_exponential.asp
https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html
https://www.geeksforgeeks.org/numpy-random-exponential-in-python/
https://numpy.org/doc/stable/reference/random/generated/numpy.random.chisquare.html

Package                      Version
---------------------------- -----------
pip                          23.1
numpy                        1.23.5
matplotlib                   3.6.2

'''

import math as mt

import matplotlib.pyplot as plt
import numpy as np

from Learning_Module2.Home_works.Home08.Model import Model
from Learning_Module2.Lections.Lesson_20_8.Statistical_learning import Stat_characteristics_in


# ------------------------- експоненційний закон розподілу ВВ ----------------------------
def random_exponential(alfa, iter):
    S = np.random.exponential(alfa,
                              iter)  # експоненційний закон розподілу ВВ з вибіркою єб'ємом iter та параметрами: dsig
    mS = np.median(S)
    dS = np.var(S)
    scvS = mt.sqrt(dS)
    print('------- статистичны характеристики ЕКСПОНЕНЦІЙНОГО закону розподілу ВВ -----')
    print('матиматичне сподівання ВВ=', mS)
    print('дисперсія ВВ =', dS)
    print('СКВ ВВ=', scvS)
    print('----------------------------------------------------------------------------')
    # гістограма закону розподілу ВВ
    plt.hist(S, bins=20, facecolor="blue", alpha=0.5)
    plt.show()
    return S


if __name__ == '__main__':
    # ----------------------------------------------- Constant section -----------------------------------------------
    n = 10_000  #
    iter = int(n)
    Q_AV = 3  # коефіцієнт переваги АВ
    nAVv = 10
    nAV = int((iter * nAVv) / 100)  # кількість АВ у відсотках та абсолютних одиницях
    dm = 0
    dsig = 5  # параметри нормального закону розподілу ВВ: середнє та СКВ
    # ---------------------
    alfa = 1
    # ----------------------------------------------- Constant section -----------------------------------------------

    # --------------- графіки тренда, вимірів з нормальним шумом  ---------------------------
    def Plot_AV(S0_L, Text):
        plt.clf()
        plt.plot(S0_L)
        plt.ylabel(Text)
        plt.show()
        return

    # --------------- графіки тренда, вимірів з нормальним шумом  ---------------------------


    print('Обраний закон розподілу ВВ: експоненційний')
    print('----------------- Обрано: експоненційний закон розподілу ВВ --------------')
    print('------------------- ВХІДНІ параметри законі розподілу ВВ:-----------------')

    print('параметр alfa =', alfa)
    print('розмір вибірки ВВ =', iter)
    random_exponential(alfa, iter)

    print("------------------------------------------ Ideal trend model  ------------------------------------------- ")
    S0 = Model(n)
    Plot_AV(S0,  'square model - ideal trend')

    print("------------------------------------- Static selection additive model   ---------------------------------- ")
    Stat_characteristics_in(S0, 'selected selection  ')
