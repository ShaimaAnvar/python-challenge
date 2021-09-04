n=int(input())
d={}
for i in range(n):
    key,value = input().split(" ")
    d[key]=value

x = input()
while len(x)>0:
    if x in d:
        print(x+"="+d[x])
    else:
        print("Not found")
    x=input()
