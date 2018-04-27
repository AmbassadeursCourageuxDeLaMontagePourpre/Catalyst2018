import numpy as np

def parse():
    l1 = list(map(int, input().split()))
    start = l1[0]
    end = l1[1]
    nb_images = l1[2]
    result = []
    for image_id in range(nb_images):
        l1 = list(map(int, input().split()))
        time_stamp = l1[0]
        nb_row = l1[1]
        nb_col = l1[2]

        image = np.zeros((nb_row, nb_col), dtype=int)
        
        for row_id in range(nb_row):
            l = list(map(int, input().split()))
            for col_id in range(nb_col):
                image[row_id][col_id] = l[col_id]

        result.append((time_stamp, image, start, end))
    return result
                

