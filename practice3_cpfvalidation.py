# CPF Validation Tool
# A utility to validate CPF input format for administrative tasks.

# Inputs: A string representing the CPF.

# Validation Rules: Must contain exactly 11 digits and strictly numerical characters.

# Outputs: Success confirmation or an error message if the input contains non-numeric characters or an incorrect digit count.


def cpf_validation(cpf):
    if len(cpf) == 11 and cpf.isdigit():
        print('CPF is valid!')
    else:
        print('CPF is invalid.')

print('CPF Validation')

while True:
    try:
        user_input = input('Please type in your CPF (11 numeric): ')
        if not user_input.isdigit():
            raise ValueError
        cpf_validation(user_input)
        break
    except ValueError:
        print('Please enter only numeric values. Try again.\n')