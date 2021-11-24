import sys
from itertools import count, permutations
from collections import Counter
import load_dictionary
def main():
    name = input('Введите имя: ')
    name = name.lower()
    word_list_ini = load_dictionary.load('m.txt')
    trigrams_filtered = load_dictionary.load('least-lickey_trigrams.txt')
    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)
def prep_words(name, word_list_ini):
    print('длина первоначального списка word_list = {}'.format(len(word_list_ini)))
    len_name = len(name)
    word_list = [word.lower() for word in word_list_ini
                if len(word) == len_name]
    print('длина нового списка word_list = {}'.format(len(word_list)))
    return word_list
def cv_map_words(word_list):
    vowels = 'aeiouy'
    cv_mapped_words = []
    for word in word_list:
        temp = ''
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 't'
        cv_mapped_words.append(temp)
    total = len(set(cv_mapped_words))
    target = 0.05
    n  = int(total * target)
    count_pruned = Counter(cv_mapped_words).most_common(total - n)
    filtered_cv_map = set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print('длина множества filtered_cv_map = {}'.format(len(filtered_cv_map)))
    return filtered_cv_map
def cv_map_filter(name, filtered_cv_map):
    perms = {''.join(i) for i in permutations(name)}
    print("длина первоначального множества перестановок = {}".format(len(perms)))
    vowels = 'aeiouy'
    filter_1 = set()
    for candidate in perms:
        temp = ''
        for letter in candidate:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        if temp in filtered_cv_map:
            filter_1.add(candidate)                
    print("# вариантов после фильтра filter_1 = {}".format(len(filter_1)))
    return filter_1
def trigram_filter(filter_1, trigrams_filtered):
    filtered = set()
    for candidate in filter_1:
        for triplet in trigrams_filtered:
            triplet = triplet.lower()
            if triplet in candidate: 
                filtered.add(candidate)
    filter_2 = filter_1 - filtered        
    print("# вариантов после фильтра filter_2 = {}".format(len(filter_2)))
    return filter_2
def letter_pair_filter(filter_2):
    filtered = set()
    rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv', 'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
    first_pair_rejects = ['ld', 'lm', 'lt', 'lv', 'rd', 'rl', 'rm', 'rt', 'rv', 'tl', 'tm']
    for candidate in filter_2:
        for r in rejects:
            if r in candidate:
                filtered.add(candidate)
        for fp in first_pair_rejects:
            if candidate.startswith(fp):
                filtered.add(candidate)
    filter_3 = filter_2 - filtered    
    print("# вариантов после фильтра filter_3 = {}".format(len(filter_3)))
    if 'voldemort' in filter_3:
        print("Волдеморт найден!", file=sys.stderr)
    return filter_3
def view_by_letter(name, filter_3):
    print("Оставшиеся письма = {}".format(name))
    first = input("выберите начальную букву или нажмите клавишу Ввод, чтобы увидеть все: ")
    subset = []
    for candidate in filter_3:
        if candidate.startswith(first):
            subset.append(candidate)
    print(*sorted(subset), sep='\n')
    print("Число вариантов начинающихся с {} = {}".format(first, len(subset)))
    try_again = input("Попробовать еще раз? (Нажмите Enter или любую другую клавишу для выхода):")
    if try_again.lower() == '':
        view_by_letter(name, filter_3)
    else:
        sys.exit()
if __name__ == '__main__':
    main()