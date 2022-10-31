#Uguale a: a == b
#Diverso da: a != b
#Minore di: a < b
#Minore o uguale a: a <= b
#Maggiore di: a > b
#Maggiore o uguale a: a >= b
a=20
b=10
c=40

if a < b:
    print("a è minore di b")
elif a == b :
    print("b è uguale ad a")
else:
    print("b è minore di a")
#metodo più veloce con 2 condizioni
print("A") if a>b else print("B")
#con 3 condizioni
if c>b and c>a:
    print("c è il più grande")
#or una delle due condizioni deve essere vera
if a>b or a>c:
    print("a non è il numero più piccolo")
#se non ho nessuna cosa da far fare al computer per una condizione metto pass così da non far venire fuori l'errore
if c<b:
    pass
