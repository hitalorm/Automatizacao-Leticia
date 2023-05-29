import re

def load_config():
    file = open('general.cfg', 'r')
    buffer=file.read()
    file.close()
    temp = re.search('Number_processors:(.*?);',buffer)
    number_processors = int(temp.group(1))
    temp = re.search('Time_run:(.*?);',buffer)
    time_run = int(temp.group(1))
    
    return number_processors, time_run
    

