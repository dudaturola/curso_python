"""
iterável -> str, range, etc(___iter___)
iterador -> quem sabe entregar um valor por vez
next-> me entregue o proximo valor
iter-> me entregue seu iterador
"""
texto = iter('Luiz') # __iter__()

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
