print("Tetration Calculator (Hyper4)")


def program():
    number = input("Number = ")
    power = input("What are you bringing your number to the power of? ")
    limit = input("Num of repeats (How many arrows up?) (How tall is this power tower?) = ")

    count = 0

    print()
    print("LAYER NUM: " + str(count))
    print()
    print(number)
    print()
    while count <= int(limit):
        number = int(number) ** int(power)
        count = count + 1
        print("Saved number into number.txt\n" + "LAYER NUM: " + str(count))
        print("\n\n\n\n" + str(number) + "\n\n\n\n")
        with open('number.txt', 'w') as file:
            file.write(str(number))



print("\nTetration is repeated exponentiation. It isn't used a lot, but is very hand for huge numbers. \n"
      "This will take a while, so the greatest number the program got to will be saved into a file. Enjoy the calculator!\n")
program()


exit = input("Press (1) to close, Press (2) to use the calculator again.")
if exit == "2":
    program()
