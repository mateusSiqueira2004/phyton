D = int(input("escreva sua idade em dias: "))

M = D/30.417
A = M/12
R = (D%365)/365
K = (D/365)

print("voce possui {: .0f} dias, {: .0f} meses e {: .0f} anos".format(D,M,A))
print("sua idade atual é de {: .0f} anos, {: .0f} meses e {: .0f} dias".format(A,R,K))