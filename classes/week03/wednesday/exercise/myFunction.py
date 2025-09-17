x = 5
print(id(x))
def myFunc(num):
    print(id(num))
    z += 1
    print(id(z))
    return z

y = myFunc(x)
print(id(y))