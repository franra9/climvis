"""this script plots el niño index"""
#import xarray as xr
#import matplotlib.pyplot as plt

def plot_nino(ano):#, month):
    """Returns monthly climatology for a given region.
    Parameters
    ----------
    ano: xarray DataArray 
        monthly sst anomalies from a 12-month period prior to our month
    
    month: integer
        month of study 
    """
    ano.plot()