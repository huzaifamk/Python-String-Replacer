from genericpath import isfile
from msilib.schema import Directory
from ntpath import join
from os import listdir


def replace_strings():
    # Open a file in read mode
    infile = open('./files/test.txt', 'r')

    # Read the file's contents to a variable
    contents = infile.read()

    # Print the file's contents
    print(contents)

    # Close the file
    infile.close()

    # Replace each dollar sign with a pound sign
    contents = contents.replace('$', '£')

    # Open the file sales.txt in write mode
    outfile = open('./files/new_file.txt', 'w')

    # Write the modified contents to the file
    outfile.write(contents)

    # Close the file
    outfile.close()


def replace_string_in_multiple_files():

    files = ['file_one.txt', 'file_two.txt', 'file_three.txt']

    # Read file names from a directory
    Directory = './files'
    files = [f for f in listdir(Directory) if isfile(join(Directory, f))]
    print(files)

    for file in files:

        infile = open('./many_files/' + file, 'r')

        contents = infile.read()

        print(contents)

        infile.close()

        contents = contents.replace('Python', 'C++')

        i = '1'

        outfile = open('./many_files/' + file+'_'+i, 'w')

        outfile.write(contents)

        outfile.close()


replace_strings()
replace_string_in_multiple_files()
