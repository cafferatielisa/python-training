#creiamo una variabile
x=15
y="Elisa" #noto che per dare un valore letterale alla variabile devo metterlo tra virgolette
#le variabili stringhe devo essere scritte tra "" oppure ''
#se una variabile è denominata a non andrà a sovrascrivere un'altra denominata A
#dando un valore ad una variabile, quando dovremo usarla per varie operazioni basta che scriveremo il nome della variabile, in questo caso x o y
print(x)
print(y)
#se vogliamo specificare il tipo di una variabile posso usare
a=int(3) #in questo caso specifichiamo che 3 è un numero intero
b=str(3) #in questo caso specifichiamo che 3 è una stinga e quindi quando la stamperemo ci mostrarà '3'
c=float(3) #in questo caso specifichiamo che 3 è un numero con la virgola e quindi quando la stamperemo ci mostrerà 3.0
#se vogliamo vedere in tipo della variabile faremo
print(type(x)) #qui dovrebbe venire fuori che è un numero intero e quindi int
print(type(y)) #qui dovrebbe venire fuori che è una stringa e quindi str
#le variabili possono essere denominate usando lettere,numeri e underscore, ma il nome della variabile non può mai iniziare con un numero, non può contenere il trattino - e non può contenere spazi
#si possono scrivere più variabili con diverso valore in una riga
x, y=15, "Elisa"
#possiamo anche creare una lista
frutta=["mela","banana","anguria"]
d, e, f=frutta
print(d, e, f) #per stampare più variabili in contemporanea posso scrivere il nome delle variabili separate da una virgola o dal +
