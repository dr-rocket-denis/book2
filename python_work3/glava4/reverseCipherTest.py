message = input('Введите сообщение которое хотите зашифровать\n>  ')
b = []
i = list(message)
for g in range(len(message)):
    f = i.pop(-1)
    b.append(f)
print(''.join(b))