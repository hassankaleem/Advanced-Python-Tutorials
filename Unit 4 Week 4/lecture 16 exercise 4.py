def my_fun(strng):
    my_dic = {}
    lis = []
    lis2= []
    current_key=1
    for value in range(len(strng)):
        print(strng[value],value)
        if strng[value] not in lis:
            print("if called")
            lis.append(strng[value])
            my_dic[current_key]=lis
        else:
            print("else one called")
            current_key = current_key +1
##            my_dic[current_key]=lis2.append(['L'])
        
    print(my_dic)
        
