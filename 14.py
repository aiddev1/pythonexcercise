def totla(lst):
    if lst == []:
        return 0
    return 1 + totla(lst[1:])
lst = [1,2,3]

print(totla(lst))