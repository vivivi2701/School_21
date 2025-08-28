import sys

def caesar_cipher(text, shift, mode):
    result = []

    for char in text:
        if char.isalpha():
            if not ('A' <= char <= 'Z' or 'a' <= char <= 'z'):
                raise Exception('Скриптонит не поддерживает не латинский язык. Пасиба.')

            base = ord('A') if char.isupper() else ord('a')

            if mode == 'encode':
                offset = (ord(char) - base + shift) % 26
            elif mode == 'decode':
                offset = (ord(char) - base - shift) % 26

            else:
                raise Exception('Неверный режим- используйте decode или encode. Пасиба.')

            result.append(chr(base + offset))
        else:
            result.append(char)
    return ''.join(result)



def main():
    if len(sys.argv) != 4:
        print('Usage: python3 caesar.py encode "ssh -i private.key user@school21.ru" 12')
        print('Usage: python3 caesar.py decode "eet -u bduhmfq.wqk geqd@eotaax21.dg" 12')
        return

    mode = sys.argv[1].lower()  # [4] = 12
    text = sys.argv[2]

    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception('Сдвиг должен быть целым числом')


    for ch in text:
        if 'А' <= ch <= 'я':
            raise Exception('Скриптонит поддерживает только латинский язык')

    output = caesar_cipher(text, shift, mode)
    print(output)

    '''
    if mode == 'decode':
        for char in string:
            if char in ['-', '.', ' ', '@', 21] :
                continue
            else:
                if (65 <= char <= 90) or (97 <= char <= 122):
                    char = chr(ord(char) + num)
        print(string)

    elif mode == 'encode':
        for char in string:
            if char in ['-', '.', ' ', '@', 21] :
                continue
            else:
                if (65 <= char <= 90) or (97 <= char <= 122):
                    char = chr(ord(char) - num)
        print(string)
    '''

if __name__ == '__main__':
    main()
