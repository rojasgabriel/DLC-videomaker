# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:02:41 2022

@author: Anne
"""
#DLC-VideoMaker by GRB

import matplotlib.pyplot as plt
import matplotlib.image as image  
#import numpy as np 

#%%

data = image.imread(r'C:\Users\Anne\data\DLC-videomaker\test_data\test_image.png')
# x = [200,100]
# y = [500,300]
for i in coord:
    plt.plot(x, y, 'wo')
    plt.imshow(data)
    plt.show()
    
    
#%%
# Read the coordinates from the csv

# Read a single frame from the camera

from wfield.io import VideoStack
mov = VideoStack([r"C:\Users\Anne\data\DLC-videomaker\test_data\JC047_20211001_114337_cam0_00000000.avi"],
                 outputdict={'-pix_fmt':'gray'})

# loads the coords
import pandas as pd
dlc_coords = pd.read_csv(r'C:\Users\Anne\data\DLC-videomaker\test_data\JC047_20211001_114337_cam0_00000000DLC_resnet50_JC047-lateralJul6shuffle1_300000.csv')
#dlc_coords = dlc_coords.values

temp = dlc_coords.values
x_data = np.zeros(len(temp))
x_data = np.resize(x_data, dlc_coords.shape)
y_data = x_data
del temp

i = 0
while i < 15:
    if i == 0:
        x_data[i] = dlc_coords.iloc[:,1]
        y_data[i] = dlc_coords.iloc[:,2]
    else:
        x_data[i] = dlc_coords.iloc[:,i*3-2] #get x values
        y_data[i] = dlc_coords.iloc[:,i*3-1] #get y values
    i += 1



#%%
# Plot a single frame
# make a function that lets us explore the frames in the movie.
import pylab as plt
from matplotlib.widgets import Slider
fig = plt.figure()
ax = fig.add_axes([0,0.2,1,.8])
plt.axis('off')
im = plt.imshow(mov[100].squeeze(),cmap='gray_r')
# allocate the plot
xx = plt.plot()

sliderax = fig.add_axes([0.1,0.05,0.8,0.02])
slider = Slider(sliderax, 'Frame', 0, len(mov)-1, valstep=1)

def plot_dlc_coords(frame):
    xx.set_ydata...
    xx.set_xdata...
    raise NotImplementedError('bnoo')

def update_frame(val):
    im.set_data(mov[int(val)].squeeze())    
    # plot coordinates
    fig.canvas.draw()
    
slider.on_changed(update_frame)
