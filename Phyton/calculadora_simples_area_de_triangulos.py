x = float(input("escreva o primeiro valor: "))
y = float(input("escreva o segundo valor: "))
z = float(input("escreva o terceiro valor: "))

if x<y+z and y<x+z and z<x+y:
    if (x==y==z):
        print("com os valores se forma um triangulo equilatero")
    
    elif x==y and x==z and y==z:
        print("com os valores se forma um triangulo isósceles")

    elif x!=z!=y:
        print("com os valores se forma um triangulo escaleno")
    
else:
    print("esse triangulo é inválido")