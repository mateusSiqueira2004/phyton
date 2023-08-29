VM = float(input("informe a velocidade media: "))
tmp = float(input("informe a duração da viagem: "))
rnd = float(input("informe o rendimento do litro: "))
pltr = float(input("informe o preco do litro: "))
pedag = float(input("informe o preco do pedagio: "))
Depre = float(input("informe o preco da depreciassao: "))

Custo = ((VM/tmp)/rnd*pltr)+((VM/tmp)*Depre)+pedag

print("os custos foram de {: .2f}".format(Custo))