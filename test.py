import os
import numpy as np

# original functions
from functions import tda
from functions import pwk  # persistence weighted kernel


def main():
    """
    Stage 1: Import persistence diagrams as list

    name_dir_pcd is the name of folder containing persistence diagrams
    num_pd is the number of persistence diagrams in list_pd

    list_pd = {D_1, ..., D_n} and each D_i is m * 2 matrix
    list_pd[0].shape = (m, 2) where m is the number of birth-death pairs

    HomCloud (or CGAL, DIPHA) computes persistence diagrams in squared
    birth-death coordinates.
    In order to scale this square effect, I use np.sqrt to mat_pd
    """
    name_dir_pcd = "%s/Desktop/data_tda/torus/pcd3_sample500_num40/pcd_pd/" \
                   % os.path.expanduser('~')
    num_pd = 40
    list_pd = []
    for k in range(num_pd):
        mat_pd = np.loadtxt("%s/dim1_%s.txt" % (name_dir_pcd, k)).reshape(-1, 2)
        list_pd.append(np.sqrt(mat_pd))  # scaling from (b^2,d^2) to (b,d)

    """
    Stage 2: Prepare a positive definite kernel and a weight function
    
    I define a positive definite kernel and a weight function as follows.
    You can define your p.d. kernel and weight function whatever you like.
    val_sigma is for k_{G}(x,y)=exp(-norm{x-y}^2 / 2 val_sigma^2)
    val_c and val_p are for w_{arc}(x)=arctan((pers(x) / val_c)^{val_p})
    I use some heuristics to determine the parameters.
    """
    def function_weight(_name_weight, _val_c=1.0, _val_p=1):
        if _name_weight == "arctan":
            def _func_weight(vec_bd):
                return np.arctan(
                    np.power((vec_bd[1] - vec_bd[0]) / _val_c, _val_p))
        else:  # p-persistence
            def _func_weight(vec_bd):
                return np.power(vec_bd[1] - vec_bd[0], _val_p)
        return _func_weight

    def function_kernel(_name_kernel, _val_sigma=1.0):
        if _name_kernel == "Gaussian":
            def _func_kernel(vec_bd_1, vec_bd_2):
                val_dist = np.power(np.linalg.norm(vec_bd_1 - vec_bd_2, 2), 2)
                return np.exp(-1.0 * val_dist / (2.0 * np.power(val_sigma, 2)))
        else:  # linear kernel
            def _func_kernel(vec_bd_1, vec_bd_2):
                return np.dot(vec_bd_1, vec_bd_2)
        return _func_kernel

    val_sigma = tda.parameter_sigma(list_pd, name_dir_pcd)
    val_c = tda.parameter_birth_death_pers(list_pd)[2]
    val_p = 5
    func_kernel = function_kernel("Gaussian", val_sigma)
    func_weight = function_weight("arctan", val_c, val_p)

    """
    Stage 3: Compute the Gram matrix
    
    name_rkhs is for p.d. kernel on the RKHS vectors 
    (see Section 3.3 in http://jmlr.org/papers/v18/17-317.html)
    approx is set whether you use the random Fourier features to compute the
    Gram matrix efficiently.
    (see Section 3.4 in http://jmlr.org/papers/v18/17-317.html)
    If the number of birth-death generator is large, I recommend to use 
    approx=True because it may take several days or months.
    """
    name_rkhs = ["Gaussian", "Linear"][0]
    approx = [True, False][0]
    class_pwk = pwk.Kernel(
        list_pd, func_kernel, func_weight, val_sigma, name_rkhs, approx)
    mat_gram = class_pwk.gram()

    """
    You can see the Gram matrix
    If name_rkhs = "Linear", 
    mat_gram[i, j] = <E_{k}(¥mu^{w}_{D_{i}}), E_{k}(¥mu^{w}_{D_{j}})>_{¥cH_{k}} 
    (see Equation 12 in http://jmlr.org/papers/v18/17-317.html) 
    """
    tda.plot_gram(mat_gram, "Gram matrix")

    """
    You can also see the squared distance matrix
    mat_distance[i, j] 
    = ||E_{k}(¥mu^{w}_{D}), E_{k}(¥mu^{w}_{E})||_{¥cH_{k}}^{2}
    """
    mat_distance = class_pwk.mat_distance
    tda.plot_gram(mat_distance, "Squared distance matrix")
    

if __name__ == "__main__":
    main()
