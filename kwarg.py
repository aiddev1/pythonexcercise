def func(**k):
    ans = k['a'] * k['b'] * k['c']
    return ans

print(func(a=1,b=2,c=3))