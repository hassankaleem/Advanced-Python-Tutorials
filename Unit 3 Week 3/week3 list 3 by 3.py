##a = [2]
##b = [3]
##c= [a[0]*b[0]]
##print(c)
##
##
##
##list1 = ["M", "na", "i", "Ke"] 
##list2 = ["y", "me", "s", "lly"]
##list3 = [i + j for i, j in zip(list1, list2)]
##print(list3)
##


## Matrix

a = [[1,2,3],[4,5,6],[7,8,9]]
##print(len(a))
def my_list(self,b=[[],[],[]]):
    for i in range(len(a)):
##       print(a[i][i])
       for j in range(len(a[i])):
            print(a[i][j],i,j)

my_list(a)
