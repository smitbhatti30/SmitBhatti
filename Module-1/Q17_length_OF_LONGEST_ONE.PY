mylist= ['PHP', 'Android','Python','C','c++']

list = []
for i in mylist:
    list.append((len(i)))
list.sort()
print(list)
print(list[-1:])