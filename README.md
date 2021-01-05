# era5vis, a climate visualization package, 

**era5vis** is a package based on [**climvis**](https://fabienmaussion.info/scientific_programming/week_08/02-ClimVis.html), which at the same time is based on [scispack](https://github.com/fmaussion/scispack). It offers a visualization interface where, for a given period and location, two variables can be compared. The climvis features are also included.

It was written as the first project of the Scientific Programming course at the University of Innsbruck, modifying the course template, by: Gorosti Mancho, Marie Schroeder and Francesc Roura. 

## Data
All data comes from the ERS-5 reanalysis and it is taken from [here](https://cds.climate.copernicus.eu/#!/home). Read carefully the intructions to be able to download the data using the [cdsapi](https://pypi.org/project/cdsapi/) package. It requires to sign in in the CDS system and to create a hidden file where the credentials can be read.

## HowTo

Make sure you have all dependencies installed. These are:
- numpy
- pandas
- xarray
- motionless
- matplotlib
- warnings
- cdsapi

Download the package and install it development mode. From the root directory,
do:

    $ pip install -e .

If you are on a university computer, you should use:

    $ pip install --user -e .

## Command line interface

### Define data directory:
Type 


    $ era5vis -s

anywhere in the directory tree. Then the path to the data directory is requiered.
### era5vis interface
Run the interface.py script by 

    $ python interface.py
and the interface will pop-up. Now you are ready to use it.

An initial date, final date, location and two variables to be compared are requiered. The data has to be downloaded, and once downloaded, a "Make plot" button will appear.
A map concerning the "el niño" regions is shown for clarity.
### Some notes about el Niño computation
- The reference sea surface temperature (sst) is comuted every time as a monthly average over the prior 20 years.
- The period to be shown when choosing a "el niño" index is limited to the same lenght as the period used to compute the climatology, i.e. 20 years.

### cruvis information
To get information about the cruvis package, type:

    $ cruvis --help

## Testing

The package is meant to be teasted using [pytest](https://docs.pytest.org). To test
the package, do:

    $ pytest .

From the package root directory.


## License

With the exception of the ``setup.py`` file which was adapted from the
[sampleproject](https://github.com/pypa/sampleproject) package, all the
code in this repository is dedicated to the public domain.
