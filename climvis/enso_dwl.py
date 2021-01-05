"""This script downloads needed sea surface temperature (SST) data from CDS 
(https://cds.climate.copernicus.eu/) to compute el niño index"""

# Import libraries 
import cdsapi
import warnings

def dwl_era5_enso(fyear, region):
    """Download ERA5 SST data for one of the 4 El Niño regions for the 20 
    years before the given year (fyear).
    
    Author: Francesc Roura Adserias
    
    Parameters
    ----------
    fyear : integer
        last year of the 20-year period.
    region : string
        String indicating the "el niño" region. 
        It must be "en12" (El niño 1+2),"en3" (El niño 3),"en34" (El niño 3.4),
        or "en4" (El niño 4).

    Returns
    -------
    Downloads the requested files in the working directory
    """
    if fyear > 2019 or fyear < 1979:
        raise ValueError('Final year must be in the 1979-2019 period.')

    c = cdsapi.Client()

    # To be faster, resolution is reduced
    grid = [1, 1] 

    # el niño 1+2
    if region == "en12":
        area = [0, -90, -10, -80]
    # el niño 3
    elif region == "en3":    
        area = [5, -150, -5, -90]
    # el niño 3.4
    elif region == "en34":
        area = [5, -170, -5, -120]
    # el niño 3.4
    elif region == "en4":
        area = [5, 160, -5, -150]
    else:
        raise ValueError('Arg "region" must be: "en12","en3","en34" or "en4".')

    # 20-year period, monthly data
    if fyear - 20 < 1979: # no data before 1979
        year = ['{}'.format(y) for y in range(int(fyear) - 20, 
                                            int(fyear + fyear + 20 -1979) + 1)]
        warnings.warn("Climatology computed from 1979 to 1999.")
    else:
        year = ['{}'.format(y) for y in range(int(fyear) - 20, int(fyear) + 1)]
    
    # All months
    month = ['{:02d}'.format(m) for m in range(1, 13)]
    
    c.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'format':'netcdf',
            'product_type':'monthly_averaged_reanalysis',
            'variable':[
                'sea_surface_temperature',
                ],
            'grid': grid,
            'area': area,
            'year': year,
            'month': month,
            'time':'00:00'
            }, 
        'ERA5_Monthly_sst_' + str(fyear) + '_' + region + '.nc')