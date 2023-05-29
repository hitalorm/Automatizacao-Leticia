'''
Script para automatização de Simulação Monte Carlo usando o código PENELOPE


Versão original criada por Rodrigo Trevisan Massera
Código adaptado para a simulação de detectores adaptada por Hitalo R. Mendes

'''


from params_set import *
import numpy as np
import pickle
import pandas as pd
import random
import seed_creator as sd




def create_df():
    columns = ['Historias','Energy(eV)','Seed1', 'Seed2']
    parameters = pd.DataFrame(data=None, columns = columns)
    return parameters

def create_dat():
    df = create_df()
    
    #Vetor que determina a energia do feixe inicial de fótons
    energy_vec = np.array([40,50,60,70,80,90,100,110,120,130,140,150])*1e3
    
    #nome do arquivo de geometria
    geometry_name = ['phantom.geo']

    #material do sensor
    materials = ['CdTe.mat','Si.mat']

    #alterar o numero de histórias da simulação
    hist = [2E5]
    r = 0

    for m in range(len(materials)):
        for energy in range(len(energy_vec)):
            for g in range(len(geometry_name)):
                for h in range(len(hist)):
        
                    s1 = random.randrange(100)
                    s2 = random.randrange(100)

                    while s1 == 0 or s2 == 0:
                        s1 = random.randrange(100)
                        s2 = random.randrange(100)

                    seed1 = sd.calc_seed1(s1)
                    seed2 = sd.calc_seed2(s2)
                    

                    for s in range(len([1])):
                            df.at[r,'Energy(eV)'] = energy_vec[energy]
                            df.at[r,'Historias'] = hist[h]
                            df.at[r,'Seed1'] = seed1[s]
                            df.at[r,'Seed2'] = seed2[s]
                            df.at[r,'Geometria'] = geometry_name[g]
                            df.at[r,'Material'] = materials[m]
                            r += 1
                        
                                                              
                               
    vec_number = np.arange(len(df))
    np.savetxt('checkpoint.dat', vec_number, '%05d')
    
    df.to_csv('dataframe.csv',index = None)    
    #print(df)
    #print(len(df))

    print('Dataframe criado')
    print('Tamanho do dataframe: ',len(df))


