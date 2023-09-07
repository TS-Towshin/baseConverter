import anyBaseToDecimal
import decimalToAnyBase

print("'exit' to quit")
while True:
    print("[1] Decimal to another base")
    print("[2] Any base to decimal")

    choice = input(">>> ")
    if choice == '1':
        N = int(input("Decimal number: "))
        b = int(input("Enter the base: "))
        decimalToAnyBase.convert(N, b)

    elif choice == '2':
        N = input("Enter the value: ")
        b = int(input("Enter the base: "))
        anyBaseToDecimal.convert(N, b)

    elif choice == 'exit':
        exit()

    else:
        print("please enter a valid option")
