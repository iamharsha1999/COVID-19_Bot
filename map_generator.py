import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import io
from PIL import Image
import cv2

## Initialize the Visualization
sns.set(style = 'whitegrid', palette = 'dark', color_codes = True)
my_dpi = 96
figsize = (1080/my_dpi,1080/my_dpi)
plt.rcParams['figure.figsize'] = figsize

## Read the Shape Files
shp_path = 'Indian_States.shp'
sdf = gpd.read_file(shp_path)

## Considering only the Mainland India
sdf = sdf.iloc[1:,:]
sdf.drop([16], inplace = True)

sdf['centroid_x'] = 0
sdf['centroid_y'] = 0
for i in sdf.index:
    sdf.loc[i, 'centroid_x'] = sdf.loc[i,'geometry'].centroid.x
    sdf.loc[i, 'centroid_y'] = sdf.loc[i,'geometry'].centroid.y

x_list = list(sdf['centroid_x'])
y_list = list(sdf['centroid_y'])
st_names = list(sdf.st_nm)
image = cv2.imread('template.jpg')
fig = sdf.plot()
plt.axis('off')
# for i,st in enumerate(st_names):
#     plt.scatter(x_list[i],y_list[i],c = 'r', s = 250, marker=r"$ {} $".format(i))


plt.savefig('map.png')
map = cv2.imread('map.png')


map = cv2.resize(map,(image.shape[0],image.shape[1]))
alpha = 0.2
final = cv2.addWeighted(image[0:image.shape[0],0:image.shape[1],:],alpha,map[0:map.shape[0],0:map.shape[1],:],1-alpha,0)
cv2.imshow('Final',final)
k = cv2.waitKey(1)
flag = True

while flag:
    k = cv2.waitKey(1)
    if k == ord('q'):
        flag = False
        cv2.destroyAllWindows()
