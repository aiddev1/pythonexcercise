def count_occurrences(lst):
    counts={}
    for i in lst:
        counts[i] = counts.get(i , 0)+1

    return counts

lst=[1,2,3,2,1,3,2,2,4]

print(count_occurrences(lst))