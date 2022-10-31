#Stampa ogni frutto in una lista di frutti
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#stampa tutte le lettere della parola indicata
for x in "banana":
  print(x)
#Esci dal ciclo quando x è "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#Non stampare banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#stampa i numeri fino a 6 escluso
for x in range(6):
  print(x)
#stampa i nueri da 2 a 29 ogni 3
for x in range(2, 30, 3):
  print(x)
#Stampa tutti i numeri da 0 a 5 e stampa un messaggio quando il ciclo è terminato
for x in range(6):
  print(x)
else:
  print("terminato")
#Il "ciclo interno" verrà eseguito una volta per ogni iterazione del "ciclo esterno"
#Stampa ogni aggettivo per ogni frutto
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
