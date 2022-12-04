def reverse_string(myStr):
    if len(myStr) % 4 == 0 :
        return "".join(reversed(myStr))
    return myStr 

print(reverse_string(input("Enter Your Word: ")))           
print(reverse_string('python'))    