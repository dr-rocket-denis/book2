plaintext = """Давай пересечем реку и отдохнём в тени деревьев."""
def main():
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)
def prep_plaintext(plaintext):
    message = "".join(plaintext.split())
    message = message.upper()
    print('открытый текст = {}'.format(plaintext))
    return message
def build_rails(message):
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails
def encrypt(rails):
    ciphertext = ' '.join([rails[i:i+5] for i in range(0, len(rails), 5)])
    print('шифротекст = {}'.format(ciphertext))
if __name__ == '__main__':
    main()