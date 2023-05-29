######This section copies opens the .ini file and extract informations#############
import re
import math
import shutil

def open_ini(filename):
    file = open(filename, 'r')
    buffer = file.read()
    file.close()
    return buffer
    
def set_config(buffer,time,update):
    time_string ='\n '+str("{0:.1e}".format(time))+'           NUMBER OF HISTORIES'
    buffer = re.sub('\n (.*?)NUMBER OF HISTORIES',time_string,buffer)
    update_string = '\n '+str("{0:.1f}".format(update))+'             UPDATE INTERVAL'
    buffer = re.sub('\n (.*?)UPDATE INTERVAL', update_string, buffer)
    return buffer


def set_particle_position(buffer,new_z):
    new_coordinates = '0.0 0.0 -'+str("{0:.1f}".format(new_z))+'                  POINT FOCAL SPOT COORDINATES (cm)'
    buffer = re.sub('0.0 0.0(.*?)POINT FOCAL SPOT COORDINATES \(cm\)',new_coordinates,buffer)
    return buffer

def set_particle_angle(buffer, new_z, radius_x, radius_y):
    #radius = 5.641895835
    angle_x = math.atan(radius_x/new_z)
    angle_x = angle_x*180/math.pi
    angle_x = round(angle_x,2)

    angle_y = math.atan(radius_y/new_z)
    angle_y = angle_y*180/math.pi
    angle_y = round(angle_y,2)

    new_angle = ' ' + str("{0:.2f}".format(angle_x)) +'  '+str("{0:.2f}".format(angle_y))+'  0.0               POLAR AND AZIMUTHAL APERTURE AND TILT ANGLE [deg]'
    buffer = re.sub('(.*?)  (.*?)  0.0               POLAR AND AZIMUTHAL APERTURE AND TILT ANGLE \[deg\]',new_angle,buffer)
    return buffer



def set_particle_energy(buffer, energy):
    energy = round(energy,2)
    new_energy = str("{0:.3e}".format(energy))+'      1.0              Spectrum table'
    buffer = re.sub('(\d\.\d\d\de\+\d\d)      1.0              Spectrum table', new_energy,buffer)
    new_energy2 = str("{0:.3e}".format(energy))+'      -1               Enter a negative'
    buffer = re.sub('(\d\.\d\d\de\+\d\d)      -1               Enter a negative',new_energy2,buffer)
    return buffer

def set_particle_energy_rect(filename,energy):
    file = open(filename[:2] + '/energy_spectra.dat','w')
    file.write('1 360.0\n')
    energy = round(energy,2)
    file.write(str("{0:.3e}".format(energy)) +'       1.0\n')
    file.write(str("{0:.3e}".format(energy)) +'        -1\n')
    file.close()

def set_particle_poly(filename, espectro, cobre):
    shutil.copy('Espectros/' + str(cobre) +'/' + str(int(espectro)) + 'kV.dat',filename[:2]+'energy_spectra.dat') 

def set_geometry(buffer, name_geo):
    string ='\n '+name_geo
    buffer = re.sub('\n (.*?).geo', string,buffer)
    return buffer

def set_material(buffer, material,pos):
    if len(pos) == 1:
      string = '\n  '+pos+'   '+material
      buffer = re.sub('\n  '+pos+'   (.*?).mat', string, buffer)
    else:
      string = '\n '+pos+'   '+material
      buffer = re.sub('\n '+pos+'   (.*?).mat', string, buffer)
    return buffer

def set_gland_proportion(buffer, proportion):
    proportion_string = ('\n '+str("{0:.2f}".format(proportion))+'							 GLANDULAR')
    buffer = re.sub('\n (\d\.\d\d)							 GLANDULAR', proportion_string, buffer)
    return buffer

def write_file(buffer, filename):
    file = open(filename, 'w')
    file.write(buffer)
    file.close()

def set_seed(buffer, seed1, seed2):
    string = '\n ' + str(seed1)+ '  ' + str(seed2) + '              INITIAL RANDOM SEEDS'
    buffer = re.sub('\n (.*?)INITIAL RANDOM SEEDS', string, buffer)
    return buffer

def set_in(filename, hist, update, energy, material, mat_id, name_geo, seed1,seed2):
    buffer = open_ini(filename)
    buffer = set_config(buffer, hist, update)
    buffer = set_geometry(buffer, name_geo)
    buffer = set_seed(buffer, seed1, seed2)
    buffer = set_material(buffer, material,mat_id)
    buffer = set_particle_energy(buffer, energy)
    write_file(buffer, filename)    

    
    
