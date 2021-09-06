p1 = input('Enter 1st name :  ').lower()
p2 = input('Enter 2nd name :  ').lower()
lp1, lp2 = list(p1), list(p2)
print(lp1, lp2)              
for i in range(len(lp1)):
    print(lp1[i])
    if lp1[i] in lp2:
        lp1.remove(lp1[i])
        lp2.remove(lp2[i])
        print(lp1)
        i -= 1

print(lp1+lp2)
