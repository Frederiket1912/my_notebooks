import argparse


def copy_content(inputfile, outputfile):
    with open(inputfile) as input_file:
        lines = input_file.readlines()
    with open(outputfile, 'w') as output_file:
        for line in lines:
            output_file.write(line)
    with open(outputfile) as file_to_read:
        print(file_to_read.readlines())


def print_file_content(file):
    with open(file) as file:
        print(file.readlines())


def print_file_content_if_email(file):
    with open(file) as file:
        for line in file.readlines():
            if('@' in line):
                print(line)


def print_first_line_in_file(file):
    with open(file) as file:
        print(file.readline())


def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as output_file:
        for element in lst:
            output_file.write(element + '\n')


def append_list_to_file(output_file, lst):
    with open(output_file, 'a') as output_file:
        for element in lst:
            output_file.write(element + '\n')


def write_strings_to_file(output_file, *strings):
    with open(output_file, 'w') as output_file:
        for string in strings:
            output_file.write(string + '\n')


def read_file(input_file):
    lst = []
    with open(input_file) as input_file:
        lines = input_file.readlines()
        for line in lines:
            lst.append(line.strip())
    return lst


def write_headlines_from_md_file(output_file, file):
    with open(file) as file:
        for line in file.readlines():
            if('#' in line[:1]):
                with open(output_file, 'a') as outputfile:
                    outputfile.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program that can write content from one file to another')
    parser.add_argument('--inputfile', default='input.txt',
                        help='the name of the inputfile')
    parser.add_argument('--outputfile', help='The name of the outputfile')
    parser.add_argument(
        '--extrawords', help='additional words to be added to output file or console print', nargs='*')
    args = parser.parse_args()
    if(args.extrawords and args.outputfile):
        lst1 = read_file(args.inputfile)
        lst2 = args.extrawords
        combinedLst = lst1 + lst2
        write_list_to_file(args.outputfile, combinedLst)
    elif(args.outputfile):
        lst = read_file(args.inputfile)
        write_list_to_file(args.outputfile, lst)
    elif(args.extrawords):
        lst3 = read_file(args.inputfile)
        lst4 = args.extrawords
        print(lst3 + lst4)
    else:
        print_file_content(args.inputfile)
