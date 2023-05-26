def delete(lst):
    return list(set(lst))

lst = [1,2,3,4,3,2,1,2,5]
print(delete(lst))