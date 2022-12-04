# Write a Python program to copy the contents of a file to another file.

with open('t1.txt','r') as firstfile, open('t4.txt','a') as secondfile:
	
	for line in firstfile:
        
			secondfile.write(line)
