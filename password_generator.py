import string
import random

dict_numder_to_symbol= {'1': '!', '2': ('@', '"'), '3': ('#', '№'), '4': ('$', ';'), '5': '%', '6': ('^', ':'),
                        '7': ('&', '?'), '8': '*', '9': '(', '0': ')'}

dict_keyboard_ukr = {'a': 'ф', 'b': 'и',  'c': 'с', 'd': 'в', 'e': 'у', 'f': 'а', 'g': 'п', 'h': 'р',
                    'i': 'ш', 'j': 'о', 'k': 'л', 'l': 'д','m': 'ь', 'n': 'т', 'o': 'щ', 'p': 'з', 'q': 'й',
                    'r': 'к', 's': 'і', 't': 'е', 'u': 'г','v': 'м', 'w': 'ц', 'x': 'ч', 'y': 'н', 'z': 'я'}


def brutpass(enter_password, dictionary, modify_rule):
    for password in {'qwerty'}:
        if password == enter_password:
            return password
        else:
            for key, value in modify_rule.items():
                for i in range(len(value)):
                    password_check = password
                    password_check = password_check.replace(key, value[i])
                    print(password_check)
                    if password_check == enter_password:
                        return password_check


                    

def check_password():
    print("Введіть пароль, щоб перевірити його надійсність:")
    enter_password = input()
    print("Оберіть тип словника:\n 1-Словниковий, що адаптується до іншої мовної розкладки клавіатури"
          "\n 2-Словниковий нечутливий до заміни цифр спеціальними символами")
    choice = int(input())

    file = open("wordlist.txt", "r")
    dictionary = file.readlines()
    for i in range(len(dictionary)):
        dictionary[i] = dictionary[i].rstrip("\n")
    file.close()

    if choice == 1:
        return brutpass(enter_password, dictionary, dict_keyboard_ukr)
    if choice == 2:
        return brutpass(enter_password, dictionary, dict_numder_to_symbol)

def generator():
    print('1 - random', '2 - generator')
    ch = int(input())
    if ch == 1:
        print("Lenght of password:")
        lenght = int(input())
        while lenght < 8:
            print("Min lenght = 8. Please input again. Lenght of password:")
            lenght = int(input())

        print('1 - just letters', '2 - letters + punctuation', '3 - letters + digits',
              '4 - letters + punctuation + digits')
        ch = int(input())
        if ch == 1:
            characters = string.ascii_letters
        elif ch == 2:
            characters = string.ascii_letters + string.punctuation
        elif ch == 3:
            characters = string.ascii_letters + string.digits
        elif ch == 4:
            characters = string.ascii_letters + string.punctuation + string.digits

        password = "".join(random.choice(characters) for _ in range(0, lenght))
        return password
    elif ch == 2:
        characters = {'a': ('@', '^', '/-\\', '/*\\', '/=\\'),
                      'b': ('|3', 'I3', '!3', '(3', '/3', ')3', ']3', 'j3', '6', '13', '8'),
                      'c': ('[', '(', '<', '¢', '{', 'sea', 'see'),
                      'd': ('|)', '[)', '(|', '])', '|}', '|]', 'T)', 'I7', 'cl'),
                      'e': ('[-', '&', 'ë'),
                      'f': ('|#', ']=', '/=', '}', 'ph', '(=', '7'),
                      'g': ('[,', '&', '(_+', 'C-', 'gee', 'jee', 'cj', '(?,', '{,', '<-', '(.', '9'),
                      'h': ('|-|', '\\-/', '/-/', '#', ']-[', '[-]', ')-(', '(-)', '|~|', '|-|', ']~[',
                            '!-!', '1-1', ':-:', '}{', '}-{', 'I+I', '{-}', '\\=\\', '|=|', '|.|', '|=|',
                            '|*|', 'aych', '?'),
                      'i': ('!', '|', 'eye', '3y3', 'ai', '¡', '1'),
                      'j': ('_|', '_/', ',_|', '_]', ',_]', '._|', '._]', ']', '</', '_)', '01'),
                      'k': ('|<', '>|', '1<', 'X', '|c', '|(', '|X', '|{', '05'),
                      'l': ('|_', 'ВЈ', '|', '|_', 'lJ', '1', '7', '07'),
                      'm': ('/\\/\\', '|\\/|', 'em', '|v|', 'IYI', 'IVI', '[V]', '^^', 'nn',
                            '//\\\\//\\\\', '(V)', '(v)', '{V}', '(\\/)', '|\\|\\', '/|\\', '/|/|',
                            '<\\/>', '.\\\\', '/^^\\', '/V\\', '|^^|', 'AA', '44', '02'),
                      'n': ('|\\|', '^/', '/\\/', '//\\\\//', '[\]', '<\\>', '{\\}', '/V', '//',
                            'И', '[]\\[]', ']\\[', '~', '03'),
                      'o': ('()', 'oh', 'p', '<>', '[]', '0', '08'),
                      'p': ('|*', '|o', '|>', '|"', '|^', '?', '9', '[]D', '|7', 'q', '|D', '66'),
                      'q': ('0_', '0,', '(,)', '<|', 'cue', '&', '9', '2', '99'),
                      'r': ('|2', '|9', '|?', '/2', 'I2', '|^', '|~', '|-', 'lz', 'В', 'I2', '[z',
                            '|`', 'l2', '.-', 'Я', '2', '44'),
                      's': ('z', 'ehs', 'es', '5', '2', '55'),
                      't': ('+', '-|-', '\'][\'', '†', '~|~', '«|»', '7', '1', '77'),
                      'u': ('|_|', '(_)', 'Y3W', 'M', '[_]', '\_/', '\_\\', '/_/', 'L|', 'v', '88'),
                      'v': ('\\/', '\\\\//', '007'),
                      'w': ('\\/\\/', 'vv', '\'//', '\\\\\'', '\\^/', '(n)', '\\X/', '\\|/', '\\_|_/',
                            '\\\\//\\\\//', '\\_:_/', ']I[', 'UU', 'dubya', '\\V/', '\\X/', 'UU', '2u',
                            'Ш', 'JL', '008'),
                      'x': ('><', '%', 'Р–', '}{', 'ecks', 'Г—', '*', ')(', '][', 'ex', '001'),
                      'y': ('`/', 'j', '`(', '-/', '\'/', '\\//', 'Ч', '7', '002'),
                      'z': ('≥', '-/_', '~/_', '-\\_', '-|_', '>_', 's', '%', '7_', '2', '003')}
        password = list()
        print("Key word:")
        key_word = input()
        while len(key_word) < 8:
            print("Min lenght = 8. Please input again. Key word:")
            key_word = input()
        for i in key_word:
            if 65 < ord(i) < 90 or 97 < ord(i) < 122:
                if 3 < ord(i) % random.randint(1, 256) < 35:
                    password.append(characters[i.lower()][random.randint(0, len(characters[i.lower()])-1)])
                else:
                    password.append(i)
        return password

if __name__ == '__main__':
    choice = 0
    while(choice != 3):
        print("Оберіть режим роботи:\n 1 - перевірка паролю на надійність \n 2 - генерування стійкого паролю \n 3 - вихід")
        choice = int(input())
        if choice == 1:
            if check_password() == None:
                print("Пароль надійний")
        elif choice == 2:
            print(*generator(), sep='')

