#write a function capable of reading two integers form the user

##num1=0
##num2=0
##
##for a in range(2):
##    if(a==0):
##        num1 = int(input('Enter the firt numb'))
##    else:
##        num2=int(input('Enter the second number'))
##
##if(num1==num2):
##    print('same')
##else:
##    if(num1<num2):
##        print(num1)
##    else:
##        print(num2)

## Two ways of doning this exercise

def lowest():
    a = int(input('Enter a number '))
    b = int(input('Enter a number '))
    if(a==b):
        print('same')
    else:
        if(a<b):
            print(a)
        else:
            prit(b)
