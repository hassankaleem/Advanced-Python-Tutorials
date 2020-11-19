import os

def my_fun(nam_f1,nam_f2):
    my_file1 = open(nam_f1,'r+')
##    my_file.write('hello world')
    my_file2 = open(nam_f2,'w+')
    for data in my_file1.read():
##        print(data)
        
        my_file2.write(data)
##        print(my_file2.readline())
    my_file2.close()  
    my_file1.close()
