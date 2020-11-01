# create a function that can take list as parameter and reverse the sequence of the list.
# input this ['hassan','salman','faizan']
# output this['hassan','salman','faizan']



def my_fun(my_list):
    counter = len(my_list)
    print(counter)
    for index in range(counter):
        counter-=1
        print(index,my_list[counter])
        

my_fun(['hassan','salman','faizan','sarmad','ahmad'])



