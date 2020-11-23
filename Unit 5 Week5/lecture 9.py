##import os
##
##def my_fun(path,char):
##    all_tuple = () # used tuple to save all the data of text in form of characters
##    all_list = [123] # use list to save text form the file path ( text file )
##    all_list.append('a')
##    counter = 0
##    my_file = open(path)
##    for txt in my_file:
##        print(txt)
##        #all_list.append(txt)
##        all_tuple  = all_tuple + tuple(txt)
##        #print(all_list)
##        print(all_tuple)
##    my_file.close()
##    for check in all_tuple:
##        if check == char:
##            counter+=1
##    return counter


##a = ['asdasdaasd asd asd asd asd']
##print(a)
##b = ('asd asd asd asd asd')
##print(b)


##   scanned name are like (SMCHGA 123) ## Rename it to (Custom Name like Ace Point Limited)
    
## software to rename the all the scanned creditors letters with some custom name.

##my_files = os.listdir('C:\\scans\\New folder')
##counter = 1
####print(my_files)
##print(type(my_files))
##
##for files in my_files:
##    type(files)
##    os.rename('C:\\scans\\New folder\\'+files,'C:\\scans\\New folder\\Ace Point Limited'+str(counter)+'.pdf')
##    print(files+str(counter))
##    counter +=1
##

my_files = open('hassan', 'w')

my_files.write('some thinx')
my_files.close()

