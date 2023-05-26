def couns(i):
    print(i)
    if i <= 5:
        return i
    else:
        couns(i-1)
print(couns(10))