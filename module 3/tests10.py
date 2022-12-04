# Write a Python program to write a list to a file.
books = ['php', 'java', 'python', 'c++', 'node.js', 'react.js']
with open('library.txt', "w") as myfile:
        for c in books:
                myfile.write("%s\n" % c)

content = open('library.txt')
print(content.read())
