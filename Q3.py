def product(a):
    if len(a)==0:
        return 0
    elif len(a)==1:
        return a[0]
    else:
        pro=a[len(a)-1] * a[len(a-2)]
    print(pro)

list=[1,2]
product(list)