"""this script downloads needed SST data to computo el niño index"""

import xarray as xr  # netCDF library
filein = 'ERA5_Monthly_sst_2018_enso34.nc'
month = 10

def clim(filein):
    """Returns monthly climatology for a given region.

    Parameters
    ----------
    filein: netcdf file
        original monthly data

    Returns
    -------
    xarray Dataset
        monthly mean sst values from the netcdf
    """
    #filein = 'ERA5_Monthly_sst_2018_enso34.nc'
    #xr.open_dataset('./ERA5_Monthly_sst_2020_enso34.nc')
    data = xr.open_dataset(filein)
    mo_data = data.groupby('time.month').mean()
    mean_data = mo_data.mean(dim = ['latitude', 'longitude'])
    
    return mean_data    

def yearly_evol(clim, filein, month):
    """Returns monthly climatology for a given region.

    Parameters
    ----------
    clim: xarray Dataset 
        monthly climatology

    filein: netcdf file       
        original monthly data 
        
    month: integer
        month of study    
    
    Returns
    -------
    xarray Dataset
        monthly mean sst anomalies during a 12-month period
    """
    data = xr.open_dataset(filein)
    region_mean = data.mean(dim = ['latitude', 'longitude'])
    
    # 12 previous months
    l_pos = region_mean.sst.size - (12 - month) #last position #i don't like indexinf in python
    i_pos = l_pos - 12 
    month12 = region_mean.sst[i_pos : l_pos]
    
    #compute anomaly
    ano = month12 - clim
    
    return ano
    
clim = clim(filein)
ano = yearly_evol(clim, filein, month)
    
    
    
    