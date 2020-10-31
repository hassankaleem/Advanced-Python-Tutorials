def power_fn(num):
    for a in range(num):
        user_base = int(input('enter the base'))
        user_exp = int (input('enter the exponent'))
        print(user_base**user_exp)

power_fn(int(input('How many timer you want to repeat this:')))
