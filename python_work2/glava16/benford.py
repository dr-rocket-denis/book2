import sys
import math
from collections import defaultdict
import matplotlib.pyplot as plt
BENFORD = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
def load_data(filename):
    with open(filename) as f:
        return f.read().strip().split('\n')
def count_first_digits(data_list):
    first_digits = defaultdict(int)
    for sample in data_list:
        if sample == '':
            continue
        try:
            int(sample)
        except ValueError as e:
            print(e, file=sys.stderr)
            print('Образцы должны быть целыми числами. Завершение работы', file=sys.stderr)
            sys.exit(1)
        first_digits[sample[0]] += 1
    keys = [str(digit) for digit in range(1, 10)]
    for key in keys:
        if key not in first_digits:
            first_digits[key] = 0
    data_count = [v for (k, v) in sorted(first_digits.items())]
    total_count = sum(data_count)
    data_pct = [(i / total_count) * 100 for i in data_count]
    return data_count, data_pct, total_count
def get_expected_counts(total_count):
    return (round(p * total_count / 100) for p in BENFORD)
def chi_square_test(data_count, expected_counts):
    chi_square_stat = 0
    for data, expected in zip(data_count, expected_counts):
        chi_square = math.pow(data - expected, 2)
        chi_square_stat += chi_square / expected
    print("\nПроверочный статистический показатель хи-квадрат = {:.3f}".format(chi_square_stat))
    print("Критическое значение при разноречении 0.05 составляет 15.51.")
    return chi_square_stat < 15.51
def bar_chart(data_pct):
    fig, ax = plt.subplots()
    index = [i + 1 for i in range(len(data_pct))]
    fig.canvas.set_window_title('Процент первых цифр')
    ax.set_title('Данные против значений Бенфорда', fontsize=15)
    ax.set_ylabel('Частота, %', fontsize=16)
    ax.set_xticks(index)
    ax.set_xticklabels(index, fontsize=14)
    rects = ax.bar(index, data_pct, width=0.95, color='black', label='Data')
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height, '{:0.1f}'.format(height), ha='center', va='bottom', fontsize=13)
    ax.scatter(index, BENFORD, s=150, c='red', zorder=2, label='Benford')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(prop={'size':15}, frameon=False)
    plt.show()
def main():
    while True:
        filename = input("\nИмя файла с КОЛИЧЕСТВЕННЫМИ данными: ")
        try:
            data_list = load_data(filename)
        except IOError as e:
            print("{}. Попробовать ещё раз.".format(e), file=sys.stderr)
        else:
            break
    data_count, data_pct, total_count = count_first_digits(data_list)
    expected_counts = get_expected_counts(total_count)
    print("\nнаблюдаемые числа = {}".format(data_count))
    print("ожидаемые кол-ва = {}".format(expected_counts), "\n")
    print("Вероятности первой цифры: ")
    for i in range(1, 10):
        print("{}: наблюдаемый: {:.3f}  ожидаемый: {:.3f}".format(i, data_pct[i - 1] / 100, BENFORD[i - 1] / 100))
    if chi_square_test(data_count, expected_counts):
        print("Наблюдаемое распределение соответствует ожидаемому распределению.")
    else:
        print("Наблюдаемое распределение не соответствует ожидаемому.", file=sys.stderr)       
    bar_chart(data_pct)    
if __name__ == '__main__':
    main()