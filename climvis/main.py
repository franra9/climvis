import enso_dwl
import enso_functions


region = "en4"
filein = 'ERA5_Monthly_sst_2015_'+ region + '.nc'
smonth = 1
fmonth = 12
syear = 1996
fyear = 2015   

enso_dwl.dwl_era5_enso(fyear, region)
clim = enso_functions.clim(filein)
ano = enso_functions.yearly_evol(clim, filein, syear, fyear, smonth, fmonth)
ano.plot()


