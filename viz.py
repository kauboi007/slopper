import matplotlib.pyplot as plt
import numpy as np
import math
#plots
def visualize(p):
    x=np.arange(8)
    l,k=np.meshgrid(x,x)
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    z=[[math.log(p[k][l]) for l in range(8)] for k in range(8)]
    z[0][0] = z[0][1] 
    z = np.array(z)
    z = z - z.min()  
    ax.plot_surface(l, k, z, cmap='viridis', edgecolor='none')
    ax.view_init(elev=35, azim=35)
    ax.set_title("power spectrum")
    plt.show()  

def visualize_residual(p, alpha, intercept):
    x = np.arange(8)
    l, k = np.meshgrid(x, x)
    z = np.zeros((8, 8))
    for ki in range(8):
        for li in range(8):
            if ki == 0 and li == 0:
                z[ki][li] = 0
                continue
            f = math.sqrt(ki**2 + li**2)
            predicted = intercept + alpha * math.log(f)
            actual = math.log(p[ki][li])
            z[ki][li] = actual - predicted
    z = z - z.min()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(l, k, z, cmap='Blues', edgecolor='none')
    ax.view_init(elev=35, azim=45)
    ax.set_title('residual')
    plt.show()