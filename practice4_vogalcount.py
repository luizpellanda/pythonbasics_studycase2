# Vowel Counter
# A tool for students and educators to analyze word structure by counting vowels in a given text.

# Inputs: A string of text provided by the user.
# Logic: Identify and count all occurrences of vowels (a, e, i, o, u), case-insensitive.
# Outputs: The total number of vowels found in the text.

def vowel_counter(text):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    count = 0
    text_lowercase = text.lower()
    for char in text_lowercase:
        if char in vowel_list:
            count += 1
    print(f'You have {count} vowels in your text.')

print('Vowel Counter')

while True:
    user_input = input('Type in your text: ').strip()
    if not user_input:
        print('Please enter a valid text. Try again.\n')
    else:
        vowel_counter(user_input)
        break

# Optimized IA code:

# def vowel_counter(text):
#     count = sum(1 for char in text.lower() if char in 'aeiou')
#     print(f'You have {count} vowels in your text.')

# print('Vowel Counter')

# while True:
#     user_input = input('Type in your text: ').strip()
#     if not user_input:
#         print('Please enter a valid text. Try again.\n')
#     else:
#         vowel_counter(user_input)
#         break