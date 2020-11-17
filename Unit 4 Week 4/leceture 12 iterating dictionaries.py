def ite_dic(my_string):
    my_dic = {} # it will create empty dictionary
    for var in my_string:
        if var not in my_dic:
            my_dic[var]= 1
        else:
            my_dic[var] = my_dic[var]+1

    print(my_dic)
