# The idea is to make a simple word counter, using best practices and validation.

print('Super Word Counter 3000')
user_input = input('Please type in your text: ')

def counter(input):
    try:
        counter = 0
        text = input.split()
        for word in text:
            counter += 1
        print(f'Your text have {counter} words.')
    except ValueError:
        print('Please type any text.')


counter(user_input)