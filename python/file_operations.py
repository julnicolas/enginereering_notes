from os import remove as os_rm

# Open file for writing
# trunc content
# create if doesn't exist
#
# call f.close if `with` is not used
with open('blah.txt', 'w') as f:
    f.writelines(['hello\n', 'world\n'])

# Open file for appending (a+ to enable reading)
# create if doesn't exist
# Read line per line
with open('blah.txt', 'a') as f:
    f.write('new line\n')

# Open file for reading
# create if doesn't exist
# Read all lines at once
with open('blah.txt', 'r') as g:
    for line in g.readlines():
        print(line, end='')

# Open file for reading
# create if doesn't exist
# Read line per line
with open('blah.txt', 'r') as h:
    line = h.readline()
    while line != '':
        print(line, end='')
        line = h.readline()

# Open file for reading
# create if doesn't exist
# Read line per line
with open('blah.txt', 'r') as h:
    for line in h:
        print(line)

# Delete file
os_rm('blah.txt')

