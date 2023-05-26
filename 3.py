def count_duplicate(lst):
    return len(lst) - len(set(lst))
lst =[1,2,3,4,5,1,2,3]
print(count_duplicate(lst))