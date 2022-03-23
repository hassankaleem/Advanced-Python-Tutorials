##class distance(object):
##    "this is my comment" 
##def myfun(p1,p2):
##    return (((p1.x-p2.y)**2 +(p1.y-p2.y)**2))**0.5


class point():
    "this is point class"

class rectangle():
    "This is box class"
    

def find_top_right(rect):
    p = point()
    p.x = rect.corner.x +  rect.width
    p.y = rect.corner.y + rect.height
    return p
