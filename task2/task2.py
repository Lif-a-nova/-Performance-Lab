"""
Задание 2:
Программа, которая рассчитывает положение точки
относительно окружности.
Координаты центра окружности и его радиус считываются из файла-1.
Координаты точек считываются из файла-2.

Пути к файлам передаются программе в качестве аргументов:
python task2.py 'путь к файлу-1' 'путь к файлу-2'

ps: важно указать путь в 'ковычках'
"""

import math
import sys


DISTANCE = {
    0: 'точка лежит на окружности',
    1: 'точка внутри',
    2: 'точка снаружи',
}
MAX_POINTS = 100


class ManagedFile:
    """Класс для чтения файлов """
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        """Функция открытия файла """
        try:
            self.opened_file = open(self.filename, 'r')
        except FileNotFoundError:
            print(f'Невозможно открыть файл {self.filename}')
        return self.opened_file
    
    def __exit__(self, exc_type, exc_val, exc_traceback):
        """Функция закрытия файла """
        if exc_type is None:
            self.opened_file.close()
            return True
        else:
            return True

def distance(radius, cx, cy, px, py):
    distance = math.sqrt((px - cx)**2 + (py - cy)**2)
    if distance > radius:
        return 2
    elif distance < radius:
        return 1
    else:
        return 0

def point_position(circle: list, points: list) -> int:
    """Функция рассчета положения точек относительно окружности """
    center, radius = circle
    center_x = center[0]
    center_y = center[1]
    result = []
    for point in points:
        point_x, point_y = point
        pos = distance(radius, center_x, center_y, point_x, point_y)
        result.append(pos)
    return result
    
def read_circle_data(file_path) -> list:
    """Функция извлечения данных для окружности """
    circle = []
    with ManagedFile(file_path) as f:
        x, y = map(float, f.readline().strip().split())
        circle.append((x, y))
        radius = float(f.readline().strip())
        circle.append(radius)
    return circle

def read_points_data(file_path) -> list:
    """Функция извлечения данных для точек """
    points = []
    with ManagedFile(file_path) as f:
        for line in f:
            x, y = map(float, line.strip().split())
            if len(points) < MAX_POINTS:
                points.append((x, y))
            else:
                break
    return points


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Ошибка: укажите два пути к файлам')
        sys.exit(1)
    else:
        circle_file = sys.argv[1]
        points_file = sys.argv[2]
        
        circle = read_circle_data(circle_file)
        points = read_points_data(points_file)
        result = point_position(circle, points)
        print('\n'.join(map(str, result)))
