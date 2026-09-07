def suma(n):
    suma_pares = 0
    suma_impares = 0
    numero = 1

    while numero <= n:
        if numero % 2 == 0:
            suma_pares += numero
        else:
            suma_impares += numero

        numero += 1

    return suma_pares, suma_impares


n = int(input("Ingrese un número: "))

pares, impares = suma(n)

print("La suma de los números pares es:", pares)
print("La suma de los números impares es:", impares)