def maxliste(a=0):
    massimo=0
    for i in a:
        if i>massimo:
            massimo=i
    return massimo
lista=[1,2,13,44,7,8,3]
print(maxliste(lista))

"""def maxliste(a=0):
    massimo=max(a)
    return massimo
lista=[1,2,13,4,7,8,3]
print(maxliste(lista))"""
