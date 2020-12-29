"""this script downloads needed SST data to computo el niño index"""

# import libraries 
import cdsapi

syear = 2018
#smonth = 12
region = [False, False, True, False]

def dwl_era5_enso(syear, region):
    """Download ERA5 SST data for ENSO regions

    Parameters
    ----------
    syear : integer
        Year of study
    #smonth : integer
    #    The number of the month of study (1=Jan, 12=Dec)
    region : boolean list
        A list of 4 boolean representing studied ENSO regions [nino 1+2, 
        nino 3, nino 3.4, nino 4]

    Returns
    -------
    downloads the requested files in the working directory
    """

    c = cdsapi.Client()

    #dl_dir='/home/francesc/'

    #to be faster, resolution is reduced
    grid = [1, 1] 

    # el niño 1+2
    area12 = [0, -90, -10, -80]
    # el niño 3
    area3 = [5, -150, -5, -90]
    # el niño 3.4
    area34 = [5, -170, -5, -120]
    # el niño 4
    area4 = [5, 160, -5, -150]

    # 10-year period, monthly data
    year = ['{}'.format(y) for y in range(syear - 10, syear + 1)]
    
    # 12 months before our month
    #months = np.arange(smonth - 12, smonth + 1) % 13
    #months = months[months != 0]
    
    month = ['{:02d}'.format(m) for m in range(1, 13)]
    
    if region[2]:
        c.retrieve(
            'reanalysis-era5-single-levels-monthly-means',
            {
                'format':'netcdf',
                'product_type':'monthly_averaged_reanalysis',
                'variable':[
                    'sea_surface_temperature',
                    ],
                'grid': grid,
                'area': area34,
                'year': year,
                'month': month,
                'time':'00:00'
                }, 
            'ERA5_Monthly_sst_' + str(syear) + '_enso34' + '.nc')
            #dl_dir + 'ERA5_LowRes_Monthly_sst.nc')
            
dwl_era5_enso(syear, region)