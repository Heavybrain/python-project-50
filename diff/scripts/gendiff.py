#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        usage= 'gendiff [-h] first_file second_file',
        description='Compares two configuration files and shows a difference.',
        add_help= True
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.print_help()

if __name__ == '__main__':
    main()