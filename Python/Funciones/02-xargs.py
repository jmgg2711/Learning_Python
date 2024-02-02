def suma(a, b):
    print(a + b)
    
def suma(a, b, c):
    print(a + b + c)

def suma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    print(f"Resultado: {resultado}")
    
suma(2,5)

suma(2,5,7)

suma(2, 5, 7, 48, 73, 95)


    
