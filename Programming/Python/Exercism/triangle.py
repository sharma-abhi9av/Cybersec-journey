def equilateral(sides):
    
    p = sides[0] 
    q = sides[1]
    r = sides[2]
    
    if p == q == r != 0:
        return True 
    else: 
        return False 
    pass


def isosceles(sides):
    p = sides[0] 
    q = sides[1]
    r = sides[2]
    if (p < q + r and r < q + p and q < p + r) and (p == q  or p == r  or q == r):
       return True
    else: 
       return False
    pass

def scalene(sides):
    p = sides[0] 
    q = sides[1]
    r = sides[2]
    if  (p < q + r and r < q + p and q < p + r) and p != q and q != r and r != p   : 
        return True 
    else : 
        return False 
    
    pass
