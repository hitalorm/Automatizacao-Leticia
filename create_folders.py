import os
import sys
import shutil
##import create_geo

def check_folder(processor_number):
    folder_exist = os.path.isdir(str(processor_number))
    if folder_exist == False:
        os.makedirs(str(processor_number))

def check_geometry(geo_name, processor_number):
    file_exist = os.path.isfile(str(processor_number)+'/'+str(geo_name))
    if file_exist == False:
        file_exist2 = os.path.isfile('geometries/'+str(geo_name))
        if file_exist2 == True:
            shutil.copy('geometries/'+str(geo_name), str(processor_number))
        #else:
        #    create_geo.create_geometry_file(thick, geo_name)
        #    shutil.copy('geometries/'+str(geo_name), str(processor_number))

def check_materials(material_name, processor_number):
    file_exist = os.path.isfile(str(processor_number)+'/'+str(material_name))
    if file_exist == False:
        shutil.copy('materials/'+str(material_name), str(processor_number))
        


def check_in(processor_number):
    material_name = 'pediatria.in'
    file_exist = os.path.isfile(str(processor_number)+'/'+str(material_name))
    if file_exist == False:
        shutil.copy(str(material_name), str(processor_number))
        

def check_exe(processor_number, exe):
    material_name = exe
    file_exist = os.path.isfile(str(processor_number)+'/'+str(material_name))
    if file_exist == False:
        shutil.copy(str(material_name), str(processor_number))

def check_bat(processor_number, exe):
    material_name = exe
    file_exist = os.path.isfile(str(processor_number)+'/'+str(material_name))
    if file_exist == False:
        shutil.copy(str(material_name), str(processor_number))
    
    
for i in range(9):
    check_folder(i)
