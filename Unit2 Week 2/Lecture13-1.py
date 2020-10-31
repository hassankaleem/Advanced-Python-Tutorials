## Factorial with for loop method
def factorial(num):
    var =1
    for a in range(num-1):
         var = var * num
         num = num -1
    return(var)

a = factorial(4)
print(a)
