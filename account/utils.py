import random
import string

def generate_username(length=8):
    letters = string.ascii_lowercase
    digits = string.digits
    all_characters = letters + digits
    username = ''.join(random.choice(all_characters) for _ in range(length))
    return username