## 
import os
def my_fun(file_1,file_2):
    file1_data = []
    file2_data  = []
    counter = 0
    f1 = open(file_1,'r')
    f2 = open(file_2,'r')
    for data1 in f1.read():
        file1_data.extend(data1) 
    for data2 in f2.read():
       file2_data.extend(data2)
    for comp in range(len(file2_data)):
##       print(len(file2_data),comp)
       print(file1_data[comp-1],file2_data[comp-1])
       if file1_data[comp-1]==file2_data[comp-1]:
           
           counter+=1
    print(counter)          
    f1.close()
    f2.close()

