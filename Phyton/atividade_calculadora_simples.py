N1 = int(input("escreva o primeiro valor: "))
N2 = int(input("escreva o segundo valor: "))
opcao = input("para soma escreva(0), para subtração escreva(1), para multiplicação escreva(2) e para divisão escreva(3)")

if opcao<"0" or opcao>"3":
    print("opcao invalida!")
    
elif opcao=="0":
    res=N1+N2

elif opcao=="1":
    res=N1-N2

elif opcao=="2":
    res=N1*N2

else:
    res=N1/N2

print("o resuldado dos valores {} e {} conforme a opcao selecionada sera de {}".format(N1,N2,res))