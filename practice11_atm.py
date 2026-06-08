# ATM Withdrawal Optimizer
# A financial logic system designed to calculate the most efficient distribution of banknotes for a requested withdrawal amount.

# Inputs: User’s requested withdrawal amount (integer).

# Logic:

# Validates that the input is a valid numeric value and a multiple of R$ 2 (as no R$ 1 banknotes exist).

# Implements a greedy algorithm to determine the minimum quantity of banknotes required (R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, R$ 2).

# Handles exceptions for invalid numeric inputs or non-divisible values.

# Outputs: A breakdown of the exact count of each banknote denomination provided to the user.

print('\n-- ATM Withdraw System --\n')

def hundred(value):
    bill = value // 100
    print(f'{bill} of $100')
    return value % 100

def fifty(value):
    bill = value // 50
    print(f'{bill} of $50')
    return value % 50

def twenty(value):
    bill = value // 20
    print(f'{bill} of $20')
    return value % 20

def ten(value):
    bill = value // 10
    print(f'{bill} of $10')
    return value % 10

def five(value):
    bill = value // 5
    print(f'{bill} of $5')
    return value % 5

def two(value):
    bill = value // 2
    print(f'{bill} of $2')
    return value % 2

while True:
    try:
        withdraw_value = int(input('\nType in withdraw amount (even numbers please): '))
        if withdraw_value % 2 == 0:
            remaining = hundred(withdraw_value)
            remaining = fifty(remaining)
            remaining = twenty(remaining)
            remaining = ten(remaining)
            remaining = five(remaining)
            remaining = two(remaining)
            
            while True:
                try:                    
                    user_input = int(input('\nPlease type 1 if you want to calculate another value, type 2 if you want to exit the application: '))
                    if user_input == 1:
                        break
                    elif user_input == 2:
                        print('Leaving the app. See ya!')
                        exit()
                    else:
                        print('Option not valid! Choose between 1 or 2')
                except ValueError:                
                    print('Please type a number.')
        else:
            print('Please type in a even number. The ATM does not process uneven values.')
    except ValueError:
        print('Please type a number.')

# Optimized IA code:

# bills = [100, 50, 20, 10, 5, 2]

# while True:
#     try:
#         value = int(input('Type in withdraw amount (even numbers please): '))
#         if value % 2 == 0:
#             for bill in bills:
#                 count = value // bill
#                 value = value % bill
#                 print(f'{count} of ${bill}')
#             break
#         else:
#             print('Please type in a even number.')
#     except ValueError:
#         print('Please type a number.')