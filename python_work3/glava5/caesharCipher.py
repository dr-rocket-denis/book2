SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
message = input("Сообшение:  ")
key = 4#input("Ключ: ")
#while not key.isdigit():
 #   key = input('Введите только ЧИСЛО\n> ')
  #  key = int(key)
mode = input("1 - зашифровать\n2 - дешифровать\n> ")
while mode != '1' and mode != '2':
    mode = input('Введите только ЧИСЛО и только СУЩЕСТВУЮЩИЙ вариант\n> ')
if mode.strip() == '1':
    mede = 'encrypt'
if mode.strip() == '2':
    mode = 'decrypt'
translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            translatedIndex = symbolIndex + int(key)
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - int(key)
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol
print(translated)