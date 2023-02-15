
def convertitore(a):
    return {a[i]:a.count(a[i]) for i in range(len(a))}
print(convertitore(["ciao","mondo","ciao","mondo","mondo"]))


def conta(lista):
    risultato={}
    for parola in lista:
        if parola in risultato:
            risultato[parola] +=1
        else:
            risultato[parola]=1
    return risultato
print(conta(["ciao","mondo","ciao","mondo","mondo"]))