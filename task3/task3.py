"""
Задание 3:
Программа, которая формирует файл report.json с заполненными полями
value для структуры tests.json на основании values.json.

На вход программы передается три пути к файлу:
python task3.py 'путь к values' 'путь к tests' 'путь к report' 

ps: важно указать путь в 'ковычках'
"""

import json
import sys

from pathlib import Path


def read_json(file_path: Path):
    """Функция распаковки файла .json """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def write_json(data, file_path: Path):
    """Функция записи файла .json """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
    return(f'Файл успешно записан: {file_path}')

def iterate_nested_dict(nested_dict, value_dict: dict):
    """Функция заполнения поля 'value' """
    for item in nested_dict:
        test_id = item['id']
        if test_id in value_dict:
            item['value'] = value_dict[test_id]
        if 'values' in item:
            iterate_nested_dict(item['values'], value_dict)
    return nested_dict

def merge_data(values_data, tests_data):
    """Функция формирования файла report """
    value_dict = {}
    for item in values_data['values']:
        value_dict[item['id']] = item['value']
    
    report_data = tests_data.copy()
    nested_dict = report_data['tests']
    report_data['tests'] = iterate_nested_dict(nested_dict, value_dict)
    return report_data


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Ошибка: укажите три пути к файлам')
        sys.exit(1)
    else:
        values_file = sys.argv[1]
        tests_file = sys.argv[2]
        report_file = sys.argv[3]

        values_data = read_json(values_file)
        tests_data = read_json(tests_file)
        report_data = merge_data(values_data, tests_data)
        
        result = write_json(report_data, report_file)
        print(result)
