from cryptography.fernet import Fernet

key_file_settings = "C:/Users/HP/Desktop/Projects/Python/Robin_Beta_v4/Robin_AI/Data/Settings.key"
key_file_commands = "C:/Users/HP/Desktop/Projects/Python/Robin_Beta_v4/Commands.key"


def generate(file_given):
    key = Fernet.generate_key()

    with open(file_given, 'wb') as file:
        file.write(key)


def encryption_file(file_key, file):
    with open(file_key, 'rb') as f:
        key_assigned = f.read()

    fernet = Fernet(key_assigned)

    with open(file, 'rb') as file_assigned:
        original = file_assigned.read()

    encrypt_file = fernet.encrypt(original)

    with open(file, 'wb') as f_encrypted:
        f_encrypted.write(encrypt_file)


def decryption_file(file_key, file):
    with open(file_key, 'rb') as f:
        key = f.read()

    fernet = Fernet(key)

    with open(file, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypt_file = fernet.decrypt(encrypted)

    with open(file, 'wb') as _file:
        _file.write(decrypt_file)


generate(key_file_commands)
# encryption_file(key_file_settings, "C:/Users/HP/Desktop/Projects/Python/Robin/Robin_AI/Data/Robin_Settings.json")
# decryption_file(key_file_settings, "C:/Users/HP/Desktop/Projects/Python/Robin/Robin_AI/Data/Robin_Settings.json")
