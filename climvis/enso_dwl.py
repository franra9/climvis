"""this script downloads needed SST data to computo el niño index"""

# import libraries 
import cdsapi

#fyear = 2019
#smonth = 12
#region = "en34"# en3 en 34, en 4[False, False, True, False]

def dwl_era5_enso(fyear, region):
    """Download ERA5 SST data for ENSO regions

    Parameters
    ----------
    syear : integer
        lest year of the period
    region : string
        String indicating the "el niño" region. 
        It must be "en12" (El niño 1+2),"en3" (El niño 3),"en34" (El niño 3.4),
        or "en4" (El niño 4).

    Returns
    -------
    downloads the requested files in the working directory
    """

    c = cdsapi.Client()

    #to be faster, resolution is reduced
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
    year = ['{}'.format(y) for y in range(int(fyear) - 20, int(fyear) + 1)]
    
    # 12 months before our month
    #months = np.arange(smonth - 12, smonth + 1) % 13
    #months = months[months != 0]
    
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
            
#dwl_era5_enso(fyear, region)