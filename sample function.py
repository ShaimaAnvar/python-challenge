
"""def hey(): #defining function
    print("hi")
hey() """   #calling function

"""def hey(name):
    print("my name is "+ name)
hey("ehsan")""" #passing argument

"""def hey(name):
    print("my name is "+ name)
value="john"
hey(value)"""

#arbitraty arguments

"""def hey(*values):
    print("name is "+values[0]+"age is "+str(values[1]))

hey("ehsan",2)"""

#global andlocal variables
"""value=10 #global var
def sample():
    value=30 #local var
    print(value)
sample()    
print(value) """

"""value=10
def sample():
    value=value+1
    print(value)
sample()
print(value)"""

#keyword argument
"""def sample(name,age):
    print(name,age)
sample(age=12,name="as")"""

#return value

def sample(num1,num2):
    sum=num1+num2
    return sum
result=sample(10,20)
print(result)




