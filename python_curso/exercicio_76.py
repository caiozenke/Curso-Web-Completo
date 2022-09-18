"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a  = [1, 2, 3, 4, 5, 6, 7]
lista_b  = [1, 2, 3, 4]



teste1=[(x,y) for x in lista_a for y in lista_b] #primeira tentativva mas ficava em forma de coordenadas qaundo somada
print(teste1)

#minha resolução que deu certa usei a função zip onde x interando na a e y na b
lista_soma=[(x + y) for x,y in zip(lista_a,lista_b)]
print(lista_soma)