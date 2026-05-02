def score(x, y):
  # for 10 points if the distance must be 1 meter or less
  # i can think of using distance formula 
  # here x1 and y1 are origin so 0,0
# dist. formula becomes (x**2 + y**2)** 1/2
    dist = (x**2 + y**2)**(1/2)
    if dist <= 1: 
       return 10
    if dist <=5 and dist > 1:
       return 5
    if dist <=10 and dist > 5:
       return 1
    if dist > 10 :
       return 0
    pass
