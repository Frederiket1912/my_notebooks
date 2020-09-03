import utils as u

if __name__ == '__main__':
    files = ['input.txt', 'output.txt', 'file_output.txt']
    md_files = ['md1.md', 'md2.md']
    # u.write_files_from_folder(
    #    'C:\\Users\\frede\\Desktop\\4.Semester\\Python\\docker_notebooks\\notebooks\\my_notebooks\\my_modules')

    # u.write_files_from_folder_and_subfolders(
    #    'C:\\Users\\frede\\Desktop\\4.Semester\\Python\\docker_notebooks\\notebooks\\my_notebooks\\my_modules')

    # u.print_first_line_from_files(files)

    # u.print_emails(files)

    u.write_headlines_to_file(md_files, 'mdheadlines.txt')
