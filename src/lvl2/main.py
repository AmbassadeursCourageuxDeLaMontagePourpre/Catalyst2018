import numpy as np
from parser import *
import same_meteorite

images = parse()

db = []

def insert(img, timestamp, db):
    l = same_meteorite.same_meteroite(img)



    
    for i in range(len(db)):
         (img_tuples, begin, last, cpt) = db[i]
         if l == img_tuples:
             db[i] = (img_tuples, begin, timestamp, cpt + 1)
             return
    db.append((l, timestamp, timestamp, 1))
    return

# Pour chaque image


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


for (img_tuples, begin, last, cpt) in db:
    print(str(begin) + ' ' + str(last) + ' ' + str(cpt))
    
            

