def flatten(lst):
    flatten_lst= [item for i in lst for item in i]
    return flatten_lst

lst=[[1,2,3],[4,5],[6,7,8,9]]
print(flatten(lst))