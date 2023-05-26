def is_all_digits(s):
    t = 0
    f=0
    for i in s:
        if i.isdigit():
            t+=1
        elif i.isalpha():
            f+=1
    return t , f

s = '12345aaa'
print(is_all_digits(s))