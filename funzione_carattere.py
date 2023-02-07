def vocale(a):
    if a.lower() in ["a","e","i","o","u"]:
        voc="si"
    else:
        voc="no"
    return voc
print(vocale(input("inserisci una lettera minuscola: ")))

#scirvere un programma che dato un carattere dica se si tratta di una vocale o di una consonante
print("vocale") if vocale(input("inserisci una lettera minuscola: "))=="si" else print("consonante")