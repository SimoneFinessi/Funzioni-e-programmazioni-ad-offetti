#scrivi una funzione che prende due mnumeri come parametro e manda in print il più grande dei due
def maggiore(a=0,b=0):
    if a>b:
        max=a
    else:
        max=b
    return max

#es 2
def maggiore3(a=0,b=0,c=0):
    if a>b and a>c:
        max=a
    elif b>a and b>c:
        max=b
    else:
        max=c
print(maggiore3(1,2,3))#codice poco funzionale perche troppo lungo

#es 2 BIS
#utilizzare la funzione precedentemente creata per scriverne una altra che trova il massimo tra 3 valori

def maggiore2(a=0,b=0,c=0):
    return maggiore(maggiore(a,b),c)
print(maggiore2(int(input("inserisci il primo numero")),int(input("inserisci il secondo numero")),int(input("inserisci il terzo numero"))))