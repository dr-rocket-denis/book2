from random import randint
import string
import load_dictionary
input_message = "Панель в восточном конце слайдов часовни"
message = ''
for char in input_message:
    if char in string.ascii_letters:
        message += char
print(message, "\n")
message = "".join(message.split())
word_list = load_dictionary.load('m.txt')
vocab_list = []
for letter in message:
    size = randint(6, 10)
    for word in word_list:
        if len(word) == size and word[2].lower() == letter.lower() and word not in vocab_list:
            vocab_list.append(word)
            break
if len(vocab_list) < len(message):
    print("Список слов слишком мал. Попробуйте увеличить словарь или сократить сообщение!")
else:        
    print("Словарные слова для блока 1: \n", *vocab_list, sep="\n")     