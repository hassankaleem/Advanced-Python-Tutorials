def h_num():
    num = list(range(0,10))
    for i in range(0,10):
        mynum = int(input('Enter first number'))
        num[i] = [mynum]
    print(num[0:10])
    a = num[0]
    b = num[1]
    for var in range(0,10):
        if(a>b):
            print('a is greater than b',a,b)
            if(var<9):
                b= num[var+2]
            print('Largest value in 10 numbers is',a)
        elif(b>a):
            print('b is greater than a',b,a)
            if(var<9):
                a= num[var+2]
            print('Largest value in 10 numbers is',b)
