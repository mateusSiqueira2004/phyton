HT = float(input("escreva as horas trabalhadas: "))
VPT = float(input("escreva o valor por horas trabalhadas: "))
PTD = float(input("escreva o valor do desconto: "))

Sb = HT * VPT

Desc = Sb * PTD/100

Sl = Sb - Desc

print("o seu salario bruto e {} e o salario liquido {}".format(Sb,Sl))