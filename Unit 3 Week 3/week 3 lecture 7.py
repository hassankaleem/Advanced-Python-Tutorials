#Calculate numebr of time some thing repeat in the string
def my_fun(arg_1):
    count=0
    for value in arg_1:
        if(value=="a"):
            count+=1   
    return count


print(my_fun("Calculate number of time a comes in this stringaaaaa"))

## String is imutable data type where we can not instert somethin in it
##let try , 

var1 = "This is my world!!"
##var1[0]="a"    # error str' object does not support item assignment

var1 = 'a'+var1[1:len(var1)] #concatination + string mutation by addading a in it. 
print(var1)
