import math
import random, sys, transpositionCipher, transpositionDecrypt
def main():
    random.seed(42)
    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test #%s: "%s..."' % (i + 1, message[:50]))
        for key in range(1, int(len(message) / 2)):
            encrypted = transpositionCipher.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)
            if message != decrypted:
                print("Несоответствие с ключом %s и сообщением %s" % (key, message))
                print("Расшифрованный как: " + decrypted)
                sys.exit()
    print("Тест на шифр транспозиции пройден.")
if __name__ == '__main__':
    main()
