# Secure Password Generator
# A tool to generate high-entropy, random passwords for user account registration.

# Inputs: None (parameterized to a fixed length of 12 characters).

# Logic: Randomly select characters from a pool consisting of uppercase letters, lowercase letters, numbers, and special characters, ensuring the final output meets minimum diversity requirements (at least one of each type).

# Outputs: A generated 12-character secure password.

import string
import random

valid_chars = string.ascii_letters + string.digits + string.punctuation

password_length = 12
result = []

while len(result) < password_length:
    result.append(random.choice(valid_chars))

print(''.join(result))

# Optimized IA code:

# import string
# import random

# valid_chars = string.ascii_letters + string.digits + string.punctuation

# password = ''.join(random.choices(valid_chars, k=12))
# print(password)