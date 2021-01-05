# Testing el niño download functions
# Author: Francesc Roura Adserias

import climvis.enso_dwl as cl
import os
import pytest

# dummy download
region = ["en12", "en3", "en34", "en4"]

def test_enso_dwl():

    # Check that dowload works for every enso region:
    for re in region:
        cl.dwl_era5_enso(2000, re)
        print(re)
        filein = 'ERA5_Monthly_sst_2000_'+ re + '.nc'
        assert os.path.exists(filein) 
    
    # Check ValueErrors rise correctly 
    with pytest.raises(ValueError, 
                match = 'Arg "region" must be: "en12","en3","en34" or "en4".'):
        cl.dwl_era5_enso(2000, "nao")
    with pytest.raises(ValueError, 
            match = 'Final year must be in the 1979-2019 period.'):
        cl.dwl_era5_enso(1714, "en12")

    