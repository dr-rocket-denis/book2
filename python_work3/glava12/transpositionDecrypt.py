import math
def main():
    #myMessage = 'Cenoonommstmme oo snnio s s c'
    myMessage = input('Введите сообщение которое хотите дешифровать\n> ')
    myKey = input('Введите ключ\n>')
    plaintext = decryptMessage(myKey, myMessage)
    print(plaintext + '|')
def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    numOfShaidedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShaidedBoxes):
            column = 0
            row += 1
    return ''.join(plaintext)
if __name__ == "__main__":
    main()
