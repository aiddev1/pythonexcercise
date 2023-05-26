def total(lst):
    if lst == []:
        return 0
    else:
        return 1 + total(lst[1:])
lst = [1,2,3]
print(total(lst))