#scrivere un funzione che facci la somma tra due numeri interi
'''def somma2(a,b):
    return int(a+b)
print(somma2(1,2))'''

#utilizzare la funzione precedente per scirivere una funzione che faci la somma di tre numeri interi
'print(somma2(somma2(1,2),3))'
#scrivere una funzione prodotto  chiamata prodotto che facci il prodotto di due numeri inseriti dall'utente usando la funzione somma usata precedentemente
'''def prodotto(a,b):
    x=a 
    c=b
    if b <0:
       c= b*-1
    for i in range(c-1):
       x=somma2(x,a)
    if b<0:
        x=x*-1
    return x
print(prodotto(int(input("")),int(input(""))))'''
#scrivere la funzione MCD che calcola il massimo comun divisore tra due numeri 
def MCD(a,b):
    for i in range(1,int(b/2)):
        if a%i == 0 and b%i == 0:
            n=i
    return n
#print(MCD(47,22))
        
#mcm minimo comune multiplo
def mcm(a,b):
    m1=a
    m2=b
    while a !=b:
        if a<b:
            a=a+m1
        else:
            b=b+m2
    return a
#print(mcm(25,15))

#scrivere una funizone chhiamata semplifica che semplifica una frazione
def semplifica(a,b):
    m=MCD(a,b)
    a=a/m
    b=b/m
    return a,b
#print(semplifica(10,20))
#scrivere una funzione che permetta di fare la somma tra due frazioni dando il risultato semplificato
def sommaF(a,aa,b,bb):
    den=mcm(aa,bb)
    a=a*(den/aa)
    b=b*(den/bb)
    a=a+bb
    return semplifica(a,den)
#print(sommaF(5,20,25,50))
#scrivere una funzione che permetta di fare il prodotto tra due frazioni dando il risultato semplificato
def moltF(a,aa,b,bb):
    a=a*b
    aa=aa*bb
    return semplifica(a,aa)
print(moltF(5,20,25,50))
#scrivere una funzione che permetta di fare la divisione tra due frazioni dando il risultato semplificato
