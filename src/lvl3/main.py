import numpy as np
from parser import *

images = parse()



def construct_solution(init, acc,  d, time, dico):
    if (init + time * d) in dico:
        (b, i) = dico[init + time * d]
        if not b:
            return acc
        else:
            acc.append(t)
            construct_solution(init, acc, d, time + 1, dico)
    else:
        return acc

def extract_solution(t, dico, l):
    for t in l:
        (b, i) = dico[t]
        if b:
            d = t - base_time
            s = construct_solution(base_time, [], 2, dico)
         if len(s) >= 4:
            solution = []
            for t in s:
                solution.append(t)
                b, i = dico[t]
                dico[t] = (False, i)
            return solution

def all_solution(l):
    dico = {}
    for i in range(len(l)):
        t = l[i]
        dico[t] = (True, i)

    solution = []
    for t in l:
        (b, i) = dico[t]
        if b:
            solution.append(extract_solution(t, dico, l))
    return solution



            
        
            


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
