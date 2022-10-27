frutta = ["mela", "banana", "ciliegia", "pera","kiwi", "anguria"] #crea una lista. nella lista posso mettere tutti i tipi di variabile
print(frutta) #stampa tutto, compreso parentesi quadre e virgolette
print(len(frutta)) #mi dice quanti componenti ho nella lista
print(type(frutta)) #mi dice la classe della variabile, in questo caso è una lista
#ci sono 4 tipi di linguaggio: 
#1.List, i contenuti sono ordinati e scambiabili. accetta contenuti duplicati
#2.Truple, i contenuti sono ordinati e non scambiabili. accetta contenuti duplicati
#3.Set, i contenuti non sono ordinati e non sono scambiabili. non accetta contenuti duplicati
#4.Dictionary, i contenuti sono ordinati e scambiabili. non accetta contenuti duplicati

#se si vuole stampare un solo contenuto della lista bisogna scrivere
print(frutta[0]) #in questo caso stamperà il primo contenuto della lista
print(frutta[-1]) #stampa l'ultimo contenuto della lista
print(frutta[-2]) #stampa il penultimo contenuto della lista
#possiamo anche stampare dicendo al computer il range, ovvero se voglio stampare da banana fino a kiwi gli devo dire la posizione in cui è banana e la posizione sucessiva a quella in cui c'è kiwi
print(frutta[1:5]) #banana è nella posizione 1 e kiwi nella 4, quindi gli dico di stampare da 1 fino a 5 escluso
#se gli dico solo [:4] mi stamperà dal primo elemento fino al 4 escluso, quindi stampa i primi 3

#if
if "mela" in frutta:
    print("si, mela è un frutto")

#se voglio cambiare l'elemento mela e mettere melone scriverò
frutta[0]="melone"
#posso anche cambiare più elementi in contemporanea
frutta[1:4]=("ananas", "pesca") #in questo caso sostituisco gli elementi dal primo fino al terzo con i 2 elementi che ho scritto
print(frutta)
#se voglio inserire un nuovo elemento scrivo
frutta.insert(2,"uva") #in posizione 2 ha messo uva
print(frutta)
#per aggiungere un elemento alla fine della lista scrivo
frutta.append("fragola")
frutta.insert(1, "ciliegia") #aggiunge ciliegia nella posizione 1
verdura=["zucchina", "carota","finocchi"]
frutta.extend(verdura) #unisce le due liste
print(frutta)
frutta.remove("uva") #rimuove banana dalla lista
frutta.pop(3) #cancella l'elemento in quella posizione. se non metto il numero si elimina l'ultimo elemento della lista
del frutta[1] #cancella l'elemento in quella posizione
del frutta #cancella la lista
frutta = ["mela", "banana", "ciliegia", "pera","kiwi", "anguria"]
frutta.clear() #cancella tutti gli elementi, ma non la lista
#per stampare tutti gli elementi della lista, uno per uno
for x in frutta:
    print(x)
#
for i in range(len(frutta)):
    print(frutta[i])
#Print all items, using a while loop to go through all the index numbers
i = 0
while i < len(frutta):
  print(frutta[i])
  i = i + 1
#A short hand for loop that will print all items in a list
[print(x) for x in frutta]
#per ogni lettera u presente nella lista frutta, aggiunge la parola che contiene quella lettera nella nuova lista
#la posso scrivere sia così
newlist = []
for x in frutta:
  if "u" in x:
    newlist.append(x)
print(newlist)
#sia così
newlist = [x for x in frutta if "a" in x]
#newlist = [expression for item in iterable if condition == True]
newlist = [x for x in frutta if x != "mela"] #accetta tutti gli elementi che non siano mela
#if x != "apple" , accetta tutti gli elementi che non siano mela
#crea una lista con 10 numeri, da 0 a 9
newlist = [x for x in range(10)]
#accetta numeri minori di 5
newlist = [x for x in range(10) if x < 5]
#tutti gli elementi di quella lista li scrive in stampatello maiuscolo
newlist = [x.upper() for x in frutta]
#sostituisce tutti gli elementi della lista con hello
newlist = ['hello' for x in frutta]
#sostituisce tutti gli elementi banana con arancia
newlist = [x if x != "banana" else "arancia" for x in frutta]
#ordina la lista in ordine alfabetico o numerico(dal più piccolo al più grande)
frutta.sort() #tutte le lettere maiuscole vengono ordinate prima delle lettere minuscole
##ordina la lista in ordine alfabetico al contrario o numerico(dal più grande al più piccolo)
frutta.sort(reverse = True)
#ordina i numeri a seconda di quanto sono vicini al numero 50
def myfunc(n):
  return abs(n - 50)

numeri = [100, 50, 65, 82, 23]
numeri.sort(key = myfunc)
#ordinamento dell'elenco senza distinzione tra maiuscole e minuscole
frutta.sort(key = str.lower)
#Invertire l'ordine delle voci dell'elenco
frutta.reverse()
#Fare una copia di una lista con il copy()metodo
listafrutta = frutta.copy()
#Fare una copia di una lista con il list()metodo
listafrutta = list(frutta)
#unire 2 liste
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
#Aggiungi list2 in list1
for x in list2:
  list1.append(x)
#Usa il extend()metodo per aggiungere list2 alla fine di list1
list1.extend(list2)