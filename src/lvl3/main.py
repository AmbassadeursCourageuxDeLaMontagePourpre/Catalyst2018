import numpy as np
import same_meteorite
from parser import *

images = parse()

#sous-fonction de same_shape
db = []
def insert(img, timestamp, db):
    l = same_meteorite.same_meteroite(img)
    for i in range(len(db)):
         (img_tuples, all_times) = db[i]
         if l == img_tuples:
             all_times.append(timestamp)
             db[i] = (img_tuples, all_times)
             return
    db.append((l, [timestamp]))
    return

#identifier meteorites de meme forme
def same_shape(images):
    for timestamp, img in images:
        i = 0
        j = 0
        while j < np.shape(img)[1]:
            if img[i][j] > 0:
                insert(img, timestamp, db)
                break
            i+=1
            if i == np.shape(img)[0]:
                j += 1
                i = 0
                
    timestamps = []
    for img, time in db:
        timestamps.append(time)
    return timestamps

print(same_shape(images))
