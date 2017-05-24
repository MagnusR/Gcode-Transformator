import math
def Transform(current_pos):
    x,y,z=current_pos
    return [x,y,z+5*math.sin(x/2)]