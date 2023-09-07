import numpy as np

def gen():
    N = 10000.0 # 1000 short flows
    T = 1200    # 5mins test
    lmbda = N / T
    count = int(N)
    x = np.arange(count)
    y = -np.log(1.0 - np.random.random_sample(len(x))) / lmbda
    y = np.round(y,2)

    strs_vals = ()
    for val in y:
        strs_vals = strs_vals + (str(val),)
    
    return strs_vals

