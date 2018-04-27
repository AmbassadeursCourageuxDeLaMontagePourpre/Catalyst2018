import numpy as np
from parser import *

images = parse()

# Pour chaque image
for timestamp, img in images:
    
    # On parcourt l'image pour voir si on trouve un astéroide
    i = 0
    j = 0
    while j < np.shape(img)[0]:
        if img[i][j] > 0:
            print(timestamp)
            break
        i+=1
        if i == np.shape(img)[1]:
            j += 1
            i = 0
