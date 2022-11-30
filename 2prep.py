#esercizio A

#for x in range(5):
#   y = input("Dimmi un numero: ")
#   print(y)

#esercizio B
#num=[]
#for x in range(5):
#   y = input("Dimmi un numero: ")
#   num.append(int(y))
#num.reverse()
#print(num)

#esercizio C
#num = []
#for x in range(5):
#    y = input("Dimmi un numero")
#    num.append(int(y))
#numeripari=[]
#for n in num:
#    check= int(n/2)
#    if (check*2)==n:
#        numeripari.append(n)
#print(numeripari)

#esercizio D
#x=input("Quanti numeri vuoi inserire? ")
#for n in range(x):
#   y = input("Dimmi un numero: ")
#   num.append(int(y))

#esercizio E
#def primo(n):
#   for x in range(2,n):
#      check=int(n/x)
#      if check*x==n: print(False)
#   else: print(True)
#
#m=int(input("dimmi un numero: "))
#primo(m)

#esercizio F
#def asterischi(lista):
#   for elem in lista:
#      print("*"*elem)

#lista=[]
#n=int(input("quanti numeri vuoi inserire: "))
#for i in range(n):
#   m=int(input("Dimmi un numero: "))
#   lista.append(m)

#asterischi(lista)

#esercizio H
lista=[]

x=int(input("Quanti numeri vuoi inserire? "))
for n in range(x):
   y = input("Dimmi un numero: ")
   lista.append(int(y))

def parametri(n) :  
    for x in range (0,len(n)+1) :
        if x==3 or x==4 :
            print (n[x])
parametri(lista)

#esercizio I
i=0
n=4
a="*"
b=n-1
print(b,a)
while i<=n:
   a=(a+2*"*")
   b=(" "*b)
   i=i+1
   print(b,a)