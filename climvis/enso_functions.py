"""this script downloads needed SST data to computo el niño index"""

import xarray as xr  # netCDF library
import numpy as np
#import datetime
import pandas as pd

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

def yearly_evol(clim, filein, syear, fyear, smonth, fmonth):
    """Returns monthly climatology for a given region.

    Parameters
    ----------
    clim: xarray Dataset 
        monthly climatology.

    filein: netcdf file       
        original monthly data.

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
    data = xr.open_dataset(filein)
    region_mean = data.mean(dim = ['latitude', 'longitude'])
    period = slice(str(syear) + '-' + str(smonth) + '-01',
             str(fyear) + '-' + str(fmonth) + '-01')
  
    data_period = region_mean.sst.sel(time=period)
    data_period.size
    
    npclim = np.array(clim.sst)
    headclim =  npclim[(smonth - 1):12] #i hate python indexing
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

    #compute anomaly
    ano = data_period - totclim
    
    return ano
 
def corr(serie1, serie2): #maybe verbose, not useful
    """Returns pearson correlation parameter between 2 dataseries.

    Parameters
    ----------
    serie1, serie2: equal-length np.arrays or lists.
        data series to be compared.
    
    Returns
    -------
    float
        pearson correlaion parameter
    """
    if len(serie1) != len(serie2):
        raise ValueError('Both serie must have equal length.')
        
    pearson = np.corrcoef(serie1, serie2)[0, 1]
    
    return pearson
    
    
#filein = 'ERA5_Monthly_sst_2019_en34.nc'
#smonth = 10
#fmonth = 2
#syear = 2000
#fyear =2015   
#clim = clim(filein)
#ano = yearly_evol(clim, filein, syear, fyear, smonth, fmonth)
#clim = clim(filein)
#ano = yearly_evol(clim, filein, month)