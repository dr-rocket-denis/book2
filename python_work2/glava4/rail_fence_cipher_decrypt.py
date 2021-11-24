import math, itertools
ciphertext = """ДВЙЕЕ ЕЕРКИ ТОНМТ НДРВЕ .ААПР СЧМЕУ ОДХЁВ ЕИЕЕЬ В"""
def main():
    message = prep_ciphertext(ciphertext)
    row1, row2 = split_rails(message)
    decrypt(row1, row2)
def prep_ciphertext(ciphertext):
    message = ''.join(ciphertext.split())
    print('\nшифротекст = {}'.format(ciphertext))
    return message
def split_rails(massage):
    row_1_len = math.ceil(len(massage)/2)
    row1 = (massage[:row_1_len])
    row2 = (massage[row_1_len:])
    return row1, row2
def decrypt(row1, row2):
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1.lower())
        plaintext.append(r2)
    if None in plaintext:
        plaintext.pop()
    print('ряд 1 = {}'.format(row1))
    print(f'ряд 2 = {row2}')
    print('\nоткрытый текст = %s' % (''.join(plaintext).lower()))
if __name__ == '__main__':
    main()