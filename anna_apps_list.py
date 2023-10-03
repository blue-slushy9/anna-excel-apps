# Import regex module
import re

# Open the file in read mode and read lines
with open('Anna.txt', 'r') as file:
    lines = file.readlines()

# Open the file in write mode to overwrite
with open('Anna2.txt', 'w') as file:
    for line in lines:
        # Find the first period in the line
        match = re.search(r'\.', line)
        if match:
            # Get the index of the first period, then subtract 1
            index = (match.start() - 1)
            
            # Write only the first "half" of the line to the file (up to the character
            # before the period, not inclusive; basically just trying to delete the 
            # versions of the apps, they are unnecessary)
            file.write(line[:index] + '\n')
        else:
            # If there's no period, write the whole line
            file.write(line)

# CLEAN-UP---in the new file that was created, we should eliminate duplicate entries

line_dict = {}

with open ('Anna2.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line not in line_dict:
            line_dict[line] = 1
        else:
            line_dict[line] += 1

# Open file in write mode to overwrite
with open('Anna2.txt', 'w') as file:
    for line, count in line_dict.items():
        if count > 1:
            file.write(line)
        else:
            file.write(line)