## Factorial with recursion method
total = 1
def factorial(num):
    if num>0:
        global total
        total = total * num
        num = num - 1
        factorial(num)
    else:
        print(total)
        total = 1
        

