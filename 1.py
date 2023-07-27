decision = input('Введите "Расшифровка" если хотите расшифровать послание, "Шифровка" если зашифровать')
if decision == 'Расшифровка':
    n = int(input('Введите смещение элемнтов шифра:'))
    text = input('Введите послания:')
    for letter in text:
        decryption = ord(letter) - n
        if decryption < 97:
            decryption += 26
        print('Расшифровка:', chr(decryption), end='')
elif decision == 'Шифровка':
    n = int(input('Введите смещение элемнтов шифра:'))
    text = input('Введите послания:')
    for letter in text:
        decryption = ord(letter) + n
        if decryption < 97:
            decryption += 26
        print(chr(decryption), end='')