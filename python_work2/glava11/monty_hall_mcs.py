import random
def user_prompt(prompt, default=None):
    prompt = '{} [{}]: '.format(prompt, default)
    responce = input(prompt)
    if not responce and default:
        return default
    else:
        return responce
num_runs = int(user_prompt('Введите число прогонов', '20000'))
first_choice_wins = 0
pick_change_wins = 0
doors = ['a', 'b', 'c']
for i in range(num_runs):
    winner = random.choice(doors)
    pick = random.choice(doors)
    if pick == winner:
        first_choice_wins += 1
    else:
        pick_change_wins += 1
print("Выигрыши с оригинальным выбором = {}.".format(first_choice_wins))
print("Выигрыши с измененным выбором = {}.".format(pick_change_wins))
print("Вероятность выигрыша при первоначальном предположении: {:.2f}".format(first_choice_wins / num_runs))
print("Вероятность выигрыша при переключении: {:.2f}".format(pick_change_wins / num_runs))
input("\nНажмите клавишу Ввода для выхода.")