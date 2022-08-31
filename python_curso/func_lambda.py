# funcao normal

def func(argumento,arg2):
    return argumento * arg2

var = func(2,5)
print(var)


#funcao anonima e ou lambda

v= lambda num1,num2 : num1* num2

print(v(9,2))

lista =[
    ['P1', 10],
    ['P2', 2],
    ['P1', 8],
    ['P1', 5],
    ['P1', 4],
    ['P1', 12],
]

def ordernar(produto):
    return produto[1]

lista.sort(key=ordernar ,reverse=True)

print(lista)