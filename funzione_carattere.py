def vocale(a):
    if a in ["a","e","i","o","u"]:
        voc="si"
    else:
        voc="no"
    return voc
print(vocale(input("inserisci una lettera minuscola: ")))