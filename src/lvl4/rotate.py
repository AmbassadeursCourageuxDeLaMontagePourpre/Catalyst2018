import numpy as np
from same_meteorite import *

def rotate(img, k):
    right = same_meteorite(np.rot90(img, k=1, axes=(0,1)))
    return right, left, middle 
