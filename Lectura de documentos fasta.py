x = open(r"C:\Users\User 1\Desktop\Bioinformatica\FASTAS\dUTPase.fasta","r")
a = x.read()
x.close()

b = a[103:]
print("Secuencia orginal dUTPasa de E.coli :\n",b)
## LA SECUENCIA ARREGLADA (sin la primera linea) ESTÁ EN LA VARIABLE b ##
inicio = "atgaaaaa"
inicio_mayus = inicio.upper()

final = "gtcagtaa"
final_mayus = final.upper()

Inicio_b = b.find(inicio_mayus)
Final_b = b.find(final_mayus)

final = Final_b+8
print("La primera parte de la secuencia codificante es: \n",b[Inicio_b:final])
