print("gutierrez Torres Paola") 
print(" ")
#creamos funcion
def calcular_longitud(objeto):
    contador = 0
    for elemento in objeto:
        contador += 1
    return contador

#creamos cadena
cadena = "Hola, mundo"
longitud_cadena = calcular_longitud(cadena)
print(f"La longitud de la cadena '{cadena}' es {longitud_cadena}")

#creamos lista
lista = [1, 2, 3, 4, 5]
longitud_lista = calcular_longitud(lista)
print(f"La longitud de la lista {lista} es {longitud_lista}")
