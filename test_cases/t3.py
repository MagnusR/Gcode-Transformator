import math
def Transform(current_pos):
    """a useful transformation that places the """
    R=50
    cx,cy,cz=(0,0,-R)
    x,y,z=current_pos

    if R**2-(cx-x)**2-(cy-y)**2>0:
        zt=cz+math.sqrt(R**2-(cx-x)**2-(cy-y)**2)
    else:
        zt=z
    return [x,y,zt]