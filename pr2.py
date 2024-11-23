print("gutierrez Torres Paola") 
print(" ")
#creamos funcion
def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

#ejecutamos
numero1 = 10
numero2 = 20
numero3 = 15
resultado = max_de_tres(numero1, numero2, numero3)
print(f"El número mayor entre {numero1}, {numero2} y {numero3} es {resultado}")
