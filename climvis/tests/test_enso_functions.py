# Testing el niño functions
# Author: Francesc Roura Adserias

import climvis.enso_functions as cl
import xarray as xr
import numpy as np
import pytest

# Test clim output
def test_clim():
    # Check that the output given a test netCDF is a xr.Dataset of length 12
    climate = cl.clim("testfile.nc")
    assert type(climate) == xr.Dataset
    assert len(np.array(climate.sst)) == 12
   
# Test yearly_evol for different known prebuilt cases
def test_evol():
    climate = cl.clim("testfile.nc")
    
    # check that output length is consistent
    ano1 = cl.yearly_evol(climate, "testfile.nc", 1998, 2000, 12, 2)
    ano2 = cl.yearly_evol(climate, "testfile.nc", 1999, 2000, 2, 12)
    ano3 = cl.yearly_evol(climate, "testfile.nc", 2000, 2000, 1, 2)
    assert len(np.array(ano1)) == 15 #((2000 - 1998 - 1) * 12 + 3)
    assert len(np.array(ano2)) == 23
    assert len(np.array(ano3)) == 2
    
    # check that an error is issued when wrong period is entered
    with pytest.raises(ValueError):
        cl.yearly_evol(climate, "testfile.nc", 2000, 1999, 2, 1)

    