##for a in range(101):
##    print (a)
##    
##for x in range(20):
##    user_number = int(input('Enter the numbers'))
##    sqr_of_each= user_number ** 2
##    print('Square of '+str(user_number)+' is',sqr_of_each)

total = 0
for y in range(4):
    user_numbers = input('enter the number')
    total = total + float(user_numbers) 
avg = total/4
print('Average is:'+str(avg))
