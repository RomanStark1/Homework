
#1) Создать переменную типа String
#2) Создать переменную типа Integer
#3) Создать переменную типа Float
#4) Создать переменную типа Bytes
#5) Создать переменную типа List
#6) Создать переменную типа Tuple
#7) Создать переменную типа Set
#8. Создать переменную типа Frozen set
#9) Создать переменную типа Dict
#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
#11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
#12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
#13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
#14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
#15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
#16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
#17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.
#Выгрузить файл в Git репозиторий.




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