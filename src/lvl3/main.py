import numpy as np
import same_meteorite
from parser import *

def construct_solution(init, acc, d, time, dico):
    if (init + time * d) in dico:
        (b, i) = dico[init + time * d]
        if not b:
            return acc
        else:
            acc.append(init + time * d)
            construct_solution(init, acc, d, time + 1, dico)
            return acc
    else:
        return acc



def is_valid(solution, start, end, d):
    return d > solution[0] - start and d > end - solution[-1] and len(solution) >= 4
    
def extract_solution(t0, dico, l, start, end):
    for t in l:
        (b, i) = dico[t]
        if b:
            d = t - t0
            s = construct_solution(t0, [t0, t], d, 2, dico)
            # print(s)
            if is_valid(s, start, end ,d):
                solution = []
                for t in s:
                    solution.append(t)
                    b, i = dico[t]
                    dico[t] = (False, i)
                return solution
            

def all_solution(l, start, end):
    dico = {}
    for i in range(len(l)):
        t = l[i]
        dico[t] = (True, i)
        

    solution = []
    for t in l:
        (b, i) = dico[t]
        dico[t] = (False, i)
        if b:
            solution.append(extract_solution(t, dico, l, start, end))
    
    return solution

db = []
def insert(img, timestamp, start, end, db):
    l = same_meteorite.same_meteroite(img)
    for i in range(len(db)):
         (img_tuples, all_times, start, end) = db[i]
         if l == img_tuples:
             all_times.append(timestamp)
             db[i] = (img_tuples, all_times, start, end)
             return
    db.append((l, [timestamp], start, end))
    return

#identifier meteorites de meme forme
def same_shape(images):
    for timestamp, img, start, end in images:
        i = 0
        j = 0
        while j < np.shape(img)[1]:
            if img[i][j] > 0:
                insert(img, timestamp, start, end, db)
                break
            i+=1
            if i == np.shape(img)[0]:
                j += 1
                i = 0
                
    timestamps = []
    for img, time, start, end in db:
        timestamps.append((time, start, end))
    return timestamps

images = parse()
timestamp = same_shape(images)

s = []

# print(timestamp[-1])
for asteroide_set, start, end in timestamp:
    for solution in all_solution(asteroide_set, start, end):
        if solution != None:
            s.append((solution[0], solution[-1], len(solution)))

for x in sorted(s, key=lambda x : x[0]):
    print(str(x[0]) + " " + str(x[1]) + " "  + str(x[2]))
    
