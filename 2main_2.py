#In Python una funzione è definita usando la parola chiave def :
def funzione():
  print("ciao da una funzione")
#se io scrivo:
print(funzione) #mi stamperà ciò che gli ho detto di stampare nella funzione

#Le informazioni possono essere passate in funzioni come argomenti.
#Gli argomenti sono specificati dopo il nome della funzione, tra parentesi.
#stampa tutti i nomi che metto tra le parentesi sucessive più Rossi
def funzione2(nome):
  print(nome + " Rossi")
funzione2("Emilia")
funzione2("Tommaso")
funzione2("Luigi")

#Dal punto di vista di una funzione:
#Un parametro è la variabile elencata tra parentesi nella definizione della funzione.
#Un argomento è il valore che viene inviato alla funzione quando viene chiamata.
#una funzione deve essere chiamata con il numero corretto di argomenti. 
#Ciò significa che se la tua funzione prevede 2 argomenti, devi chiamare la funzione con 2 argomenti, non di più e non di meno.
def funzione3(nome, cognome):
  print(nome + " " + cognome)
funzione3("Elisa", "Cafferati") #se avessi messo solo un argomento mi avrebbe dato errore

#Se il numero di argomenti è sconosciuto, aggiungere a * prima del nome del parametro:
def funzione4(*bambino):
  print("Il bambino più piccolo è " + bambino[2])
funzione4("Emilia", "Tommaso", "Luigi")

#Puoi anche inviare argomenti con la sintassi chiave = valore 
def funzione5(bambino3, bambino2, bambino1):
  print("Il bambino più piccolo è  " + bambino3)
funzione5(bambino1 = "Emilia", bambino2 = "Tommaso", bambino3 = "Luigi")

#Se il numero di argomenti della parola chiave è sconosciuto, aggiungi un double **prima del nome del parametro:
def funzione6(**bambino):
  print("il suo nome è " + bambino["nome2"])
funzione6(nome1= "Tobias", nome2 = "Refsnes")

#utilizzare un valore di parametro predefinito
def funzione7(paese = "Norvegia"):
  print("Arrivo da " + paese)
funzione7("Svezia")
funzione7("India")
funzione7()
funzione7("Brasile")

#se nell'argomento metto il nome di una lista, la funzione viene eseguita per quella lista
def funzione8(cibo):
  for x in cibo:
    print(x)
frutta = ["mela", "banana", "ciliegia"]
funzione8(frutta)

#per farci restituire il risultato della funzione uso return
def funzione9(x):
  return 5 * x

print(funzione9(3))
print(funzione9(5))
print(funzione9(9))#in questo caso mi dirà la soluzione di questa moltiplicazione

#se per qualche motivo la funzione la devo lasciare vuota uso pass
def funzionevuota():
  pass

#spiegazione sul foglio
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
tri_recursion(6)
