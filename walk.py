from os import listdir
from os.path import isdir, join

def walk_directory(d, indent):
    # Implement recursive directory walk here
    merged_directory = join(d,f)
    for f in listdir(d):
        print(indent + f)
        if isdir(merged_directory):#if it is true
            walk_directory(merged_directory, 2 * indent)
        

# '.' means current directory
walk_directory('Desktop', ' ')
