import os
def my_fun():
    file_name = input('Enter the file name ')
    a = os.path.exists(file_name)
    print(a)
    if a==True:
        print(' this file exit')
    else:
        print(' this file is not listed')
        a= os.listdir()
        print(a)
        for value in a:
            if os.path.isfile(value):
                print(value)
