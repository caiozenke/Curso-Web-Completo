
import re

t = 'Teste de expressão regular aqui ok teste teste'
teste= t.lower()
 

#FUCTION SEARCH
achar_search = re.search(r'aqui', teste) # ele para quando achar a variavel
print(f'search retorna um Match :{achar_search}') #retorna um match



if achar_search: 
    print(f'A palavra existe')
else:
    print('erro')
    
    
print()
#FUNCTION  FIND_ALL
achar_findall = re.findall(r'teste', teste) #vai buscar todos os teste 
print(f'find_all retornou uma lista : {achar_findall}') # retorna uma lista

"""c= 0
for teste in achar_findall: #mostra os testes da lista 
    c += 1
    print(f'{teste}{c}')
"""   
    
print()
#FUNCTION SUB
achar_sub = re.sub(r'teste','substitui',teste) #substitui  a palava por outra
print(type(achar_sub))
print(achar_sub)



print()

#Compilar FUCTION COMPILE MAIS FACIL

print('funcao compile testes:')
com_compile = re.compile(r'teste') # PASSA A STRING QUE SERÁ ACHADA E USE AS FUNÇÕES ANTERIORES

print(com_compile.search(teste))
print(com_compile.findall(teste))
print(com_compile.sub('DEF', teste ))
