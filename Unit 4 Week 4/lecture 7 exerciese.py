def my_fun():
    array = []
    i=1
    no = int(input("how my number you like to inut"))
    while i<=no:
        val = int(input("Enter"))
        array.append(val)
        i+=1
    del_num = input("Please type Y to delete and N if not")
    if del_num=='Y':
        num = int(input("enter the number you want to delete"))
        array.remove(num)
        print(avrg(array))
    else:
        print(avrg(array))
        
        

def avrg(par_list):
    sum(par_list)
    print(sum(par_list)/len(par_list))
    return sum(par_list)/len(par_list)
