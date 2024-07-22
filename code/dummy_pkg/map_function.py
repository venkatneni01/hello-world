#map function - map(function,iterable)

def make_even(num):
    if num % 2 == 0:
       return num + 1
    else:
      return num
    
x = [552,551,543,45 ,33,22,448,339,229,44,39,49]

#y = list (map (make_even,x))

y = [make_even(num) for num in x]

#for num in x:
 #       y.append(make_even(num))

print (y)   