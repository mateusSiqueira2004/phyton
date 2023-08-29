a = float(input("escreva a sua altura: "))
p = float(input("escreva o seu peso: "))

imc = p/(a*a)

if imc<18.5:
    print("seu peso é de {} você está abaixo do peso".format(imc))
    
elif 18.5<imc<25:
    print("seu peso é de {} você está normal".format(imc))

elif 25<imc<30:
    print("seu peso é de {} você está com obesidade".format(imc))
    
elif 30<imc<35:
    print("seu peso é de {} você está com obesidade grau I".format(imc))
    
elif 35<imc<40:
    print("seu peso é de {} você está com obesidade grau II".format(imc))
    
else:
    print("seu peso é de {} você está com obesidade grau III".format(imc))
