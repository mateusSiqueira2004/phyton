import math

a= int(input("Digite o valor de a:"))
b= int(input("Digite o valor de b:"))
c= int(input("Digite o valor de c:"))
 
x=(b**2)-(4*a*c)
 
if x<0:
        print ("Raiz negativa nao pode ser extraida.")
 
else :
    x=math.sqrt(x)
    x1=(-b+x)/(2*a)
    x2=(-b-x)/(2*a)
print("na forma positiva {: .2f}, e na forma negativa {: .2f}".format(x1,x2))