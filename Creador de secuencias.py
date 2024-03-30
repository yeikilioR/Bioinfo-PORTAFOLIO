def escribir_archivo_fasta(identificadores, secuencias, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for i in range(len(identificadores)):
            identificador = f">{identificadores[i]}_{len(secuencias[i])}"
            secuencia = secuencias[i]
            archivo.write(identificador + '\n') 
            archivo.write(secuencia + '\n')  

cant_secuencias = int(input("Ingrese el número de secuencias: "))
identificadores = []
secuencias = []
nombre = input("¿Como desea que se llame su archivo?: ")
for i in range(cant_secuencias):
    identificador = input(f"Ingrese el identificador para la secuencia {i + 1}: ")
    secuencia = input(f"Ingrese la secuencia {i + 1}: ")
    identificadores.append(identificador)
    secuencias.append(secuencia)

nombre_secuencia = nombre+(".fasta")
escribir_archivo_fasta(identificadores, secuencias, nombre_secuencia)

print(f"El archivo {nombre_secuencia} ha sido creado satisfactoriamente.")
