import random
import string

def generate_random_email():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + "@example.com"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))