def my_func(inp):
    return [x for x,y in enumerate(inp) if y%2 == 0]

inp=[2,3,6,1,53,76]
print(my_func(inp))