import sys
from collections import Counter
import load_dictionary
dict_file = load_dictionary.load('m.txt')
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)
ini_name = input('Введите имя: ')
def find_anagrams(name, word_list):
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    print(*anagrams, sep='\n')
    print('\nОстальные буквы = {}'.format(name))
    print('Число остальных букв = {}'.format(len(name)))
    print('Число остальных анаграмм (реальных слов) = {}'.format(len(anagrams)))
def process_choice(name):
    while True:
        msg = '\nВведите Enter чтобы продолжить, или введите \'#\' для выхода.\n---> '
        choice = input(msg)
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
            left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print('Не сработает! Попробовать ещё один вариант!', file=sys.stderr)
    name = ''.join(left_over_list)
    return choice, name
def main():
    name = ''.join(ini_name.lower().split())
    name = name.replace('-', '')
    limit = len(name)
    phrase = ''
    running = True
    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print('Длина анаграмного слоаосочетания = {}'.format(len(temp_phrase)))
            find_anagrams(name, dict_file)
            print('Текущее анаграмное словосочетание =', end=' ')
            print(phrase, file=sys.stderr)
            choice, name = process_choice(name)
            phrase += choice + ' '
        elif len(temp_phrase) == limit:
            print("\n***** ГОТОВО!!! *****\n")
            print("Анаграмма имени =", end=" ")
            print(phrase, file=sys.stderr)
            print()
            try_again = input('\n\nПопробовать ещё? (нажмите Enter, или "n" чтобы выйти)\n--> ')
            if try_again.lower() == "n":
                running = False
                sys.exit()  
            else:
                main()
if __name__ == '__main__':
    main()