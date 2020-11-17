import os

def my_fun(path,char):
    all_tuple = () # used tuple to save all the data of text in form of characters
    all_list = [123] # use list to save text form the file path ( text file )
    all_list.append('a')
    counter = 0
    my_file = open(path)
    for txt in my_file:
        print(txt)
        #all_list.append(txt)
        all_tuple  = all_tuple + tuple(txt)
        #print(all_list)
        print(all_tuple)
    my_file.close()
    for check in all_tuple:
        if check == char:
            counter+=1
    return counter


##a = ['asdasdaasd asd asd asd asd']
##print(a)
##b = ('asd asd asd asd asd')
##print(b)



## software to rename the all the files in some directory

my_file = open('C:\\Users\\hp\\Desktop\\new-branch-pull-push\\pythonpractice\\open.txt','w')


my_files = os.listdir('C:\\scans')

print(my_files)
print(type(my_files))

for files in my_files:
    print(files)

