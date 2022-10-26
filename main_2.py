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
