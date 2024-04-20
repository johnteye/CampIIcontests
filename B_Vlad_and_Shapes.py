t = int(input())

for _ in range(t):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(str, input().strip())))

    count = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):

            if matrix[row][col] == "1":
                count += 1

        if count == 1:
            print("TRIANGLE")   
            break
        elif count > 1:
            print("SQUARE")
            break

    print(matrix)
