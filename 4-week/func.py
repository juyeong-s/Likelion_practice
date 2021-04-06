# # list=['1','2','3']

# # for i in range(list):
# #     print(i)

# def sum():
#     return "나도함수랍니다."

# print(sum())

# def noreturn():
#     print("as")

# print(noreturn())4

# def manyinput(*data):
#     a, b, c=data
#     print(a)
#     print(b)
#     print(c)

# print(manyinput(1,2,'sada'))

# def manyinput(a, **data):
#     print(a)
#     print(data)

# print(manyinput(1,2,3,'da'))

# def multreturn(a=2,b):
#     plus=a+b
#     minus=a-b
#     return plus, minus

# def func(a):
#     return "메롱"

# print(func1234.__name__)

a=1

def func():
    global a
    a=9999

func()
print(a)
asas
