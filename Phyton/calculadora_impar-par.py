N = float(input("escreva o numero desejado: "))

P=N%2

if N==0:
    print("esse numero é nulo")

elif P!=0 and N<0:
    print("esse numero {} é impar e negativo".format(N))

elif P!=0 and N>0:
    print("esse numero {} é impar e positivo".format(N))
    
elif P==0 and N>0:
    print("esse numero {} é par e positivo".format(N))

elif P==0 and N<0:
    print("esse numero {} é par e negativo".format(N))

else:
    print("esse numero está em outra categoria")