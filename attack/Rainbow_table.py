import itertools

# Module 1
personal_info = [
    "Atharva gaikwad","atharva", "23-10-2003", "sahil andhare", "vedant mali", "10", "09", "bala"
] 

# Module 2
common_words = [
    "1234", "qwerty", "abc123", "letmein", "111111", 
    "admin", "login", "welcome", "football", "iloveyou",
    "princess", "monkey", "sunshine", "master", "123456789", 
    "passw0rd", "baseball", "dragon", "1234567"
]

# Module 3
variations = {
    'a': '@',
    'o': '0',
    's': '$',
    'l': '1'
}

# Module 4
keyboard_patterns = [
    "asdfgh", "zxcvbn", "qazwsx", "123qwe", "1qaz2wsx", 
    "!qaz@wsx#", "1q2w3e4r", "1qazxsw2", "qwerty123", 
    "qwertyuiop", "asdfghjkl", "zxcvbnm", "poiuytrewq", 
    "mnbvcxz", "12345", "987654321", "!@#$%^", "0987654321", 
    "1q2w3e4r5t", "qwertypoiuy"
]

# Function to apply variations to a word
def apply_variations(word):
    variants = [word]
    for char, substitution in variations.items():
        if char in word:
            new_variants = [variant.replace(char, substitution) for variant in variants]
            variants.extend(new_variants)
    return variants

# Remove spaces and hyphens from personal information
personal_info_no_spaces_hyphens = [info.replace(" ", "").replace("-", "") for info in personal_info]

# Combine all modules into one list
all_modules = personal_info_no_spaces_hyphens + common_words + keyboard_patterns + personal_info


# Generate possible passwords
possible_passwords = set()

# Generate mismatched combinations of elements from different modules
for combination in itertools.combinations(all_modules, 2):
    for elem1, elem2 in itertools.product(apply_variations(combination[0]), apply_variations(combination[1])):
        password = elem1 + elem2
        if len(password) <= 14:
            possible_passwords.add(password)
        password = elem2 + elem1
        if len(password) <= 14:
            possible_passwords.add(password)

# Print all the generated passwords
print("Generated passwords:")
for password in possible_passwords:
    print(password)
    
    # Open a file to write the generated passwords
with open('generated_passwords.txt', 'w') as f:
    # Write each generated password to the file
    for password in possible_passwords:
        f.write(password + '\n')

# Notify the user that the file has been generated
print("Generated passwords have been saved to generated_passwords.txt")
    