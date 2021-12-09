import sys, cryptomath, random
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
def main():
    myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    myKey = 2894
    myMode = 'encrypt'
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
        f = 'Зашифрованный'
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
        f = 'Дешифрованный'
    print('Ключ: %s' % (myKey))
    print('%s текст:' % (f))
    print(translated)
def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)
def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Шифр является слабым, если ключ A равен 1. Выберите другой ключ.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Шифр является слабым, если ключ B равен 1. Выберите другой ключ.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Ключ A должен быть больше 0, а ключ B должен находиться в диапазоне от 0 до %s.' % (len(SYMBOLS - 1)))
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Ключ A (%s) и размер набора символов (%s) не являются относительно простыми. Выберите другой ключ.' % (keyA, len(SYMBOLS)))
def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol
    return ciphertext
def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModeInverse(keyA, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext
def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB
if __name__ == '__main__':
    main()