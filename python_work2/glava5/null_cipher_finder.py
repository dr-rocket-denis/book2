import sys
import string
def load_text(file):
    with open(file) as f:
        return f.read().strip()
def solve_null_cipher(message, lookahead):
    for i in range(1, lookahead + 1):
        plaintext = ''
        count = 0 
        found_first = True
        for char in message:
            if char in string.punctuation:
                count = 0
                found_first = True
            elif found_first is True:
                count += 1
            if count == i:
                plaintext += char
        print('используя сдвиг {} после знака препинания = {}'.format(i, plaintext))
    print()
def main():
    filename = 't.txt'
    try:
        loaded_message = load_text(filename)
    except IOError as e:
        print('{}. Завершение программы.'.format(e))
        sys.exit(1)
    print('\nПЕРВОНАЛЬНОЕ СООБЩЕНИЕ =')
    print('{}'.format(loaded_message), '\n')
    print('\nсписок проаеряемых знаков препинания = {}'.format(string.punctuation), '\n')
    message = ''.join(loaded_message.split())
    while True:
        lookahead = input("\nКоличество букв для проверки после знака препинания: ")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Пожалуйста, введите номер.", file=sys.stderr)           
    print()
    solve_null_cipher(message, lookahead)
if __name__ == '__main__':
    main()