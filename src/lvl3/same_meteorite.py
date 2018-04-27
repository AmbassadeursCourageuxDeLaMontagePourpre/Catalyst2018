import numpy as np

def same_meteroite(img):
    # Parcourt de l'image
    # Dès qu'on trouve le premier, point
    # il devient la référence
    # Ensuite on ajoute chaque point > 0
    # relatif  

    ref_x = -1
    ref_y = -1

    new_shape = []

    for i in range(len(img)):
        for j in range(len(img[i])):

            # Si on trouve un pixel
            if img[i][j] > 0:
                
                # Le point de ref n'est pas fait
                if ref_x == -1:
                    ref_x = i
                    ref_y = j

                # On l'ajoute au new_shape            
                new_shape.append((ref_x-i, ref_y-j))

    return new_shape
