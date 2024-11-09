#!/usr/bin/env python3
import argparse
import sys

def main():
    print("Welcome to the Gendiff!")
    name = input('May I have your name? ')
    print(f"Hello, {name}")


    parser = argparse.ArgumentParser(
        prog='gendiff',
        usage= 'gendiff [-h] first_file second_file',
        description='Compares two configuration files and shows a difference.',
        add_help= True
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    if len(sys.argv) > 1:
        args = parser.parse_args()
        parser.print_help()

if __name__ == '__main__':
    main()