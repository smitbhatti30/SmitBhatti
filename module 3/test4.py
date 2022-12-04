# //Write a Python program to read last n lines of a file ?   
n = 5

with open('t1.txt', 'r') as fp:

    lines = fp.readlines()
    total_length = len(lines)
    threshold = total_length - n

    for i, v in enumerate(lines): 
        if i >= threshold:
            print(i, v)




