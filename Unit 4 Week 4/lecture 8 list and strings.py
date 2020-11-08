strng = 'This is 17 character long string'
print(strng.split())
t=list(strng)
##t[3]='so'
print(t)


num = '12345'
t2 = num.split(',')
print(t2)


num2 = '1,2,3,4,5'
t3 = num2.split()
print(t3)

num3 = '1,2,3,4,5'
t4 = num3.split(',')
print(t4)


sep = ''
a= sep.join(strng)
print(a)
