import affineCipher, detectEnglish, cryptomath
SILENT_MODE = False
def main():
    myMessage = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""
    hackedMessage = hackAffine(myMessage)
    if hackedMessage != None:
        print(hackedMessage)
    else:
        print('Не удалось взломать шифрование.')
def hackAffine(message):
    print('Взламывается...')
    print('(Нажмите <Ctrl+D> чтобы выйти)')
    for key in range(len(affineCipher.SYMBOLS)**2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue
        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Попробованный Ключ %s... (%s)' % (key, decryptedText[:40]))
        if detectEnglish.isInglish(decryptedText):
            print('\nВозможный взлом шифрования:')
            print('Ключ: %s' % (key))
            print("Расшифрованное сообщение: " + decryptedText[:200])
            print('\nВведите D, если готово, что-нибудь еще, чтобы продолжить взлом')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None
if __name__ == '__main__':
    main()