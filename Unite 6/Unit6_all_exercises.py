# Ex:1
# def Jaccard_(L1,L2):
#     counter=0
#     for val in range(len(L1)):
#         if L1[val] == L2[val]:
#             counter +=1
#     print(counter)
#     myval = counter/(len(L1)+len(L2)-counter)
#     print(myval)
#
#
#
# Jaccard_([1,2,3,6,8,9],[1,2,4,5,6,7])

# Ex:2
#
# def input_number():
#     try:
#         my_num = int(input("Enter only umber"))
#         print(my_num)
#     except:
#         print("its not an integer")
# input_number()
#

# Ex:3

# def my_sorted(L1):
#     a1=0
#     for all in range(len(L1)):
#         if a1<=L1[all]:
#             a1=L1[all]
#             print("True")
#         else:
#             print("False")
# my_sorted([1,2,3,4])

# Ex:4
# def reverse(L1):
#     L2 = ['']*len(L1)
#     print(len(L2))
#     for val in range(len(L1)):
#         L2[val] = L1[len(L2)-1-val]
#
#
#     print(L2)
# reverse(['a','b','c'])
#

# Ex:5
# def my_lists(L1):
#     print(L1[0])
#     print(L1[len(L1)-1])
#     print(sum(L1))
#
# my_lists([1,2,3,4,5])


# Ex:6
# def my_list(L1):
#     for val in range(len(L1)):
#         if L1[val] != L1[len(L1)-1-val]:
#             return False
#         else:
#             return True
#         # print(L1[val],L1[len(L1)-1-val])
#
# def pas(pass_list):
#     counter=0
#     for data in pass_list:
#         if my_list(data):
#             counter +=1
#     print(counter)
# pas(['aba','cba'])

# import os.path
#
# def my_file(filename):
#     # dotname = "hassa.txt"
#     # part[0] = "salman"
#     #
#     # print(part)
#     part = filename.split(".")
#     print(part[0])
#     try:
#         with open(filename) as oppo:
#             print("True")
#     except:
#         print("False")
# my_file("hassan.txt")

# import os
#
# def myfile(filename):
#     found = False
#     allfile = os.listdir()
#     print(allfile)
#     for files in allfile:
#         myfiles = files.split(".")
#         if filename == myfiles[0]:
#             print(filename)
#             found = True
#             print(found)
#     return found
#
# myfile("hassan")







import os

def freq(str1):

    mydic = {}
    mylist = []
    # print(type(mydic))
    file = open(str1,'r')
    print(type(file))
    for words in file:
        mylist.append(words)
    print(mylist)
    for eachword in mylist[0].split('/n'):
        print(eachword)
        # print(len(eachword))
        # print(type(eachword))
        for word in eachword.split(' '):
            print(word)
            if word not in mydic:
                mydic[word] = 1
            else:
                mydic[word] +=1
    print(mydic)

    # mynew = mylist[0].split('/n')
    # print(mynew)

    # for val in file.readlines():
    #     # print(type(val))
    #     for ch in val:
    #         # print(ch)
    #         if ch not in mydic:
    #             mydic[ch] = 1
    #         else:
    #             mydic[ch] +=1

    # print(mydic)
    # if os.path.exists(str1):
    #     print(str1)

freq("hassan.txt")






