#!/usr/bin/env python3
import argparse
from diff.scripts.finding_diff import find_diff
from diff.scripts.parser import parser


def generate_diff(file_path1, file_path2,):
    data1 = parser(file_path1)
    data2 = parser(file_path2)
    diff = find_diff(data1, data2)
    return diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='first config file')
    parser.add_argument('second_file', help='second config file')
    parser.add_argument('-f', '--format', help='set format of output',)
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    diff = generate_diff(file_path1, file_path2)
    print(diff)


if __name__ == '__main__':
    main()
