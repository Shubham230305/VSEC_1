print("Please Select Operation -\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n")

choice = int(input("Select Operation (1-4): "))

n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))

if choice == 1:
    print(n1, "+", n2, "=", n1+n2)
elif choice == 2:
    print(n1, "-", n2, "=", n1-n2)
elif choice == 3:
    print(n1, "*", n2, "=", n1*n2)
elif choice == 4:
    print(n1, "/", n2, "=", n1/n2)
else:
    print("INVALID INPUT")
