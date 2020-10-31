## use len() to  check string lenght and fect the value stored in string over index.
val="My name is Hassan Kaleem"
for index in range(0,len(val)):
    print(val[index],index,type(index))
##    print(index)


def findLen(str): 
    counter = 0    
    for i in str: 
        counter += 1
    return counter 
  
  
str = "hello dear"
print(findLen(str))


fruits = ["mango","apple","banana"]
for index in fruits:
    print(index)
    print(type(index))
