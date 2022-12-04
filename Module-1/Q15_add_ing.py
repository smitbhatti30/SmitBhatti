myStr= input('Enter Your String: \n')
length = len(myStr)

if length > 2:
    if myStr[-3:] == "ing":
        myStr += 'ly'
    else:
        myStr += 'ing'

print(myStr)      