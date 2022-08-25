# DLC-videomaker
Plot predicted DeepLabCut (DLC) labels onto video frames

This code is for quickly assessing DLC model performance. The DLC built-in function "create_labeled_video" does this, but is rather slow. This is meant to be a quicker alternative.

There are two ways to do this:
  1) using matplotlib 
  2) using vispy (https://vispy.org/)

The matplotlib method is in the form of a Jupyter Notebook whereas the vispy method is in a python script. The vispy method is preferred because it is faster.

Get the "wfield" module here: https://github.com/jcouto/wfield.

Made by Gabriel Rojas Bowe and Joao Couto.

24 Aug 2022
