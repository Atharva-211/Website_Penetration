import itertools

# Given information
name = "sahil andhare"
bday = "17-10-2004"
father_name = "Satish andhare"
fav_player = "messi"
jersey_no = ["10", "09"]
pet_name = "bala"

# Common words
common_words = [
    "123456", "qwerty", "abc123", "letmein", "111111", 
    "admin", "login", "welcome", "football", "iloveyou", 
    "princess", "monkey", "sunshine", "master", "123456789", 
    "passw0rd", "baseball", "dragon", "1234567"
]

# Variations and substitutions
variations = {
    'a': '@',
    'o': '0',
    's': '$',
    'l': '1'
}

# Keyboard patterns
keyboard_patterns = [
    "asdfgh", "zxcvbn", "qazwsx", "123qwe", "1qaz2wsx", 
    "!qaz@wsx#", "1q2w3e4r", "1qazxsw2", "qwerty123", 
    "qwertyuiop", "asdfghjkl", "zxcvbnm", "poiuytrewq", 
    "mnbvcxz", "12345", "987654321", "!@#$%^", "0987654321", 
    "1q2w3e4r5t", "qwertypoiuy"
]

# Generate possible passwords
passwords = []

# Add common words
passwords.extend(common_words)

# Add variations and substitutions
for word in common_words:
    for char, replacement in variations.items():
        passwords.append(word.replace(char, replacement))

# Add keyboard patterns
passwords.extend(keyboard_patterns)

# Add combinations of given information
info_combinations = [
    name.replace(" ", ""), 
    bday.replace("-", ""), 
    father_name.replace(" ", ""), 
    fav_player, 
    pet_name
]

for combination in itertools.product(*info_combinations):
    password = "".join(combination)
    if 8 <= len(password) <= 12:
        passwords.append(password)

# Convert passwords to set to remove duplicates
passwords_set = set(passwords)

# Print generated passwords
for password in passwords_set:
    print(password)
