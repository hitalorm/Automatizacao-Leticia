import pandas as pd
import numpy as np
import matplotlib.pylab as plt




df = pd.read_csv('dataframe.csv',names = None)
sum1 = [0 for i in range(7)]
sum2 = [0 for i in range(7)]
N = [0 for i in range(7)]

tipo = ['Dose','ESD','Kerma']

res = pd.DataFrame(data=None, columns = None)
##print(df)


for j in range(3):
##    print(sum1[j])
    index = 0
##    for i in range(12):
##                print( df['Energy(eV)'][i],sum1[j], sum2[j], N[j])

    for i in range(len(df)):
##                i += 1
##            index = 0
##                print(sum1[j])
                if i == 0:
                    sum1[j] += df[tipo[j]][i]*df['Simuladas'][i]
                    sum2[j] += (df['Erro '+ tipo[j]][i]**2)*(df['Simuladas'][i])**2
                    N[j] += df['Simuladas'][i]
##                      print(i)
                    
                elif i == len(df)-1:

                    sum1[j] += df[tipo[j]][i]*df['Simuladas'][i]
                    sum2[j] += (df['Erro '+ tipo[j]][i]**2)*(df['Simuladas'][i])**2
                    N[j] += df['Simuladas'][i]
                    
                    q = sum1[j]/N[j]
                    q2 = np.sqrt(sum2[j])/N[j]
##                    print(index,i)
                    
##                    sigma = (q2 - q**2)/(10*df['Simuladas'][i])
##                    sigma = np.sqrt(sigma)
                    res.at[index, 'Energy(eV)'] =  df['Energy(eV)'][i-1]
                    res.at[index, tipo[j]] = q
                    res.at[index, 'Erro '+ tipo[j]] =  q2
                    res.at[index, 'Geometria'] =  df['Geometria'][i-1]
                    res.at[index, 'Material'] = df['Material'][i-1]
                    res.at[index, 'Seed1'] = df['Seed1'][i-1]
                    res.at[index, 'Seed2'] = df['Seed2'][i-1]
                    res.at[index, 'Energy(eV)'] = df['Energy(eV)'][i-1]
                    res.at[index, 'Cobre'] = df['Cobre'][i-1]
                    res.at[index, 'Historias'] = N[j]
                    res.at[index, 'Campo'] = df['Campo'][i-1]
                    #res.at[index, 'HVL(mmAl)'] = df['HVL(mmAl)'][i-1]
                    #res.at[index, 'EnergiaMedia'] = df['EnergiaMedia'][i-1]
                    #res.at[index, 'Rendimento'] = df['Rendimento'][i-1]

##                    print(i)
                
                elif df['Energy(eV)'][i] == df['Energy(eV)'][i-1] and df['Cobre'][i] == df['Cobre'][i-1]:
##                  print(df['Energy(eV)'][i],df['Energy(eV)'][i+1],df['Cobre'][i],df['Cobre'][i+1])
                    sum1[j] += df[tipo[j]][i]*df['Simuladas'][i]
                    sum2[j] += (df['Erro '+ tipo[j]][i]**2)*(df['Simuladas'][i])**2
                    N[j] += df['Simuladas'][i]
##                      print(i)


                    
                            
                elif df['Energy(eV)'][i] != df['Energy(eV)'][i-1]:
##                    N[j] += df['Simuladas'][i]

                    q = sum1[j]/N[j]
                    q2 = np.sqrt(sum2[j])/N[j]
##                    print(index,i)
                    
##                    sigma = (q2 - q**2)/(10*df['Simuladas'][i])
##                    sigma = np.sqrt(sigma)
                    res.at[index, 'Geometria'] = df['Geometria'][i-1]
                    res.at[index, 'Material'] = df['Material'][i-1]
                    res.at[index, 'Seed1'] = df['Seed1'][i-1]
                    res.at[index, 'Seed2'] = df['Seed2'][i-1]
                    res.at[index, 'Energy(eV)'] = df['Energy(eV)'][i-1]
                    res.at[index, 'Cobre'] = df['Cobre'][i-1]
                    res.at[index, 'Historias'] = N[j]
                    res.at[index, 'Campo'] = df['Campo'][i-1]
                    #res.at[index, 'HVL(mmAl)'] = df['HVL(mmAl)'][i-1]
                    #res.at[index, 'EnergiaMedia'] = df['EnergiaMedia'][i-1]
                    #res.at[index, 'Rendimento'] = df['Rendimento'][i-1]
                    
                    
                    res.at[index, tipo[j]] =  q
                    res.at[index, 'Erro '+ tipo[j]] =  q2
                    

##                    print( df['Energy(eV)'][i],df['Energy(eV)'][i-1],sum1[j], sum2[j], N[j])
                    ##
                    index += 1
                    sum1[j] = df[tipo[j]][i]*df['Simuladas'][i]
                    sum2[j] = (df['Erro '+ tipo[j]][i]**2)*(df['Simuladas'][i])**2
                    N[j] = df['Simuladas'][i]

##                    print(i)

                
##                    break
##            print(sum1[0])
    
        
res.to_csv('dataframe_mono_pmma.csv',  index = None)
