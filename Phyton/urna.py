senha = "1234"

M  = 0 
P  = 0 
R  = 0
B  = 0 
N  = 0 
Mv = 0
Pv = 0
Rv = 0
Nv = 0
Bv = 0

while True:
    infsenha = input("informe a senha: ")
    if senha == infsenha:
        print("\n|===============|\n")
        print("Sistema online")
        print("\n|============|\n")
        break

while True:
    eleicao = input("deseja iniciar o processor eleitoral: (s) ou (n)\n")
    print("\n \n")
    if eleicao=="s":
        opcao = input("faca o seu voto conforme o numero ao lado do nome do mesmo  \n Anular voto (Nulo) \n Paozinho  (10) \n Ronaldinho  (15)  \n Marquinhos  (20) \n Voto em branco (branco) \n Escolha uma das opcoes a cima:  ")


        print("\n|--------------------------------|\n")

        if opcao=="Nulo":
            N = Nv + 1
 
        elif opcao=="20":
            M = Mv + 1
    
        elif opcao=="10":
            P = Pv + 1
    
        elif opcao=="15":
            R = Rv + 1
        
        elif opcao=="branco":
            B = Bv + 1
    
        elif opcao=="Admin":
            segundo = input("Digite a senha de acesso do ADM")
            if segundo==senha:
                opcao1=input("voce deseja encerrar a eleicao e imprimir (s)\n voce deseja iniciar uma nova eleicao(r)")
                
                if opcao1=="s":
                    print("|Votos Nulos-0  ({})|".format(N))
                    print("|Marquinhos-20  ({})|".format(M))
                    print("|Paozinho-10    ({})|".format(P))
                    print("|Ronaldinho-15  ({})|".format(R))
                    print("|Votos em branco({})|".format(B))
                
                    print("\n|---------------------|\n")
                    print("a porcentagem é \n")
                
                    T1 = N + M + P + B + R 
                    P1 = (N/T1)*100
                    P2 = (M/T1)*100
                    P3 = (P/T1)*100
                    P4 = (R/T1)*100
                    P5 = (B/T1)*100
                
                    print("\n \ntodas as opcoes\n")
                    print("|Votos Nulos-0  ({: .2f}%)|".format(P1))
                    print("|Marquinhos-20  ({: .2f}%)|".format(P2))
                    print("|Paozinho-10    ({: .2f}%)|".format(P3))
                    print("|Ronaldinho-15  ({: .2f}%)|".format(P4))
                    print("|Votos em branco({: .2f}%)|".format(P5))
                
                    print("\n \n|---------------------|\n")
                    print("apenas dos canditados\n")
                
                    T = R + M + P
                    P6 = (M/T)*100
                    P7 = (P/T)*100
                    P8 = (R/T)*100
                
                    print("|Marquinhos-20  ({: .2f}%)|".format(P6))
                    print("|Paozinho-10    ({: .2f}%)|".format(P7))
                    print("|Ronaldinho-15  ({: .2f}%)|".format(P8))
                    exit()

                elif opcao1=="r":
                    Mv = 0
                    Pv = 0
                    Rv = 0
                    Nv = 0
                    Bv = 0
                    M  = 0 
                    P  = 0 
                    R  = 0
                    B  = 0 
                    N  = 0
        else:
            print("\n-------------------\n")
            print("erro confirmado, repitindo o processor")
            print("\n-------------------------\n")
            
    else:
        confirm = input("digite a senha para encerrar: \n se foi engano digite (e): ")
        if confirm=="e":
            print("\n===================\n               ")
            print("voltando a eleicao")
            print("\n================\n")
        
        elif confirm==senha:
            print("cancelando a eleicao")
            exit()
            
        
    
        Nv = N
        Mv = M
        Pv = P
        Rv = R
        Bv = B