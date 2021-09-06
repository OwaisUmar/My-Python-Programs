def decoder(r, c, m):
    dec = []
    for i in range(r):
        for i in range(c):
            if m[r][c].isalnum():
                dec.append(m[r][c])
    return dec


n,m = input().split()
mat = []
for i in range(m):
    row = input().split()
    mat.append(row)
decoder(n, m, mat)
