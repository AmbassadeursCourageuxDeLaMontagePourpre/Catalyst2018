import numpy as np
from same_meteorite import *

def rotate(img):
    right = same_meteorite(np.rot90(img, k=1, axes=(0,1)))
    left = same_meteorite(np.rot90(img, k=1, axes=(1,0))) 
    return right, left 
