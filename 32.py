def find(lst):
    duplicate = set()
    indices = {}
    for i, item in enumerate(lst):
        if item in indices:
            duplicate.add(item)
            indices[item].append(i)
        else:
            indices[item]=[i]
    return indices

lst =[1,2,3,4,1,2,3,4]
print(find(lst))