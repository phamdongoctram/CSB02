while True:
    number = float(input("Input a positive number: "))
    try:
        if number > 0:
            print("Thank you.")
            break
    except ValueError:
        print("Input a positive number: ")
