#function than can take two strings in parameter and print every letter of string a that is also in string b


def my_fun(var1,var2):
    for i in var1:
        for  j in var2:
            if i == j:
                print(i)
print(my_fun('hassan','salman'))


def my_fun1(var1,var2):
    for i in var1:
        if i in var2:
            print(i)
print(my_fun1('hassan','salman'))
