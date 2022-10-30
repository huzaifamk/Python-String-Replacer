def replace_strings():
    # Open the file sales.txt.
    infile = open('./files/test.txt', 'r')

    # Read the file's contents.
    contents = infile.read()

    # Print the file's contents.
    print(contents)

    # Close the file.
    infile.close()

    # Replace each dollar sign with a pound sign.
    contents = contents.replace('$', '£')

    # Open the file sales.txt.
    outfile = open('./files/new_file.txt', 'w')

    # Write the modified contents to the file.
    outfile.write(contents)

    # Close the file.
    outfile.close()

replace_strings()