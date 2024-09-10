import os

# operating system - files, path related to the OS

# print(os.name) # posix - unix based - system mac or linus, windows - nt
# if os.name == 'posix':
#     print("using mac")
# else:
#     print("windows")

# print(os.getcwd())
# os.chdir("/Users/promode/Downloads/postman_collections/project1")
# print(os.getcwd())
# os.mkdir('new_directory')
# os.makedirs('parent/child/grandchild')
# print(os.listdir('.'))
# for file in os.listdir('.'):
#     print(file)


# os.remove('example.txt')
# os.rmdir('new_directory')

# os.rename('old_name.txt', 'new_name.txt')

full_path = os.path.join('/Users/promode/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024', 'file.txt')
# "/Users/promode/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/file.text"


print(full_path)

print(os.path.exists('file.txt'))

print(os.path.isfile('file.txt'))

print(os.path.isdir('directory_name'))






