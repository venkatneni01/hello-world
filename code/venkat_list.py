


def venkat_list():

    venkat_list1 = ['apple','uma','anu']
    print (venkat_list1)

    venkat_list2 =['apple','uma',5,9.9,True]
    print (venkat_list2)

    venkat_list2.append('orange')
    print(venkat_list2)

    venkat_list1.extend(venkat_list2)
    print(venkat_list1)

    for xtray in venkat_list1:
        if xtray == 'apple':
           print ('appple--------=111')
        elif xtray =='orange':
            print ('orange___LL___')
        else:
            print(xtray) 





        
if __name__ == '__main__':
    venkat_list()
    
