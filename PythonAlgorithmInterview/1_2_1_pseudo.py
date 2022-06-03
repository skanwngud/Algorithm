def fizzbuzz():
    for i in range(1, 100):
        print_number = True

        if i % 3 == 0:
            print("Fizz")
            print_number = False

        elif i % 5 == 0:
            print("Buzz")
            print_number = False

        if print_number == True:
            print(i)
        print()


if __name__ == "__main__":
    fizzbuzz()