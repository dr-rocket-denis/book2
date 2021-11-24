import sys
def load(file):
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print('{}\nошибка при открытии {}. Завершение программы.'.format(e, file), file=sys.stderr)
        sys.exit(1)