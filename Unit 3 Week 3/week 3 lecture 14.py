def my_fun(my_list):
    new_list = [''] * len(my_list)
    print(new_list)
    for i in range(len(my_list)):
        print(my_list[len(my_list)-1-i])
        new_list[i] = my_list[len(my_list)-1-i]
    return new_list



print(my_fun(['hassan','salman','Klaeem','ahmad']))



