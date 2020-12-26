"""This configuration module is a container for parameters and constants."""
import os
import sys

def data(cru_dir):
    f = open(cru_dir + "/.climvis", "r")
    file_str = f.read().splitlines() #to get rid of \n
    file_path = "".join(file_str)
    return cru_dir + file_path
    
#cru_dir = '/home/francesc/data/climvis/'
cru_dir = os.path.expanduser(path="~")
cru_dir1 = data(cru_dir)

cru_tmp_file = cru_dir1 + 'cru_ts4.03.1901.2018.tmp.dat.nc'
cru_pre_file = cru_dir1 + 'cru_ts4.03.1901.2018.pre.dat.nc'
cru_topo_file = cru_dir1 + 'cru_cl1_topography.nc'

file_path = [cru_tmp_file, cru_pre_file, cru_topo_file]

for a in file_path:
    # exits the program 
    if not os.path.exists(a):
        sys.exit('The CRU files are not available on this system. For cruvis'\
                 '(part of the climvis package) to work properly, please'\
                 'create a file called ".climvis" in your HOME directory,'\
                 'and indicate the path to the CRU directory in it.')    
    
bdir = os.path.dirname(__file__)
html_tpl = os.path.join(bdir, 'data', 'template.html')
world_cities = os.path.join(bdir, 'data', 'world_cities.csv')

default_zoom = 8

