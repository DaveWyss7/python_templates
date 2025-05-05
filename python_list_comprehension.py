"""
List Comprehension
"""
emails = [
    'batman@gmail.com',
    'captain.america@@gmail.com',
    'spider.man@gmail.com',
    'thor@hotmail.com',
    'super.women@hotmai.com'
]

# List comprehension to filter valid emails
usernames = [
    email.split('@', maxsplit=1)[0] for email in emails if '@' in email and '.' in email.split('@')[1]
]
# Print the list of usernames
print(usernames)
