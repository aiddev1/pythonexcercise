def sumi(lst):
    if lst == []:
        return 0
    return lst[0] + sumi(lst[1:])
lst=[1,2,3]

print(sumi(lst))