# Import regex module;
import re

# Open the file in read mode and read lines;
# we use 'with as' so we won't have to close the file after reading;
with open('Anna.txt', 'r') as file:
    # The readlines() method reads the entire file all at once and returns them
    # as a list of strings; this is useful because it saves you from having to
    # run 'readline()' repeatedly;
    lines = file.readlines()

# Open the file in write mode to overwrite;
with open('Anna2.txt', 'w') as file:
    for line in lines:
        # Find the first period in the line;
        match = re.search(r'\.', line)
        if match:
            # Get the index of the first period, then subtract 1;
            index = (match.start() - 1)
            
            # Write only the first "half" of the line to the file (up to the character
            # before the period, not inclusive; basically just trying to delete the 
            # versions of the apps, they are unnecessary);
            file.write(line[:index] + '\n')

# CLEAN-UP---in the new file that was created, we should eliminate duplicate entries;

# Create a dictionary to store the strings and keep track of how many times they
# appear in the text file;
line_dict = {}

with open ('Anna2.txt', 'r') as file:
    # Again, we use 'readlines()' to read all lines simultaneously and store 
    # them as a list;
    lines = file.readlines()
    for line in lines:
        # If line has not appeared yet in our dictionary, we add it and set
        # its value to 1;
        if line not in line_dict:
            line_dict[line] = 1
        # Else, we add 1 to the value of the line as it is already in our 
        # dictionary;
        else:
            line_dict[line] += 1

# Open file in write mode to overwrite;
with open('Anna2.txt', 'w') as file:
    # Check how many times the line appears in dictionary;
    for line, count in line_dict.items():
        # This verification of line count is unnecessary as every line/string
        # in the dictionary must be printed, but it's not hurting anything;
        if count > 1:
            file.write(line)
        else:
            file.write(line)