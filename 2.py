def lst_to_cama(lst):
    return ','.join(map(str,lst))

lst = [1,2,3,4,5]
print(lst_to_cama(lst))