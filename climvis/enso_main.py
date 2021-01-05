import enso_dwl
import enso_functions
import numpy as np

smonth = 4
fmonth = 3
syear = 1980
fyear = 1984
region = "en12"
filein = 'ERA5_Monthly_sst_' + str(fyear) + '_'+ region + '.nc'
  

enso_dwl.dwl_era5_enso(fyear, region)
clim = enso_functions.clim(filein)
ano1 = enso_functions.yearly_evol(clim, filein, syear, fyear, smonth, fmonth)
ano1.plot()

smonth = 4
fmonth = 3
syear = 2005
fyear = 2010 
region = "en2"
filein = 'ERA5_Monthly_sst_' + str(fyear) + '_'+ region + '.nc'
  

enso_dwl.dwl_era5_enso(fyear, region)
clim = enso_functions.clim(filein)
ano2 = enso_functions.yearly_evol(clim, filein, syear, fyear, smonth, fmonth)
ano2.plot()

pearson = np.corrcoef(ano1, ano2)[0, 1]
print(pearson)

