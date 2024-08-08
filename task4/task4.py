"""
Задание 4:
Программа, которая выводит минимальное количество ходов,
требуемых для приведения всех элементов к одному числу.
За один ход можно уменьшить или увеличить число массива на 1.

Элементы массива читаются из файла,
переданного в качестве аргумента командной строки:
python task4.py 'путь к файлу'

ps: важно указать путь в 'ковычках'
"""

import sys

from statistics import median


MIN_STEP = 1


def min_steps(nums):
    """Функция рассчета минимального количества ходов """
    check_args = []
    for num in nums:
        remainder = num % MIN_STEP
        check_args.append(remainder)

    if all(x == check_args[0] for x in check_args):
        target = int(median(nums))
        total_steps = 0
        for num in nums:
            step = abs(num - target)
            total_steps += step
        return total_steps
    
    return(
        f'Элементы массива не одинаково кратны\n'
        f'Их не возможно привести к одному числу'
    )

def read_file(file_path):
    """Функция извлечения данных элементов массива """
    with open(file_path, 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]
    return data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Ошибка: укажите один путь к файлу')
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        nums = read_file(input_file)
        steps = min_steps(nums)
        print(steps)
