# Pass a list to this function and it will identify which number is repeaded most times.

def my_mode(mylist):
    my_dic={} # new dictionary
    for all in mylist:
        if all not in my_dic:
            my_dic[all] = 1
        else:
            my_dic[all] = my_dic[all]+1
    highest = 0
    print(my_dic)
    for ke in my_dic:
        if my_dic[ke]>highest:
            highest=my_dic[ke]
            my_key=ke
    print('The number',my_key,'is repeated most times')




##    print(max(my_dic.values()))
##    most = max(my_dic.values())
##    key = my_dic.keys()
##    print(key,most)
            
##    mostone = key[most]
     #print(mostone)
##  a = [1,2,23,4,5,1,4]
##  print(max(a))

##    greater =0 
##    print(my_dic)
##    print(my_dic.values())
##    
##    
##    for val in my_dic.values():
##        if val>greater:
##            greater=val
##    print(greater)
##            


    
##    
##    for key in my_dic:
    
##        if <greater:
##            greater= my_dic[key]
#    print(greater)
