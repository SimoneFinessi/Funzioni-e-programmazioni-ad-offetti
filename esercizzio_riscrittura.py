
def controllo(a=""):
    global x
    if (a=="Dante" and x==2) or (a=="Manzoni"and x==1):
        print("corretto")
        print("bravo")
    else:
        if x == 1:
            print("la risposta é Manzoni")
        else:
            print("la risposta é Dante")
        print("studia di più")

risposta1=input("chi ha scritto i promessi sposi?:")
x=1
controllo(risposta1)
risposta2=input("chi ha scritto la divina commedia?:")
x=2
controllo(risposta2)
#-----------------------------------------------------------------------------------------------------------
def controllo(a,b):
    if a==b:
        print("corretto")
        print("bravo")
    else:
        print("la risposta é ",b)
        print("studia di più")

risposta1=input("chi ha scritto i promessi sposi?:")
controllo(risposta1,"Manzoni")
risposta2=input("chi ha scritto la divina commedia?:")
controllo(risposta2,"Dante")