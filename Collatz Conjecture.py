def checkNum(n):
    iterations = 1

    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
            iterations +=  1
        else:
            n = 3*n + 1
            iterations += 1
        print(n)

    print(iterations)


checkNum(256)