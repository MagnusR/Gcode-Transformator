import numpy as np
def Transform(current_pos):
    mat=np.matrix("3 0 0;0 2 0;0 0 1")
    transformed_pos=mat.dot(current_pos)
    return transformed_pos.tolist()[0]