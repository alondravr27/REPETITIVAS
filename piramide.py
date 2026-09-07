def piramide(n):
    for i in range(1, n + 1):
        espacios = " " * (n - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)


n = int(input("Ingrese la altura de la pirámide: "))

piramide(n)
