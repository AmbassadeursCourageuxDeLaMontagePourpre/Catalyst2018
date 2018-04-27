import numpy as np
from parser import *
import same_meteorite

images = parse()

db = []

def insert(img, timestamp, db):
    l = same_meteorite.same_meteorite(img)
    
    for i in range(len(db)):
         (img_tuples, begin, last, cpt) = db[i]
        if l == img_tuples:
            db[i] = (img_tuples, begin, timestamp, cpt + 1)
            return
    db.append(l, timestamp, timestamp, 1)
    return

# Pour chaque image
for timestamp, img in images:
    insert(img, timestamp, db)

for (img_tuples, begin, last, cpt) in db:
    print(str(begin) + ' ' + str(last) + ' ' + str(cpt))
    
            

