#i print()sono funzioni infatti ne abbiamo gia usate alcune
"""print("ciao")"""#funzione integrata
#FUNZIONE= blocco di istruzioni utilizzate per eseguire un'attivita specifica
#perche non usare copia-incolla
#perceh usando la funzine rendi il codice piu compatto e leggibile, rendendolo anche facilmente modificabile in caso di errori+
#si creano con def <nome()>: 
#dentro alle parentesi ci inseriamo i parametri

def nome():#dichiaro la funzione e il nome
    name=input("inserisci nome")
    print(name)
"""nome()"""#richiamo la funzione

def addizione(a,b):#PARAMETRO modo che l'utente a per passare valori tra le funzioni
    risultato=a+b
    print(str(risultato))
"""addizione(15,5)"""
#inserisco oltre al richiamare la funzione anche i valori il primo sara poi chiamato A e il second B

#si puo rendere il passaggio di tutti i valori opzionali dando un valore di dafoult ai valori nella funzione 
def addnoval(a,b=0):
    print(a,b)
"""addnoval(1)
addnoval(1,2)"""

def addizione2(a,b):
    risultato=a+b
somma=addizione2(1,2)
"""print(somma)
print(type(somma))"""

#funzionamente delle variabili all'interno delle funzioni

x=15
def esempio():#in python le variabili vengono salvate o in locale o in globale
    global x
    x +=2
    return x
print(esempio())

#per poter utilizzare ilvalore di una variabile globale dall'interno di una funzione come abbiamo provato a fare con  la nostra 
