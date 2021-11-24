import load_dictionary
word_list = load_dictionary.load('m.txt')
anagram_list = []
name = input('Введите имя: ')
name = name.lower()
print('используемое имя = {}'.format(name))
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)
print()
if len(anagram_list) == 0:
    print('Вам нужны более крупный словарь или новое имя.')
else:
    print('Анаграммы =', *anagram_list, sep='\n')