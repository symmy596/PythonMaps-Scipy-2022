import rasterio
import matplotlib
import shapely
import pandas as pd
import geopandas as gpd
import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import rioxarray as rxr

fig, ax = plt.subplots()
ax.scatter(x=[-3, -2, -1, 0, 1, 2, 3], y=[0, -1, -1.5, -1.75, -1.5, -1, 0])
ax.scatter(x=[-1.5, 1.5], y=[2, 2], s=1000)
ax.set_ylim((-3, 3))
plt.show()