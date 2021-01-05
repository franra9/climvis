"""This script downloads needed sea surface temperature SST data to compute 
el niño index"""

import xarray as xr  # netCDF library
import numpy as np
import os
import datetime

def clim(filein):
    """Returns monthly climatology for a given region.
    
    Author: Francesc Roura Adserias
    
    Parameters
    ----------
    filein: netcdf file
        original monthly sea surface temperature (sst) data for a given region 
        and period.

    Returns
    -------
    xarray Dataset
        Sea surface temperature (sst) monthly clmatology.
    """
    # Open data
    data = xr.open_dataset(filein)
    
    # Check that data exists
    if not os.path.exists(filein):
        raise ValueError("The file" + filein + "does not exist.")
    
    # Compute regional-monthly mean
    mo_data = data.groupby('time.month').mean()
    mean_data = mo_data.mean(dim = ['latitude', 'longitude'])
    
    return mean_data    

def yearly_evol(clim, filein, syear, fyear, smonth, fmonth):
    """Returns monthly anomalies for a given region and a given monthly 
    climatology.
    
    Author: Francesc Roura Adserias
    
    Parameters
    ----------
    clim: xarray Dataset 
        monthly climatology.

    filein: netcdf file       
        original monthly-mean data.

    syear: integer
        first year of the period of study.

    smonth: integer
        first month of the period of study.   
    
    fyear: integer
        final year of the period of study.
        
    fmonth: integer
        last month of the period of study.    

    Returns
    -------
    xarray Dataset
        monthly mean sst anomalies during a 12-month period.
    """
    # Check imput dates 
    if (fyear - syear) > 20:
        raise ValueError("Period of study can not exceed the climtology period (20 years).")
    
    if datetime.datetime(syear, smonth, 1) >= datetime.datetime(fyear, fmonth, 1):
        raise ValueError("Non-consistent start and final dates.")

    data = xr.open_dataset(filein)
    
    # Spatial mean for the study period
    region_mean = data.mean(dim = ['latitude', 'longitude'])
    period = slice(str(syear) + '-' + str(smonth) + '-01',
             str(fyear) + '-' + str(fmonth) + '-01')
    
    data_period = region_mean.sst.sel(time = period)
    
    # Compare climatology to our period.    
    npclim = np.array(clim.sst)
    headclim =  npclim[(smonth - 1):12]
    if (fyear - syear) == 0:
        midclim = None
    else:
        midclim = np.repeat(npclim, fyear - syear - 1)
    tailclim = npclim[0:fmonth]
    
    if fyear == syear: #only one year
        totclim = npclim[(smonth -1):fmonth]
    else:
        if fmonth == 12: #last year is complete
            totclim = np.concatenate((headclim, midclim))
        if smonth == 1: #first year is complete
            totclim = np.concatenate((midclim, tailclim))
        if smonth == 1 & fmonth == 12:
            totclim = midclim
        else:
            totclim = np.concatenate((headclim, midclim, tailclim))

    # Compute anomaly
    ano = data_period - totclim
    
    return ano