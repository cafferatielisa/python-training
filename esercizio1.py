#ALBERO DI NATALE
# Importo alcune librerie per far lampeggiare l'albero
import os
import time
clear = lambda: os.system('clear') #Su linux
#clear = lambda: os.system('cls') #Su windows

#Definisco la funzione christmas tree
def christmas_tree(h, c):
    n_ast = 1
    n_spc = h-1

    for i in range(0, h):
        print(n_spc * ' ' , n_ast * c)
        n_ast = n_ast +2
        n_spc = n_spc -1

#Richiedo l'input all'utente
height = int(input("Dimmi l'altezza: "))
char = input("Dimmi un carattere: ")
char2 = input("Dimmi un carattere: ")

turno = True #Uso questa variabile per alternare la stampa dei due caratteri
#Faccio lampeggiare l'albero 20 volte (10 secondi)

for i in range(0, 20):
    clear()  # Cancella la console
    if turno == True: christmas_tree(height, char)
    else: christmas_tree(height, char2)
    turno = not turno #l'operatore logico not inverte il valore di una variabile boolean s: not true => false  | not false = true
    time.sleep(0.5) #Blocca l'esecuzione di un programma per 0.5 secondi




#esercizio J
listanumeri=[]

def funzione(a):
   x=int(input("Quanti numeri vuoi inserire? "))
      for n in range(x):
         y = int(input("Dimmi un numero: "))
         listanumeri.append(int(y))
print(listanumeri)

#MCD

def mcd(a, b):
    while(b != 0):
        R=a/b
        a=b
        b=R
    return a
 
print(mcd(70,15))


#scomposizione in numeri primi
fattori=[]
risultato = []
numero = input("numero: ")

while numero != 1:
    for i in range(2, numero+1):
       if numero / i == 0:
            numero = numero / i
            if i in fattori:  
                fattori=fattori + 1
            else:
                fattori = 1
            break

#NUMERO PRIMO O NO
numero=int(input("dimmi un numero: "))
i=0
dividendo=2
if numero/dividendo==0:
    i=i+1
    dividendo=dividendo+1
    if i==0:
        print("Numero primo")
else:
   print("Il numero non è primo")

