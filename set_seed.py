###################Set seeds files#############

def create_seed(seed1,seed2,processor_number):
    file = open(str(processor_number)+'/seed.dt','w')
    file.write(str(int(seed1))+' '+str(int(seed2)))
    file.close()

    
