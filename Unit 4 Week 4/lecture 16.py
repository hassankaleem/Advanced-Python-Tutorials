my_string='this is outside'
def loc_var():
    my_string= 'this is inside the function'
    print(my_string)
loc_var()
print(my_string)


