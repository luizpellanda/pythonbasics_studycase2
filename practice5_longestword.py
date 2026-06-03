# Long Word Identifier
# A utility for editors to assess text readability by identifying complex or long words.

# Inputs: A paragraph or string of text.

# Logic: Analyze word length; filter and isolate words containing more than 10 characters.

# Outputs: A list of identified long words or a notification if no words meeting the criteria are found.

long_word_def = 10

user_input = input('Please type in your sentence: ')
phrase = user_input.split()
result = []

for word in phrase:
    if len(word) >= long_word_def:
        result.append(word)

if result:
    print('Long words are: ')
    for word in result:
        print(word)
else:
    print('No long words found')

# # Optimized IA code:

# def long_word_identifier(text):
#     long_word_def = 10
#     words = text.split()
#     result = [word for word in words if len(word) > long_word_def]

#     if result:
#         print('Long words found:')
#         for word in result:
#             print(word)
#     else:
#         print('No long words found.')

# print('Long Word Identifier')

# while True:
#     user_input = input('Please type in your sentence: ').strip() #strip removes the empty spaces on the string borders - a " " would turn into a "" and therefore the validation works
#     if not user_input:
#         print('Please enter a valid text. Try again.\n')
#     else:
#         long_word_identifier(user_input)
#         break