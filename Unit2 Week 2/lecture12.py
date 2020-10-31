##Print the absolute number no 

def absolute_val(val):
    if(val<0):
        val= -val
    print(val)
    absolute_val(val)
