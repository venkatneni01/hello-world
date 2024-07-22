
def custom_comprehension():
      # custom_list = [i for i in [1,2,3,4,5]] 
      # print (custom_list)

  #s_dict = {x: x * 5 if x ==5 else x + 1 for x in [1,2,3,4,5]}
  #print(s_dict)

    #custom_list = [i for i in [1,2,3,4,5,6] if i == 2]
    #print (custom_list)

 # custom_list = [i if (i ==2) else i*2 for i in [1,2,3,4,5,6,]]
 #print (custom_list)

 custom_dict ={x: x ** 2 for x in [1,2,3,4,5,6]}
 print (custom_dict)


if __name__ == '__main__':    
    custom_comprehension()
