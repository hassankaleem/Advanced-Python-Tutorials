var = int(input('Enter some number'))
def check_up(var):
    if(var>0):
        print('This number is positive')
    elif(var==0):
        print('This number is equal to zero')
    else:
        print('This number is negative')
check_up(var)
