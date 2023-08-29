P = float(input("escreva a nota do primeiro bimestre: "))
S = float(input("escreva a nota do segundo bimestre: "))
T = float(input("escreva a nota do terceiro bimestre: "))
Q = float(input("escreva a nota do quarto bimestre: "))

Nt = P+S+T+Q
F = Nt/4

if F>=6:
    print("esse aluno tirou {: .2f}, portanto ele foi aprovado".format(F))

else:
    print("esse aluno tirou {: .2f}portanto ele foi reprovado".format(F))