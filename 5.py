#Scrieti o functie care citeste un string de la tastatura si afiseaza lungimea lui. Tratati cazul in care textul nu este string

def citesteString():
    try:
        n=input("Scrieti stringul: ")
        if isinstance(n, str):
            return len(n)
        else:
            print("nu este sir de caractere")
    except(ValueError) as err:
        print(err)


print(citesteString())