largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break

        else:
            num = int(num)

            if largest is None:
                largest = num
            elif num > largest:
                largest = num
            if smallest is None:
               smallest = num
            elif num < smallest:
                smallest = num

    except:
        print("Invalid Input")

    # if largest is None:
    #     largest = num
    # elif num > largest:
    #     largest = num
    # if smallest is None:
    #     smallest = num
    # elif num < smallest:
    #     smallest = num

print("Maximum", largest)
print("Smallest", smallest)
