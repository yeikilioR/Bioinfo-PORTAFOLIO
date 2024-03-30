import paired

seq_1 = 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'
seq_2 = 'MVHFTAEEKAAITSIWDKVDLEKVGGETLGRLLIVYPWTQRFFDKFGNLSSALAIMGNPRIRAHGKKVLTSLGLGVKNMDNLKETFAHLSELHCDKLHVDPENFKLLGNMLVIVLSTHFAKEFTPEVQAAWQKLVIGVANALSHKYH'
alignment = paired.align(seq_1, seq_2, match_score=5, mismatch_score=-1, gap_score=-5)

print(alignment)
# [(0, 0), (1, None), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)]

for i_1, i_2 in alignment:
    print((seq_1[i_1] if i_1 is not None else '').ljust(15), end='')
    print(seq_2[i_2] if i_2 is not None else '')
