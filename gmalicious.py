def malicious():
    # creating an empty list
    mlst = []

    # number of elements as input
    try:
        n = int(input("Enter number of elements : "))
    except ValueError:
        print("try again!")
        n = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, n):
        print("Please input node id to be malicious: ")
        try:
            ele = int(input())
        except ValueError:
            print("try again!")
        mlst.append(ele)  # adding the element

    return mlst
