saludo = "HOLA GLOBAL"

def saludar():
    global saludo
    saludo = "Hola Mundo"
    print(saludo)
    
    
def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)
    
# saludar()
# print(saludo)
# saludaChanchito()
# print(saludo)
# saludar()

print(saludo)
saludar()
