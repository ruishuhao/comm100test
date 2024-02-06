from DataGenerator import generate_random_email

valid_credentials = [
    {"email": "valid_email1@example.com", "password": "valid_password1"},
    {"email": "valid_email2@example.com", "password": "valid_password2"}
]

invalid_credentials = [
    {"email": generate_random_email(), "password": "invalid_password1"},
    {"email": generate_random_email(), "password": "invalid_password2"}
]
