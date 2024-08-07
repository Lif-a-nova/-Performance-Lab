"""
Задание 1:
Программа, которая выводит путь,
двигаясь интервалом длины m по заданному массиву.
Концом будет являться первый элемент.
Началом одного интервала является конец предыдущего.
Путь - массив из начальных элементов полученных интервалов.

Параметры передаются в качестве аргументов командной строки:
python task1.py -n arg1 -m arg2
"""

import argparse

from typing import List


class ListNode:
    """Класс для создания кругового массива """
    def __init__(self, max_n: int):
        self.max_n: int = max_n
        self.queue: list = [None] * self.max_n
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def is_empty(self):
        """Функция проверки массива на пустоту """
        return self.size == 0
  
    def push(self, value: int):
        """Функция добавления элемента в массив """
        if self.size < self.max_n:
            if self.queue[self.tail] is not None:
                self.head += 1
                if self.head == self.max_n:
                    self.head = 0
            self.queue[self.tail] = value
            self.tail += 1
            if self.tail == self.max_n:
                self.tail -= 1
            self.size += 1 

    def shift(self, steps: int):
        """Функция смещения элементов массива """
        for i in range(steps):
            self.queue.append(self.queue.pop(0))


def way_array(n: int, m: int) -> List[int]:
    """Функция поиска пути по круговому массиву """
    array = ListNode(n)
    for i in range(1, n + 1):
        array.push(i)
    collector = []
    stop_arr = array.queue[0]
    while stop_arr:
        arr = array.queue[:m]
        collector.append(arr)
        if stop_arr == arr[-1]:
            break
        array.shift(m - 1)
    result = [ x[0] for x in collector]
    return result

def createParser():
    """Функция обработки аргументов командной строки """
    parser = argparse.ArgumentParser()
    for name in ('-n', '-m'):
        parser.add_argument(name, type=int, required=True)
    return parser

if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    try:
        n: int = args.n
        if n == 0:
            raise ValueError('Массив (n) не может быть равен 0')
        m: int = args.m
        if m == 0:
            raise ValueError('Интервал (m) не может быть равен 0')
        result = way_array(n, m)
        print(''.join(map(str, result)))
    except Exception as err:
        print(f'{err.__class__}: {err}')
