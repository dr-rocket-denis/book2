import sys
ciphertext = """16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"""
COLS = 4
ROWS = 5
key = """-1 2 -3 4"""
def main():
    print("\nЗашифрованный текст  = {}".format(ciphertext))
    print("Пробуем {} столбцов ".format(COLS))
    print("Пробуем {} строк".format(ROWS))
    print("Пробуем ключ  = {}".format(key))
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)       
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)       
    print("Plaintext = {}".format(plaintext))
    print()
def validate_col_row(cipherlist):
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):
        if len_cipher % i == 0:
            factors.append(i)
    print("\nДлина шифра  = {}".format(len_cipher))
    print("Допустимые значения столбца / строки включают:  {}".format(factors))
    print()
    if ROWS * COLS != len_cipher:
        print("\nОшибка - входные столбцы и строки не зависят от длины шифра. Завершение программы. ", file=sys.stderr)
        sys.exit(1)    
def key_to_int(key):
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
        or 0 in key_int:
        print("\nОшибка - проблема с ключом. Завершение.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int
def build_matrix(key_int, cipherlist):
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0: 
            col_items = cipherlist[start:stop]
        elif k > 0:  
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix
def decrypt(translation_matrix):   
    plaintext = ''
    for i in range(ROWS): 
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext
if __name__ == '__main__':
    main()