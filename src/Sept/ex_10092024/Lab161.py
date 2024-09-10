import os

full_path_file = os.path.join("/Users/promode/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/pra", "pramod.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)
