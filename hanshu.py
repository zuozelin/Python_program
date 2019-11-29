# def func (a, b, c):
#   print('a= %s' %a)
#   print('b= %s' %b)
#   print('c= %s' %c)

# func(1, c=2, b=3)


# 取得参数的个数
# def howlong(first, *other):
#   print( 1 + len(other))

# howlong(123)

# var1 = 123

# def func():
#   global var1
#   var1 = 456
#   print(var1)

# func()
# print(var1)


# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))  # except



# for i in range(10,20,2):
#  print(i)

# def frange(start, stop, step):
#   x = start
#   while x < stop:
#     yield x
#     x += step

# for i in frange(10, 20, 0.5):
#   print(i)


# def true():return True
# lambda : True

# def add(x, y): return x+y
# lambda x,y:x+y


# lambda x:x<= (month, day)

# def func1(x):
#   return x<= (month, day)


# lambda item:item[1]

# def func2(item):
#   return item[1]


###  Python中常见的内建函数
# filter() map() reduce() zip()

# a=[1,2,3,4,5,6,7]
# list(filter(lambda x:x>2 , a))

def func():
  a = 1
  b = 2
  return a+b

def sum(a):
  def add(b):
    return a+b
  return add

# add 函数名称或函数的引用
# add() 函数的调用

num1 = func()
num2 = sum(2)

print(num2(4))


# print(type(num1))
# print(type(num2))


