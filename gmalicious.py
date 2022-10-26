def malicious():
    # creating an empty list
    mlst = []

    # number of elements as input
    n = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, n):
        ele = int(input())

        mlst.append(ele)  # adding the element

    return mlst

