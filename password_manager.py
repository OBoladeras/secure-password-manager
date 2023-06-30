import os
import base64
import hashlib
from cryptography.fernet import Fernet

password_file = "data.txt"


def get_encryption_key():
    key_file = "encryption_key.txt"

    if os.path.exists(key_file):
        with open(key_file, "rb") as file:
            encryption_key = file.read()
    else:
        encryption_key = generate_key()
        with open(key_file, "wb") as file:
            file.write(encryption_key)

    return encryption_key


def generate_key():
    return Fernet.generate_key()


def encrypt_password(password, encryption_key):
    cipher_suite = Fernet(encryption_key)
    cipher_text = cipher_suite.encrypt(password.encode())

    return cipher_text


def decrypt_password(cipher_text, encryption_key):
    cipher_suite = Fernet(encryption_key)
    plain_text = cipher_suite.decrypt(cipher_text)

    return plain_text.decode()


def hash_password(password):
    salt = b"kb3p9sa8NSJ8783As"
    hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)

    return hashed_password.hex()


def save_password(site, username, password):
    encryption_key = get_encryption_key()

    encrypted_password = encrypt_password(password, encryption_key)
    encoded_password = base64.urlsafe_b64encode(encrypted_password).decode()
    with open(password_file, "a") as file:
        file.write(f"{site},{username},{encoded_password}\n")


def retrieve_password(site, username):
    encryption_key = get_encryption_key()

    with open(password_file, "r") as file:
        for line in file:
            stored_site, stored_username, encoded_password = line.strip().split(",")
            if stored_site == site and stored_username == username:
                encoded_password += "=" * (4 - len(encoded_password) % 4)
                encrypted_password = base64.urlsafe_b64decode(encoded_password)
                decrypted_password = decrypt_password(
                    encrypted_password, encryption_key
                )

                return decrypted_password


def generate_password():
    import random

    password = ""
    characters = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*-+=|:?,/"
    )

    for i in range(random.randint(15, 20)):
        password += random.choice(characters)

        if random.randint(15, 20) == i:
            password += str(i)

    return password


def password_rate(password):
    rate = 0
    numbers = 0
    symbols = 0
    upper_case = 0
    lower_case = 0

    if len(password) <= 15:
        rate = len(password) / 15
        required = len(password) / 4 - 2
    else:
        rate = len(password) / 10
        required = len(password) / 4

    if rate > 2:
        rate = 2

    for character in str(password):
        if character.isnumeric():
            numbers += 1
        elif character.isupper():
            upper_case += 1
        elif character.islower():
            lower_case += 1
        else:
            symbols += 1

    labels = [numbers, symbols, upper_case, lower_case]

    for unit in labels:
        if unit >= required:
            rate += 2
        elif unit == 0:
            rate += 0
        else:
            rate += unit / required

    return rate
