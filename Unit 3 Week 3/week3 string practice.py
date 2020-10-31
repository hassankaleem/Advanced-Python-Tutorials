## use len() to  check string lenght and fect the value stored in string over index.
val="My name is Hassan Kaleem"
for i in range(0,len(val)):
    print(val[i])


def findLen(str): 
    counter = 0    
    for i in str: 
        counter += 1
    return counter 
  
  
str = "hello dear"
print(findLen(str))
