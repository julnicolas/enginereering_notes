import os

# Shows all files in the python dir (recursively)
working_dir = '/home/julien/projects/julnicolas/enginereering_notes'
for p, d, f, in ((path, directory, files) for path, directory, files in os.walk(working_dir) if 'python' in path):
    print(f"{p}:")
    print(f)
    print('')
