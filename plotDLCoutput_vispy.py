# For fast plotting of DeepLabCut bodyparts from analyzed video

from wfield.io import VideoStack
import numpy as np
import pandas as pd
import sys
from vispy import plot as vp
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox, QRadioButton, QVBoxLayout, QWidget, QSlider)

# define the slider window
class DLCvideomaker(QWidget):
    def __init__(self, parent=None):
        super(DLCvideomaker, self).__init__(parent)

        grid = QGridLayout()
        grid.addWidget(self.createExampleGroup(), 0, 0)
        self.setLayout(grid)

        self.setWindowTitle("DLCvideomaker")
        self.resize(400, 300)

    def createExampleGroup(self):
        groupBox = QGroupBox("Video slider")

        radio1 = QRadioButton("&Frames")

        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(10)
        slider.setMaximum(len(mov)-1)
        slider.setSingleStep(1)
        slider.valueChanged.connect(set_data)
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(slider)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

# load video and data
video_path = r'C:\Users\Anne\data\JC066\20211006_151200\DropletsTask\JC066_20211006_151200_cam1_00000002.avi'
data_path = r'C:\Users\Anne\data\JC066\20211006_151200\dlc_analysis\JC066_20211006_151200_cam1_00000002DLC_resnet50_JC066Jun27shuffle1_300000.h5'
mov = VideoStack([video_path], outputdict={'-pix_fmt':'gray'})
dlc_coords = pd.read_hdf(data_path)
bpts = dlc_coords.columns.get_level_values("bodyparts")
all_bpts = bpts.values[::3]
dlc_coords_x, dlc_coords_y, dlc_coords_likelihood = dlc_coords.values.reshape((len(dlc_coords), -1, 3)).T
bplist = bpts.unique().to_list()
nbodyparts = len(bplist)
val = 0

# allocate coordinates for all bodyparts for first frame
x = []
y = []
for label in range(nbodyparts):
    x.append(dlc_coords_x[label, int(val)])
    y.append(dlc_coords_y[label, int(val)])
    
frame = mov[int(np.mod(val,len(mov)-1))].squeeze()
  
# make vispy widget
fig = vp.Fig(size=(800, 600), show=False,vsync=True)
plot = fig[0, 0]
plot.bgcolor = "#efefef"

# to update coordinates by frame
def set_data(val):
    x = []
    y = []
    for label in range(nbodyparts):
        x.append(dlc_coords_x[label, int(val)])
        y.append(dlc_coords_y[label, int(val)])
    frame = mov[int(np.mod(val,len(mov)-1))].squeeze()
    pl.set_data(np.vstack([x,y]).T)
    im.set_data(frame)

# plot and show data on vispy widget
pl = plot.plot(data=np.vstack([x,y]).T,symbol='o',marker_size=3,width = 0,face_color='k',edge_color='k')
im = plot.image(frame, cmap="gray")
plot.camera.set_range((mov.shape[2],0), (mov.shape[3],0)) # flip upside down video
fig.show(run=True)

# opens slider window
app = QApplication(sys.argv)
sliderwindow = DLCvideomaker()
sliderwindow.show()

# to-do:
# 1) add drop down menu in slider window to select symbol to use, marker size, and color