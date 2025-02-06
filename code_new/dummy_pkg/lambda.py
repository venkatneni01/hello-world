 def my_map(my_func, my_iter):
   
    result = []

    for iteam in my_iter:
        new_iteam = my_func(iteam)
        result.append(new_iteam)

    return(result)    


num = [2,3,4,5,6,7]

cubed = my_map(lambda x: x**3, num)

print(cubed) 


