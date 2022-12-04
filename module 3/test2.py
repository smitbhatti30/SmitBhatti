# Write a Python program to append text to a file and display the text.

def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("i love photography.\n")
                myfile.write("i have a canon camera.")
        txt = open(fname)
        print(txt.read())
file_read('t2.txt')
