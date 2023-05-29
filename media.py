from params_set import *
import numpy as np
import pickle
import pandas as pd
import random
import matplotlib.pylab as plt

df = pd.read_csv('dataframe.csv', names = None)

df_1 = pd.DataFrame(data=None, columns = None)
##print(df_1)
k = 0
conta = 0

for j in range(len(df)):
    if j == 0:
        conta = df['ESD'][j]
        err_conta =  df['Erro ESD'][j]
        k = 1
    elif j > 0 and df['Energy(eV)'][j] == df['Energy(eV)'][j-1]:
        conta += df['ESD'][j]
        err_conta +=  df['Erro ESD'][j]
        k += 1
    else:
        df_1.set_value(j,'Geometria', df['Geometria'][j-1])
        df_1.set_value(j,'Distance(cm)', df['Distance(cm)'][j-1])        
        df_1.set_value(j,'Campo', df['Campo'][j-1])
        df_1.set_value(j,'Cobre', df['Cobre'][j-1])
        df_1.set_value(j,'Energy(eV)', df['Energy(eV)'][j-1])
        df_1.set_value(j, 'ESD', conta/k)
        df_1.set_value(j, 'Erro ESD', err_conta/k)
##        print(k)
        conta = df['ESD'][j]
        err_conta =  df['Erro ESD'][j]
##        plt.plot(df['Energy(eV)'][j-k:j].values, df['Eabs 2'][j-k:j].values,'o')
##        plt.title(df['Campo'][j-1])
##        plt.ylabel(df['Geometria'][j-1])
##        plt.show()
        k = 1
        


df_1.to_csv('dataframe_media.csv', index = None)  
