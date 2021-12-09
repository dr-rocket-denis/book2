import time, sys, os, transpositionCipher, transpositionDecrypt
def main():
    inputFilename = 'frankenstein.txt'
    outputFilename = 'frankinstein.encrypted.txt'
    myKey = 10 
    myMode = 'encrypt'
    if not os.path.exists(inputFilename):
        print('Файл %s не существует. Выход...' % (inputFilename))
        sys.exit()
    if os.path.exists(outputFilename):
        print('Это приведет к перезаписи файла %s. продолжить(C) или выйти(Q)' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    print('%sing...' % (myMode.title()))
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionCipher.encryptMessage(myKey, content)
    elif myMode == "decrypt":
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion file is time: %s seconds' % (myMode.title(), totalTime))
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()
    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))
if __name__ == '__main__':
    main()