# write a program to print multiplication table of "n" using for loop in reverse order


num = (int(input("Enter Your Number: ")))
for i in range(10,0,-1):
    print(f"{num}x{i}={num*i}")