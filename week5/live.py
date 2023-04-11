#import os

#path = "c:/Users/alebel/Documents/programming_introduction/week5/my_file.txt"
#current_script_path = os.path.abspath(__file__)
#current_directory = os.path.dirname(current_script_path)

#print(current_directory)
#with open(path, "r") as f:
#    lines = f.readlines()

#    for line in lines:
#        print(line)

#path2 = "c:/Users/alebel/Documents/programming_introduction/week5/my_file2.txt"
#with open(path2, "w") as handle:
#    handle.write("My new file line")

recipe = "Banane orange in mix"
path = "."
with open(path, "w") as f:
    f.write(recipe)
