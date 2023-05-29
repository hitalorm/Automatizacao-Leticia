###################################################################
#PenEasy auto######################################################
###Automation for penEasy simulations##############################
import numpy as np
import os
import sys
import pickle 
from create_dat import *
from load_config import *
import pandas as pd
#import create_folders
import set_in
import set_seed
import subprocess
import time
import get_out
#import calc_kerma
from timer import *
#import calc_kerma_poli
#import calc_hvl
import platform
import shutil

material_list = ['air.mat', 'skin.mat', 'water.mat', 'selenium.mat', 'pmma.mat', 'adipose.mat', 'calcification.mat',
                 'grid.mat', 'lesion.mat']
tables_list = ['adipose_inc.txt', 'adipose_photo.txt', 'glandular_inc.txt', 'glandular_photo.txt', 'interstrip_table.txt', 'strip_table.txt']

#detect OS
OS = platform.system()
if OS=='Windows':
    exe = 'penEasy.exe'
else:
    exe = 'penEasy.run'


initial_dir = os.getcwd()


teste1 = input('Criar arquivo dataframe.csv? \n (y/n):   ')

if teste1 == 'y':
    create_dat()

data_exist = os.path.isfile('parameters.dat')

if data_exist == False:
    teste=input('No parameters.dat file found, create a new one?'
                'digite y para criar')
    if teste=='y':
        create_dat()
    else:
        print("No File Create, exiting")

else:
    
    print('\nLoading Config Files')
    number_processors, time_run = load_config()
    print('Number of processors is set to:', number_processors)
    print('Time in seconds per run is set to: ',time_run)
    print('Loading checkpoint file')
    stack = np.loadtxt('checkpoint.dat',dtype=int)
    stack_save = np.loadtxt('checkpoint.dat',dtype=int)
        
    
    print('Checkpoint is ', stack[0])
    print('Loading Parameters')
    #ile = open('parameters.dat','rb')
    parameters = pd.read_csv('dataframe.csv', names = None)
    #file.close()
    #df = pd.read_pickle('dataframe.csv')
    print('Parameters Loaded')
    total_len = len(parameters)
    time_min = (total_len-stack[0])*time_run/(60*number_processors)
    print('Estimated time remaining to complete the simulation (min): ', time_min)
    print('Starting Simulation')
##    np.random.seed(106171910)
    p_vec = np.zeros(number_processors,dtype=object)
    stack_temp = np.zeros(number_processors,dtype=int)
    processor_order = []
    avaiable_processors = np.arange(0,number_processors,dtype=int)
    finished = False
    counter_backup = 0
    while finished==False:
        
        while len(avaiable_processors)>0 and len(stack)>0:            
            print('\n')
            print('simulation number '+str(stack[0]+1)+' of', len(parameters))
            j = avaiable_processors[0]
            avaiable_processors= avaiable_processors[1:]
            i = stack[0]
            os.chdir(initial_dir)
            #create_folders.check_folder(j)

            print('\n')
            print('Histórias: ',parameters['Historias'].iloc[i])
            print('Energia: ',parameters['Energy(eV)'].iloc[i])
            print('Material: ',parameters['Material'].iloc[i])
            print('Geometria: ',parameters['Geometria'].iloc[i])
            print('\n')
            
            
            set_in.set_in(str(j) + '/penEasy.in', parameters['Historias'].iloc[i], 60, parameters['Energy(eV)'].iloc[i],
                          parameters['Material'].iloc[i],'1', parameters['Geometria'].iloc[i], 
                          parameters['Seed1'].iloc[i], parameters['Seed2'].iloc[i])


            os.chdir(str(j))
            if OS =='Windows':
                p = subprocess.Popen('penEasy.exe<penEasy.in>res.out', shell=True)
            else:
                directory = os.getcwd()
                p = subprocess.Popen('./penEasy.x<penEasy.in>res.out', cwd = directory, shell=True)
            p._internal_poll(_deadstate=127)
            p_vec[j] = p
            stack_temp[j] = stack[0]
            stack = stack[1:]

        time.sleep(5)
            
        for idx,p in enumerate(p_vec):
            if p!=0:
                signal = p.poll()
                if signal !=None:
                    time.sleep(1)
                    index = stack_temp[idx]
                    counter_backup+=1

                    
                        
                    
                    os.chdir(initial_dir)
                    
                    if counter_backup==10:
                        shutil.copyfile('dataframe.csv', 'dataframe_backup.dat')
                        shutil.copyfile('checkpoint.dat', 'checkpoint_backup.dat')

                        counter_backup=0
                    
                    results, error, hist, = get_out.get_out(str(idx),2)

                    #EABS == Energia Absorvida
                    parameters.at[index, 'EABS'] = results[0]
                    parameters.at[index, 'Erro EABS'] = error[0]/2
                    parameters.at[index, 'Simuladas'] = hist
                    
                    
                    new_name = 'v1/'+str(int(parameters['Energy(eV)'].iloc[index]/1000))+ '-' + parameters['Material'].iloc[index] + '.dat'
                    os.rename(str(idx)+'/tallyPixelImageDetectEI-matrix.dat', new_name)
                    
                    try:
                        os.remove(str(idx) + '/tallyEnergyDepositionPP.dat')
                        os.remove(str(idx) + '/tallyEnergyDeposition.dat')
                        os.remove(str(idx)+'/tallyPixelImageDetectEI-matrix.dat')
                    
                    except OSError:
                        pass
                    
                    
                    print('COLLECTING RESULTS')



                    print(parameters.loc[index])
                    print('SAVING RESULTS')
                    parameters.to_csv('dataframe.csv', index = None)
                    
                    index_save = np.where(stack_save==index)
                    stack_save[index_save] = -1

                    stack_save=stack_save[stack_save!=-1]
                    
                    try:
                        np.savetxt('checkpoint.dat', stack_save, '%05d')
                    except:
                        time.sleep(2)
                        np.savetxt('checkpoint.dat', stack_save, '%05d')
                    print('RESULTS SAVED')

                    #del p[idx]
                    avaiable_processors = np.append(avaiable_processors,idx)
                    p_vec[idx] = 0

                    

                


        if len(stack)==0 and len(avaiable_processors)==number_processors:
            finished = True
                
        
        
                  
            
            
        
        
            
            
            

            
                          
                          
            
            
        
        
                


                
                
