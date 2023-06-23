
# Array = conjunto de dados (lista)
# Um Array inicia com indíce 0

my_array = [1, 2, 3, 4, 'teste', False, True, 0.1]

print(my_array[0])  # Acessa o primeiro elemento.

print(my_array[-1])  # Acessa o último elemento.

print(my_array[1:3])  # Acessa o intervalo do elemento

print(my_array[150])  # Erro: Tentou acessar um elemento inexistente,

print(len(my_array))  # Informa o número de elementos.

my_array.sort() # ordena definitivamente

sorted([78,3,5,8,9]) # ordena momentâneamente

my_array.insert(0, 999) # Insere um elemento no array (posição, elemento)

my_array.append(456) # Insere um elemento no final obs:consome muita memoria.

my_array.remove(999) # Remove um elemento pelo item, não pelo indíce.

my_array[1] = None #Durante o processamento considerar o valor None não é nada.

del my_array[1] # Outra forma de remover um item.

min(my_array) # Elemento com valor mínimo.

max(my_array) # Elemento com valor máximo.

my_array = [-1, 2, 3, 5, 456]
print(my_array)

# Árvores Binárias: 
import bisect
bisect.bisect(my_array, 5) # Busca na lista pelo indíce muito mais rápido, (lista, indíce).
# O(n log n) = Algoritmos de busca em geral.
# O (log n) = Pelo bisect é bem mais rápido.
bisect.insort(my_array, 888) # Adiciona um  item a árvore binária.

my_array = range(10) # Gera os indíces de acordo com o número sequêncial

list(my_array) # Lista o array

two_dimentions_array = [[123, 456], [789, 321]] # Cria um array de 2 dimensões.
print(two_dimentions_array)

two_dimentions_array[0][0] # Acessa o indíce 0, 0.
two_dimentions_array[0] # Acessa a primeira linha.
two_dimentions_array[1] # Acessa a segunda linha.


A = [1, 2, 3]
B = A # Cria um ponteiro, e todas as alterações de A passam para B.
print(A)
print(B)
B[0] = 999

a = [1, 2, 3]
b = list(a) # "Deep Copy" Faz uma cópia da lista sem alterar a principal.
print(a)
print(b)
b[0] = 999

a = [{'test': 123, 'bbb': 456}] # Lista que contém dicionários
b = a
b[0]['test'] = 999

import copy # Biblioteca para cópias mais profundas
b = copy.copy(a) # Cria uma cópia, e, altera a cópia.
b[0]['test'] = 999

b = copy.deepcopy(a) # Cria uma cópia, e, altera a cópia. Não altera a lista matriz. Usar em lista complexas.
b[0]['test'] = 999


a = [1, 2, 3, 4]
tmp1 = a[1] # Variável temporária
tmp2 = a[2] # Variável temporária
a[2] = tmp1
a[1] = tmp2

a[2], a[1], a[3] = a[1], a[2], a[0] # Altera a orden dos indíces sem usar variáveis temporárias.

print(a)















