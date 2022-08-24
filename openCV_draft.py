# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 19:24:01 2022

@author: Anne
"""
from wfield.io import VideoStack
import numpy as np
import pandas as pd

import cv2
video_path = r'C:\Users\Anne\data\JC072\20220307_110327\DropletsTask\JC072_20220307_110327_cam0_00000000.avi'
data_path = r'C:\Users\Anne\data\JC072\20220307_110327\dlc_analysis\JC072_20220307_110327_cam0_00000000DLC_resnet50_JC072Apr1shuffle1_200000.h5'
mov = VideoStack([video_path], outputdict={'-pix_fmt':'gray'})
dlc_coords = pd.read_hdf(data_path)
val = 0
while True:
  frame = mov[int(np.mod(val,len(mov)-1))].squeeze()
  cv2.imshow('Frame', frame)
  val +=1
  if cv2.waitKey(25) & 0xFF == ord('q'):
      break
   
# Closes all the frames
cv2.destroyAllWindows()