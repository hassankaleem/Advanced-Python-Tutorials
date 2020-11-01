# foor loops , string , list , return , concatemention for mutation of string as string is imutable.

#Calculate numebr of time some thing repeat in the string
def my_fun(arg_1): 
    count=0
    for value in arg_1: # one way of doing this checking value by value of stirng via iteration for loop 
        if(value=="a"):
            count += 1  # if you write += this will increment count by 1 if we
            #           do count = + 1 if will assign 1 to count.
    return count
print(my_fun("Calculate number of time a comes in this stringaaaaa"))

def my_fun2(arg_1):
    count=0
    for value in range(len(arg_1)): # Second way of doing this by checking index by index of string via iteration for loop 
        if(arg_1[value]=="a"):
            count+=1   
    return count

print(my_fun2("Calculate number of time a comes in this stringaaaaa"))

## String is imutable data type where we can not instert somethin in it
##let try , 

var1 = "This is my world!!"
##var1[0]="a"    # error str' object does not support item assignment

var1 = 'a'+var1[1:len(var1)] #concatination + string mutation by addading a in it. 
print(var1)
print(len(var1))  
for i in range(0,len(var1)):  #this time i holds the index of the string with rage limit we define
    print(var1[i],i, type(i))

for i in var1: # this time i hold the string value the var1 variable have
    print(i,type(i))


var1 = 1
#for i in var1: # like stirng in previous example we can't iterate the integer number so error popups
##    print(i, type(i)) 

var1 = ['1','2','bed',3]

for i in var1:  # in this example for loop is iterating stirngs and intergers 
    print(i,type(i))
