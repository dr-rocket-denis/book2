import sys, random
print('Подберите имя своему другу.')
first = [
    'nurmambet', 'gavnyk', 'kakah', 'vrednyh'
]
lost = [
    'cralnykov', 'dolbonosov', 'balbesyatskiy', 'dgmotov'
]
while True:
    fN = random.choice(first)
    lN = random.choice(lost)
    print('\n\n\t{} {}'.format(fN, lN), file=sys.stderr)
    try_again = input('\n\nPoprobuyte eshe? (n/y)\n\t--> ')
    if try_again.lower() == 'n':
        break
