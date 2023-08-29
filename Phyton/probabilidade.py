
print("imaginando uma competição onde há dois times com participantes em quantidades diferentes, qual a probabilidade de pelo menos um competidor de um dos times ganhar nas 3 primeiras colocações numa sequência de ganhador aleatória ou numa sequência do de maior quantidade\n")
t = float(input("escreva quantos participantes terão no total: "))
h1 = float(input("escreva quantos de um tipo de participantes terão: "))
h2 = float(input("escreva quantos de um outro tipo de participantes terão: "))

resul = h1 + h2

if resul != t:
    print("digite valores correspondentes com o total")
    exit()
else:    
    opcao = input("aleatório(a) ou não(n), ou ambos(A)")
  
    if opcao=="A":
        ra = ((h1/t)*((h1-1)/(t-1))*(h2/(t-2))*3)*100
        r = ((h1/t)*((h1-1)/(t-1))*(h2/(t-2)))*100
        print("são{: .2f}% de chance de ganhar nessa sequencia ou em qualquer sequencia é {: .2f}%".format(r,ra))

    elif opcao=="n":
        r = ((h1/t)*((h1-1)/(t-1))*(h2/(t-2)))*100
        print("são {: .2f}% de chance de ganhar nessa sequencia".format(r))
            
    elif opcao == "a":
        ra = ((h1/t)*((h1-1)/(t-1))*(h2/(t-2))*3)*100
        print("em qualquer sequencia é {: .2f}%".format(ra))

    else:
        print("digite valores validos")