from os import remove as os_rm

with open('blah.txt', 'w') as f:
    f.writelines(['hello\n', 'world\n'])

with open('blah.txt', 'r') as g:
    for line in g.readlines():
        print(line, end='')

print('\nother method\n')

with open('blah.txt', 'r') as h:
    line = h.readline()
    while line != '':
        print(line, end='')
        line = h.readline()

os_rm('blah.txt')

