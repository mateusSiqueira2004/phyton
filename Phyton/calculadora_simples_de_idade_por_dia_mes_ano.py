
opcao = input("escolha a forma que voce deseja verificar a sua idade, dias(D), meses(M) e ano(A)")

if opcao=="D":
    D = int(input("informe quantos dias de vida voce possui: "))
    M = D/30.417
    A = D*365
    
elif opcao=="M":
    M = int(input("informe quantos meses voce possui: "))
    D = M/30.417
    A = M*12
    
elif opcao=="A":
    A = int(input("informe quantos anos voce possui: "))
    M = A*12
    D = A/365
    
else:
    print("opcao invalida")

R = (D%365)/30
K = (D/360)

print("voce possui {: .0f} dias, {: .0f} meses e {: .0f} anos".format(D,M,A))
print("sua idade atual é de {: .0f} anos, {: .0f} meses e {: .0f} dias".format(A,R,K))