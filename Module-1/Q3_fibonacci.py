numbers = int(input("enter number Range: "))

n1 = 0
n2 = 1
sum = 0

if numbers<= 0:
    print("Enter positive Integer")

elif numbers == 1 :
    print(f"Fibonacci sequence upto {numbers}")
    print(n1)

else :
    print("Fibonacci sequence: ")
    for i in range(numbers):
        print(sum,end=" ")
        n1 = n2
        n2 = sum
        sum = n1+n2