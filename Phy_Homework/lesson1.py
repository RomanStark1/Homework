name = 'Tom'
age = 33
weight = 89.4
b = bytes([46, 46, 46])
s = ['hi', 'hello', 'bye']
y = ('hi', 'hello', 'bye')
setNew = {'hi', 'hello', 'bye'}
f = frozenset({'hi', 'hello', 'bye'})
d = {'a': 1, 'b': 2}

print(name, type(name))
print(age, type(age))
print(weight, type(weight))
print(b, type(b))
print(s, type(s))
print(y, type(y))
print(setNew, (setNew))
print(f, type(f))
print(d, type(d))

st1 = 'hi'
st2 = 'by'
st3 = st1 + st2
print(st3)

in1 = 4
in2 = 2
in3 = in1 + in2
print(in3)

print(type(in1),type(in2))

in4 = in1 / in2
print(int(in4))

in5 = in1 * in2;
print(in5)

in6 = in1 // in2;
print(in6)

in6 = in1 % in2;
print(in6)

z = (7 + 12) ** 3 + 7 * 4 - 44 / 2**4
print (z)