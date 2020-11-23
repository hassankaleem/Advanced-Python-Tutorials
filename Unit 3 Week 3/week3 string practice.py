## use len() to  check string lenght and fect the value stored in string over index.

## is this iteratring by index ?

val="My name is Hassan Kaleem"
for index in range(0,len(val)):
    print(val[index],index,type(index))

# is this iteration the valuse of string ?

val="My name is Hassan Kaleem"
for index in val:
    print(index,type(index))





fruits = ["mango","apple","banana"]

def findLen(str): 
    counter = 0    
    for i in str: 
        counter += 1
    return counter 
  
  
str = "hello dear"
print(findLen(str))





