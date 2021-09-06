def spiral(r, c, mat):
    ir = 0  # Inner row start index
    ic = 0  # Inner col start index
    while ir < r and ic < c:
        # left column top to bottom
        for i in range(ir, r):
            print(mat[i][ic], end=' ')
        ic += 1

        # bottom row left to right
        for i in range(ic, c):
            print(mat[r - 1][i], end=' ')

        r -= 1

        if ic < c:
            # right column bottom to top
            for i in range(r - 1, ir - 1, -1):
                print(mat[i][c - 1], end=' ')

        c -= 1

        if ir < r:
            # top Row left to right
            for i in range(c - 1, ic - 1, -1):
                print(mat[ir][i], end=' ')

        ir += 1
    return mat


n = int(input())
matrix = []
for x in range(n):
    l = input().split()
    matrix.append(l)

spiral(n, n, matrix)

for i in range(n):
    for j in range(n):
        if j != n - 1:
            print(matrix[i][j], end=" ")
        else:
            print(matrix[i][j], end="")
    if i != n - 1:
        print()

