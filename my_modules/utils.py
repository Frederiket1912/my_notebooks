import os
import io_module as io
import argparse


def write_files_from_folder(path):
    files = os.listdir(path)
    io.write_list_to_file('file_output.txt', files)


def write_files_from_folder_and_subfolders(path):
    files = os.listdir(path)
    io.append_list_to_file('file_output.txt', files)
    for file in files:
        if(os.path.isdir(path + '\\' + file)):
            write_files_from_folder_and_subfolders(path + '\\' + file)


def print_first_line_from_files(files):
    for file in files:
        io.print_first_line_in_file(file)


def print_emails(files):
    for file in files:
        io.print_file_content_if_email(file)


def write_headlines_to_file(files, output_file):
    for file in files:
        io.write_headlines_from_md_file(output_file, file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program that can write content from one file to another')
    parser.add_argument('--dir', help='name of directory to look for files in')
    parser.add_argument(
        '--files', help='list of files to print first line from', nargs='*')
    parser.add_argument(
        '--outputfile', help='file to write to, if needed for method')
    args = parser.parse_args()
    # write_files_from_folder(args.dir)
    # write_files_from_folder_and_subfolders(args.dir)
    # print_first_line_from_files(args.files)
    # print_emails(args.files)
    write_headlines_to_file(args.files, args.outputfile)
