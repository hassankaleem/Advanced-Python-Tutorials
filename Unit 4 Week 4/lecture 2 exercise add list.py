def add(a):
    type(a)
    sum=0
    for i in range(len(a)):
        sum = sum + a[i]
    return sum

print(add([1,2,3]))
