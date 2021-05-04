import weakref


class Car:
    pass


x = 10
print(type(x))
y = x
if (id(x) == id(y)):
    print("x and y refer to same object")
x += 1
if (id(x) == id(y)):
    print("x and y different to same object")
z = 10
if (id(y) == id(z)):
    print("y and z refer to same object")
else:
    print("y and z different to same object")
z = Car()

print("z memory location: ", hex(id(z)))
r = weakref.ref(z)
print("before: ", r)
z = None
print("After: ", r)
