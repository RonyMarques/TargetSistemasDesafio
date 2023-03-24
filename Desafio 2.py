def fibonacci(n):
    a, b = 0, 1
    while a < n:
        if a == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if fibonacci(numero):
    print(numero, "pertence à sequência de Fibonacci.")
else:
    print(numero, "não pertence à sequência de Fibonacci.")
