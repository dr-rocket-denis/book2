import sys
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict
cmudict = cmudict.dict()
def main():
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    build_dict = input('\nПостроить словарь исключений в ручную? (y/n)\n> ')
    if build_dict.lower() == 'n':
        sys.exit()
    else:
        missing_words_dict = make_exceptions_dict(exceptions)
        save_exceptions(missing_words_dict)
def load_haiku(filename):
    with open(filename) as in_file:
        haiku = set(in_file.read().replace('-', ' ').split())
        return haiku
def cmudict_missing(word_set):
    exceptions = set()
    for word in word_set:
        word = word.lower().strip(punctuation)
        if word.endswith("'s") or word.endwith("`s"):
            word = word[:-2]
        if word not in cmudict:
            exceptions.add(word)
    print('\nисключения: ')
    print(*exceptions, sep='\n')
    print('\nЧисло уникальных слов в корпусе хокку = {}'.format(len(word_set)))
    print('Число слов в корпусе слов не из cmudict = {}'.format(len(exceptions)))
    membership = (1 - (len(exceptions) / len(word_set))) * 100
    print('членство в cmudict = {:.1f}'.format(membership + '%'))
    return exceptions
def make_exceptions_dict(exsceptions_set):
    missing_words = {}
    print('Введите число слогов в слове. Ошибки можно исправить в конце. \n')
    for word in exsceptions_set:
        while True:
            num_sylls = input('Введите число слогов в {}: '.format(word))
            if num_sylls.isdigit():
                break
            else:
                print('                   Недопустимый ответ!', file=sys.stderr)
        missing_words[word] = int(num_sylls)              
    print()
    pprint.pprint(missing_words, width=1)
    print("\nВнесите изменения в Словарь Перед сохранением?")
    print("""
    0 - Выход и сохранение
    1 - Добавьте слово или Измените количество слогов 
    2 - Удалить слово
    """)
    while True:
        choice = input("\nВведите выбор: ")   
        if choice == '0':
            break
        elif choice == '1':
            word = input("\nСлово, которое нужно добавить или изменить: ")
            missing_words[word] = int(input("Введите числовые слоги в {}: ".format(word)))
        elif choice == '2':
            word = input("\nВведите слово для удаления: ")
            missing_words.pop(word, None)       
    print("\nНовые слова или изменения слога:")
    pprint.pprint(missing_words, width=1)
    return missing_words
def save_exceptions(missing_words):
    json_string = json.dumps(missing_words)
    f = open('missing_words.json', 'w')
    f.write(json_string)
    f.close()
    print("\nФайл, сохраненный как missing_words.json")
if __name__ == '__main__':
    main()