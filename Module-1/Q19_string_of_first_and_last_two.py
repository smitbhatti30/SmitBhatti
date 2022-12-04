def string(myStr):
    length = len(myStr)
    if length> 2:
        return myStr[0:2] + myStr[-2:]
    else:
        return'' 

print(string(input("Enter Your Word: ")))