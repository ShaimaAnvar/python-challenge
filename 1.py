n=int(input())
d={}
for i in range(n):
    key,value = input().split(" ")
    d[key]=value
querries = []
inp = input()
while len(inp)>0:
    querries.append(inp)
    inp=input()
for i in range(len(querries)):
    if querries[i] in d:
        print(querries[i]+"="+d[querries[i]])
    else:
        print("Not found")
