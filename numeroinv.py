def invertir_numero(num):
    invertido = 0

    if num < 0:
        num = -num

    while num > 0:
        digito = num % 10
        invertido = invertido * 10 + digito
        num = num // 10

    return invertido

numero = int(input("Ingrese un numero entero: "))

resultado = invertir_numero(numero)

print(f"El numero invertido es: {resultado}")