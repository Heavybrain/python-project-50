#!/usr/bin/env python3
import argparse
import sys
import json




def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        usage= 'gendiff [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration files and shows a difference.',
        add_help= True
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', 
                        help='set format of output')

    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
        parser.print_help()
        return 


if __name__ == '__main__':
    main()



def generate_diff(file_name1, file_name2, directory='path/to/your/json/files'):
    # Формируем полные пути к файлам
    file_path1 = os.path.join(directory, file_name1)
    file_path2 = os.path.join(directory, file_name2)

    # Чтение и загрузка JSON-файлов
    try:
        with open(file_path1) as file1, open(file_path2) as file2:
            data1 = json.load(file1)
            data2 = json.load(file2)
    except FileNotFoundError as e:
        return f"Error: {e}"

    diff = []
    all_keys = set(data1) | set(data2)  # Объединяем ключи из обоих файлов

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 != value2:
            if key in data1 and key in data2:
                diff.append(f"Key '{key}' has different values: '{value1}' in '{file_name1}' and '{value2}' in '{file_name2}'.")
            elif key in data1:
                diff.append(f"Key '{key}' is present in '{file_name1}' but not in '{file_name2}'.")
            else:
                diff.append(f"Key '{key}' is present in '{file_name2}' but not in '{file_name1}'.")

    if not diff:
        return "No differences found."
    
    return "\n".join(diff)