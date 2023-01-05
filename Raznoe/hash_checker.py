import hashlib

import os


def gen_hash(password: str):
    salt = os.urandom(8)
    user_password = password
    user_key = hashlib.pbkdf2_hmac(
        'sha256',
        user_password.encode('utf-8'),
        salt,
        100000
    )
    storage = salt + user_key
    return storage


def check_hash(salty_hash: bytes, password: str) -> bool:
    salt = salty_hash[:8]
    key = salty_hash[8:]
    pass_to_check = password
    check_key = hashlib.pbkdf2_hmac(
        'sha256',
        pass_to_check.encode('utf-8'),
        salt,
        100000
    )
    if check_key == key:
        return True
    else:
        return False


def main():
    password = '123'
    password_check = check_hash(gen_hash(password), password)
    return password_check

if __name__ == '__main__':
    print(main())