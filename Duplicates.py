L = input().split()
Temp_List = []
for x in L:
    if x not in Temp_List:
        Temp_List.append(x)
for i in Temp_List:
    print(i, end=' ')