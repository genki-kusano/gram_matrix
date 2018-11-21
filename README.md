This is an example code to compute a Gram matrix (and a distance matrix) from persistence diagrams by the persistence weighted kernel method.<br>
I did this on macOS Mojave 10.14.1, python 3.7.1, and homcloud 2.0.0.<br>
My python codes use matplotlib, tqdm, os, and numpy.<br>
Reference: Kernel Method for Persistence Diagrams via Kernel Embedding and Weight Factor.
Genki Kusano, Kenji Fukumizu, Yasuaki Hiraoka; JMLR 18(189):1−41, 2018. http://jmlr.org/papers/v18/17-317.html

# Summary
1. Download `data_tda` folder to your Desktop
2. Run `python3 test.py`

Explanations are written in test.py.<br>
If you have your persistence diagrams, please see comments entitled "Stage 1" in test.py and import your persistence diagrams as list.

The example dataset `data_tda/torus/pcd3_sample500_num40` contains 40 persistence diagrams in dimension 1 whose point sets are deforming from a shpere to a torus (dim1_0.txt is a persistence diagram of a sphere and dim1_39.txt is that of a torus), created by https://github.com/genki-kusano/point_cloud_data 
