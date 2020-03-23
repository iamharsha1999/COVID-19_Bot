import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns
import geopandas as gpd


## Initialize the Visualization
sns.set(style = 'whitegrid', palette = 'dark', color_codes = True)
my_dpi = 96
figsize = (1080/my_dpi,1080/my_dpi)
pylab.rcParams['figure.figsize'] = figsize

## Read the Shape Files
shp_path = 'Indian_States.shp'
sdf = gpd.read_file(shp_path)
## Considering only the Mainland India 
sdf = sdf.iloc[1:,:]
fig = sdf.plot()
plt.axis('off')
plt.show()
