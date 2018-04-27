import numpy as np
import same_meteorite
from parser import *
from rotate import *

images = parse()

#sous-fonction de same_shape
db = []
def insert(img, timestamp, db):
    l = same_meteorite.same_meteroite(img)
    for i in range(len(db)):
         (img, img_tuples, all_times) = db[i]
         if l == img_tuples:
             all_times.append(timestamp)
             db[i] = (img, img_tuples, all_times)
             return
    db.append((img, l, [timestamp]))
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
    #for img, time in db:
    #    timestamps.append(time)
    return db 

print(same_shape(images))

final_timestamps = []
all_image = same_shapes(images)
for img, l, timestamp in all_image:
    new_timestamps = [timestamp]
    for k in range(3):
        new_rot = np.rot90(img, k)
        for sh in all_image:
            if same_meteorite.same_meteroite(sh) == same_meteorite.same_meteroite(new_rot):
                new_timestamps.append(sh)
                break
    
    final_timestamps.append(new_timestamps)
