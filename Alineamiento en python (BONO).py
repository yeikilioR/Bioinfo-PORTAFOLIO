import paired

Homo_sapiens = ("MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH")
Mus_musculus_domesticus = ("MVHFTAEEKAAITSIWDKVDLEKVGGETLGRLLIVYPWTQRFFDKFGNLSSALAIMGNPRIRAHGKKVLTSLGLGVKNMDNLKETFAHLSELHCDKLHVDPENFKLLGNMLVIVLSTHFAKEFTPEVQAAWQKLVIGVANALSHKYH")
alignment = paired.align(Homo_sapiens, Mus_musculus_domesticus)
# El comando "alignment" es el cual realiza el alineamiento global de las secuencias.
for i_1, i_2 in alignment:
    print((Homo_sapiens[i_1] if i_1 is not None else '').ljust(15), end='')
    print(Mus_musculus_domesticus[i_2] if i_2 is not None else '')
# Este organiza los alineamientos de forma vertical para visualizar más facilmente los pares.
