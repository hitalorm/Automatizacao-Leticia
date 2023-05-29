import regex as re
import os
import pandas as pd
def make_buffer(filename):
    file = open(filename, 'r')
    buffer = file.read()
    file.close()
    return buffer

def get_simulation_end(buffer):
    string = 'Have a nice day.'
    end = re.search(string, buffer)
    if end==None:
        return False
    else:
        return True
def get_last_seeds(buffer):
    string = 'Last random seeds:\n (\d*?) (\d*?)\n' 
    seeds = re.search(string, buffer)
    seed1 = seeds.group(1)
    seed2 = seeds.group(2)
    return int(seed1),int(seed2)

def pick_result(buffer2, dado):
    string = str(dado)+'  (\d.\d\d\d\d\dE.\d\d)  (\d.\d\d\d\d\dE.\d\d)'
    values = re.search(string,buffer2)
    energy_depos_1 = float(values.group(1))
    error_1 = float(values.group(2))
    return energy_depos_1

def pick_error(buffer2, dado):
    string = str(dado) +'  (\d.\d\d\d\d\dE.\d\d)  (\d.\d\d\d\d\dE.\d\d)'
    values = re.search(string,buffer2)
    energy_depos_1 = float(values.group(1))
    error_1 = float(values.group(2))
    return error_1

def pick_pp(buffer3):
    string = '2  (\d.\d\d\d\d\d\E.\d\d)  (\d.\d\d\d\d\d\E.\d\d)(.*?)(\d*?)\n'
    values = re.search(string,buffer3)
    energy_depos_pp = float(values.group(1))
    error_pp = float(values.group(2))
    hist_pp = int(values.group(4))
    return [energy_depos_pp, error_pp]

def pick_time(buffer2):
    string = 'CPU time \[t\] \(s\):\n#(.*?)(\d.\d\d\d\d\d\E\+\d\d)\n'
    values = re.search(string,buffer2)
    time = float(values.group(2))
    string = 'Speed \(histories/s\):\n#(.*?)(\d.\d\d\d\d\d\E\+\d\d)\n'
    values = re.search(string,buffer2)
    vel = float(values.group(2))
    return [time, vel]

def pick_hist(buffer2):
    string = 'No. of histories simulated \[N\]:\n#(.*?)(\d*?).\n'
    values = re.search(string, buffer2)
    hist = int(values.group(2))
    
    return hist
def get_out(filename,dados):
    buffer2 = make_buffer(filename+'/tallyEnergyDeposition.dat')
    results = [0 for i in range(dados)]
    error = [0 for i in range(dados)]
    
    for i in range(dados):
        hist = pick_hist(buffer2)
        results[i] = pick_result(buffer2, i+1)                
        error[i] = pick_error(buffer2,i+1)
        
    return results, error, hist


