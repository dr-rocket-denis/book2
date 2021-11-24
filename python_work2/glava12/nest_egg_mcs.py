import sys
import random
import matplotlib.pyplot as plt
def read_to_list(file_name):
    with open(file_name) as in_file:
        lines = [float(line.strip()) for line in in_file]
        decimal = [round(line / 100, 5) for line in lines]
        return decimal
def default_input(prompt, default=None):
    prompt = '{} [{}]'.format(prompt, default)
    response = input(prompt)
    if not response and default:
        return default
    else:
        return response
print("\nNote: Input data should be in percent, not decimal!\n")
try:
    bonds = read_to_list('10-yr_TBond_returns_1926-2013_pct.txt')
    stocks = read_to_list('SP500_returns_1926-2013_pct.txt')
    blend_40_50_10 = read_to_list('S-B-C_blend_1926-2013_pct.txt')
    blend_50_50 = read_to_list('S-B_blend_1926-2013_pct.txt')
    infl_rate = read_to_list('annual_infl_rate_1926-2013_pct.txt')
except IOError as e:
    print("{}. \nTerminating program.".format(e), file=sys.stderr)
    sys.exit(1) 
investment_type_args = {'bonds': bonds, 'stocks': stocks, 'sb_blend': blend_50_50, 'sbc_blend': blend_40_50_10}
print("   stocks = SP500")
print("    bonds = 10-летние казначейские облигации")
print(" sb_blend = 50% SP500/50% казн.обл")
print("sbc_blend = 40% SP500/50% казн.обл/10% нал.\n")
print("Нажмите клавишу ВВОД, чтобы принять значение по умолчанию, указанное в [скобках]. \n")
invest_type = default_input("Введите тип инвестиций: (акции, облигации, их сочетаниеб scbs_blend): \n", 'облигаций').lower()
while invest_type not in investment_type_args:
    invest_type = input("Недействительные инвестиции. Введите тип инвестиций, как указано в приглашении: ")
start_value = default_input("Ввод стартовой стоимости инвестиций: \n", '2000000')
while not start_value.isdigit():
    start_value = input("Неверный ввод! Только входное целое число: ")
withdrawal = default_input("Ввод ежегодного вывода средств до уплаты налогов (в сегодняшних долларах): \n", '80000')
while not withdrawal.isdigit():
    withdrawal = input("Неверный ввод! Только входное целое число: ")
min_years = default_input("Минимальный стаж выхода на пенсию: \n", '18')
while not min_years.isdigit():
    min_years = input("Неверный ввод! Только входное целое число: ")
most_likely_years = default_input("Введите наиболее вероятные годы выхода на пенсию: \n", '25')
while not most_likely_years.isdigit():
    most_likely_years = input("Неверный ввод! Только входное целое число: ")
max_years = default_input("Введите максимальные годы выхода на пенсию: \n", '40')
while not max_years.isdigit():
    max_years = input("Неверный ввод! Только входное целое число: ")
num_cases = default_input("Введите количество запущенных обращений: \n", '50000')
while not num_cases.isdigit():
    num_cases = input("Неверный ввод! Только входное целое число: ")
if not int(min_years) < int(most_likely_years) < int(max_years) or int(max_years) > 99:
    print("\nПроблема с входными годами.", file=sys.stderr)
    print("Требуется, чтобы мин. < наиболее вероятн. < макс, где макс. <= 99.", file=sys.stderr)
    sys.exit(1)
def montecarlo(returns):
    case_count = 0
    bankrupt_count = 0
    outcome = []
    while case_count < int(num_cases):
        investments = int(start_value)
        start_year = random.randrange(0, len(returns))
        duration = int(random.triangular(int(min_years), int(max_years), int(most_likely_years)))
        end_year = start_year + duration
        lifespan = [i for i in range(start_year, end_year)]
        bankrupt = 'no'
        lifespan_returns = []
        lifespan_infl = []
        for i in lifespan:
            lifespan_returns.append(returns[i % len(returns)])
            lifespan_infl.append(infl_rate[i % len(infl_rate)])
        for index, i in enumerate(lifespan_returns):
            infl = lifespan_infl[index]
            if index == 0:
                windraw_infl_adj = int(withdrawal)
            else:
                windraw_infl_adj = int(windraw_infl_adj * (1 + infl))
            investments -= windraw_infl_adj
            investments = int(investments * (1 + i))
            if investments <= 0:
                bankrupt = 'yes'
                break
        if bankrupt == 'yes':
            outcome.append(0)
            bankrupt_count += 1
        else:
            outcome.append(investments)
    case_count+= 1 
    return outcome, bankrupt_count
def bankrupt_prob(outcome, bankrupt_count):
    total = len(outcome)
    odds = round(100 * bankrupt_count / total, 1)
    print("\nТип инвестиций: {}".format(invest_type))
    print("Начальное значение: ${:,}".format(int(start_value)))
    print("Ежегодный вывод средств: ${:,}".format(int(withdrawal)))
    print("Годы на пенсии (мин-мл-макс): {}-{}-{}".format(min_years, most_likely_years, max_years))
    print("Количество запусков: {:,}\n".format(len(outcome)))
    print("Вероятность того, что деньги кончатся: {}%\n".format(odds))
    print("Средний результат: ${:,}".format(int(sum(outcome) / total)))
    print("Минимальный результат: ${:,}".format(min(i for i in outcome)))
    print("Максимальный результат: ${:,}".format(max(i for i in outcome)))
    return odds
def main():
    outcome, bankrupt_count = montecarlo(investment_type_args[invest_type])
    odds = bankrupt_prob(outcome, bankrupt_count)
    plotdata = outcome[:3000]
    plt.figure('Результат по делу (показаны первые {} запуски)'.format(len(plotdata)), figsize=(16, 5)) 
    index = [i + 1 for i in range(len(plotdata))]
    plt.bar(index, plotdata, color='black')
    plt.xlabel('Симулируюмые жизни', fontsize=18)
    plt.ylabel('Остаток 💲', fontsize=18)
    plt.ticklabel_format(style='plain', axis='y')
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.title('Вероятность исчерпания денег = {}%'.format(odds), fontsize=20, color='red')
    plt.show()
if __name__ == '__main__':
    main()