# Creating Beautiful Geospatial Data Visualisations with Python 
 
Presented by Dr. Adam Symington (PythonMaps)

This repository contains all the material needed by students registered for the "Creating Beautiful Geospatial Data Visualisations with Python" tutorial at SciPy 2022 on 12th July 2022.

For a smooth experience, you will need to make sure that you install or update your Python distribution and download the tutorial material before the day of the tutorial. Furthermore, there are a number of data sources (listed below) required for the tutorial. These will need to be downloaded and placed in the resources folder ahead of time.

## Download Tutorial Materials

This GitHub repository is all that is needed in terms of tutorial content. The simplest solution is to download the material using this link:

https://github.com/symmy596/PythonMaps-Scipy-2022/archive/refs/heads/master.zip

If you are familiar with Git, you can also clone this repository with:

```
$ git clone https://github.com/symmy596/PythonMaps-Scipy-2022.git
```

It will create a new folder named `PythonMaps-Scipy-2022` with all the content you will need.

There are a number of datasets required for these tutorials. These will need to all be downloaded prior to the tutorial and placed in the resources folder.


#### Tutorial 1 Points and Lines

- [World Port Index (WPI)](https://msi.nga.mil/Publications/WPI)
- [Open Flights](https://openflights.org/data.html)

#### Tutorial 2 Polygons

- [Natural Earth](https://www.naturalearthdata.com/)

#### Tutorial 3 Rasters

- [Forests](https://globalmaps.github.io/ptc.html)
- [NASA](https://neo.gsfc.nasa.gov/)

#### Tutorial 4 Rasters and Shapes

- [Topography](https://www.ngdc.noaa.gov/mgg/global/relief/ETOPO1/data/bedrock/grid_registered/georeferenced_tiff/)
- [River Basins](https://www.hydrosheds.org/products/hydrobasins)


### Install Packages

To be able to run the examples, demos and exercises, you must have the following packages installed:

The following libraries are required to run the workshop

- geopandas==0.10.2
- pandas==1.4.2
- numpy==1.21.5
- shapely==1.8.0
- matplotlib==3.5.1
- cartopy==0.20.2
- rasterio==1.2.10
- rioxarray==0.11.1

If you are using Anaconda, you can use the Anaconda Prompt (Windows) or Terminal.app (macOS) to create an environment with the necessary packages:

1. Open the Anaconda Prompt or Terminal.app using the below instructions:
    - **Windows**: Click Start and search for "Anaconda Prompt". Click on the application to launch a new Anaconda Prompt window.
    - **macOS**: Open Spotlight Search (using Cmd+Space) and type "Terminal.app". Click on the application to launch a new Terminal.app window.   

2. Create a new Anaconda virtual environment by executing the below command in the application window you opened in step 1 above.

    ```
    $ conda create -n pythonmaps-tutorial jupyter geopandas==0.10.2 pandas==1.4.2 numpy==1.21.5 shapely==1.8.0 matplotlib==3.5.1 cartopy==0.20.2 rasterio==1.2.10 rioxarray==0.11.1
    ```

3. To test your installation, please execute the `check_env.py` script in the environment where you have installed the requirements. If you created an Anaconda environment using the instructions above, keep the application window that you opened in step 1 active (or launch the platform specific application again -- Anaconda Prompt for Windows or Terminal.app for macOS), navigate to where you have this GitHub repository, and type:

    ```
    $ conda activate numpy-tutorial
    $ python check_env.py
    ```

You should see a window pop up with a plot that looks vaguely like a smiley face.