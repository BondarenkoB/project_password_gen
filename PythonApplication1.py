   #creating pass gen

# Combining the character types requested by the user
characters = letters + numbers + special_chars

# Generating the password
password = "".join(random.choice(characters) for i in range(password_length))
