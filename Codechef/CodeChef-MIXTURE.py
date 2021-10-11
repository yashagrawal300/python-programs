# cook your dish here
T = int(input("enter the number of test cases :"))
for i in range(T):
    a = int(input("\nenter the number of solid units:"))
    if a == 0:
        b = int(input("please enter the number of liquid units :"))
        while b == 0:
            b = int(input("please enter a non nul number of liquid units :"))
        print("Liquid")
    else:
        b = int(input("please enter the number of liquid units :"))
        if b == 0:
            print("Solid")
        else:
            print("Solution")
