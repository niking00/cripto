from random import randint

ELEM_CHAR_COUNT = 163
ELEM_CHAR = [i for i in range(32, 127)] + [128, 129] +\
            [ord(i) for i in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"]
ITERATIONS = 15

def cipher_text(user_text, code):
    # преобразование в аски
    cipher = [str(ord(i)) for i in user_text]

    # шифрация по сдвигу
    random_num = randint(10, 60)
    counter = 0
    for symbol in cipher:
        sym = ELEM_CHAR[(ELEM_CHAR.index(int(symbol)) + counter * code + counter * random_num + random_num ** 2) % ELEM_CHAR_COUNT]
        if sym < 100:
            cipher[counter] = '00' + str(sym)
        elif sym < 1000:
            cipher[counter] = '0' + str(sym)
        else:
            cipher[counter] = str(sym)
        counter += 1

    # добавления ключа - рандома
    counter = len(cipher)
    for symbol in str(random_num):
        sym = ELEM_CHAR[(ELEM_CHAR.index(int(ord(symbol))) + counter * code + counter * 123 + counter ** 2) % ELEM_CHAR_COUNT]
        if sym < 100:
            cipher.append('00' + str(sym))
        elif sym < 1000:
            cipher.append('0' + str(sym))
        else:
            cipher.append(str(sym))
        counter += 1
    return ''.join(cipher)

def decipher_text(cipher, code):
    # разбиение на элементы
    decipher = [cipher[i] + cipher[i + 1] + cipher[i + 2] + cipher[i + 3] for i in range(0, len(cipher), 4)]

    # расшифровка рандома
    counter = len(decipher) - 2
    for symbol in decipher[-2:]:
        sym = ELEM_CHAR[(ELEM_CHAR.index(int(symbol)) - counter * code - counter * 123 - counter ** 2) % ELEM_CHAR_COUNT]
        decipher[counter] = str(sym)
        counter += 1

    # декод преобразования со сдвигом
    counter = 0
    random_num = int(chr(int(decipher[-2])) + chr(int(decipher[-1])))
    for symbol in decipher:
        sym = ELEM_CHAR[(ELEM_CHAR.index(int(symbol)) - counter * code - counter * random_num - random_num ** 2) % ELEM_CHAR_COUNT]
        decipher[counter] = str(sym)
        counter += 1

    return ''.join([chr(int(i)) for i in decipher][:-2])

def decoder_ASCII(text):
    return ''.join([chr(int(text[i] + text[i+1] + text[i+2] + text[i+3])) for i in range(0, len(text), 4)])

def coder_ASCII(text):
    cipher = []
    for symbol in text:
        if ord(symbol) < 100:
            cipher.append('00' + str(ord(symbol)))
        elif ord(symbol) < 1000:
            cipher.append('0' + str(ord(symbol)))
        else:
            cipher.append(str(ord(symbol)))
    return ''.join(cipher)

def cipher(text, code):
    try:
        text = text.replace("\t", chr(128))
        text = text.replace("\n", chr(129))

        text = [text[i] for i in range(len(text))]
        for elem in text:
            if not ord(elem) in ELEM_CHAR:
                text[text.index(elem)] = ' '
        text = ''.join(text)
        text = ' '.join(text.split())

        cod = cipher_text(text, code)
        for i in range(ITERATIONS):
            cod1 = decoder_ASCII(cod)
            cod = cipher_text(cod1, code)
        cod1 = decoder_ASCII(cod)
        return cod1
    except:
        return "Вы ввели что-то не корректно"

def decipher(text, code):
    try:
        cod = coder_ASCII(text)
        for i in range(ITERATIONS):
            cod1 = decipher_text(cod, code)
            cod = coder_ASCII(cod1)
        cod1 = decipher_text(cod, code)
        cod1 = cod1.replace(chr(128), "\t")
        cod1 = cod1.replace(chr(129), "\n")
        return cod1
    except:
        return "Вы ввели некорректный шифр или персональный код"

if __name__ == '__main__':
    print(cipher(input()))
    print(decipher(input()))