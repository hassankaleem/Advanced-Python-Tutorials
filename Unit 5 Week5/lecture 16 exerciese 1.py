# menu
import os

def my_fun():
    print("Press 1 to write a file")
    print("Press 2 to show the file on screen")
    print("Press 3 to exit the game")
    val = int(input("Press 1/2/3"))
    if val == 1:
        f_name=input("Enter the file name")
        m_file= open(f_name,'w')
        my_input= input("Type your data here")
        m_file.write(my_input)
        m_file.close()
        my_fun()
    if val == 2:
        f_name=open(input("Enter the file name"),'r')
##      for txt in f_name.readline():
##      for txt in f_name.readline():
##          print(txt)
        print(f_name.readline())
        my_fun()
    if val==3:
        return

my_fun()
