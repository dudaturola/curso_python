# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

#Criando um set
#set(iterável) ou {1, 2, 3}

# s1 = {'Duda',1,2,3}
# print(s1, type(s1))

# s1 = set() # set vazio
# s1 = {'Duda',1,2,3} # set com dados


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in , not in)

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = s1 = {1,2,3}
# print(s1)
# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discart

# s1 = set()
# s1.add('Luiz')
# s1.add(5)
# s1.update(('Olá mundo',1,2,3,4))
# s1.discard('Olá mundo')
# print(s1)
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(s3)
s4 = s1 & s2
print(s4)
s5 = s1 - s2
print(s5)
s6 = s1 ^ s2
print(s6)