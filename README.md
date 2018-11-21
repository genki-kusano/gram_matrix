This is used to create a Gram matrix from n persistence diagrams.<br>
I did this on macOS Mojave 10.14.1, python 3.7.1, and homcloud 2.0.0.<br>
My python codes use matplotlib, tqdm, os, and numpy.


# Summary
1. Download `data_tda` folder to your Desktop
2. Run `python3 test.py`

Explanations are written in test.py.<br>
If you have your persistence diagrams, please see comments titled Stage 1 in test.py and import your persistence diagrams as list.

The example dataset `data_tda` is a sequence of point cloud data deforming from a shpere to a torus, created by https://github.com/genki-kusano/point_cloud_data 
