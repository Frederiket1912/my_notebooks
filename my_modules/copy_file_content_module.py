import argparse

#parser = argparse.ArgumentParser(description='A program that can write content from one file to another')
#parser.add_argument('inputfile', default='input.txt', help='the name of the inputfile')
#parser.add_argument('outputfile', default='output.txt', help='The name of the outputfile')
#args = parser.parse_args()

def copy_content(inputfile, outputfile):
    

    with open(inputfile) as input_file:
        lines = input_file.readlines()

    with open(outputfile, 'w') as output_file:
        for line in lines:
            output_file.write(line)

    with open(outputfile) as file_to_read:    
        print(file_to_read.readlines())