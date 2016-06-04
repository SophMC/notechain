def distance(x,y):
    count=0
    for i,x in enumerate(x):
        if x != y[i]: count += 1
    return count
  
