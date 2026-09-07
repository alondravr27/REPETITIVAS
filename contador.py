def contador_digitos(numero):
    if numero < 0:
        numero = -numero

    contador = 0

    if numero == 0:
        contador = 1
    else:
        while numero > 0:
            numero = numero // 10
            contador += 1

    return contador


numero = int(input("Ingrese un número entero: "))

resultado = contador_digitos(numero)

print(f"El número tiene {resultado} dígitos.")