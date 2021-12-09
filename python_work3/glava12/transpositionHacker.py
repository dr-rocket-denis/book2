from typing import Text
import detectEnglish, transpositionDecrypt
def main():
    myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""
    hackedMessage = hackTransposition(myMessage)
    if hackedMessage == None:
        print('Не удалось взломать шифрование.')
    else:
        print('hacked message: ')
        print(hackedMessage)
def hackTransposition(message):
    print('Взлом...')
    print('Нажмите <Сtrl+D> чтобы выйти.')
    for key in range(1, len(message)):
        print('Используется ключ #%s...' % (key))
        decryptedText = transpositionDecrypt.decryptMessage(key, message)
        if detectEnglish.isInglish(decryptedText):
            print('Возможный взлом шифрования:')
            print('Ключ %s: %s' % (key, decryptedText[:100]))
            print('\nВведите D, если готово, что-нибудь еще, чтобы продолжить взлом:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None
if __name__ == '__main__':
    main()