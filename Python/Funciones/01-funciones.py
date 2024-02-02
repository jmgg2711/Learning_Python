def hola1():                         # Definición de funcion, nombre de la función seguida de paréntesis
    print("Hola Mundo!")            # Cuerpo de la función en la que se incluyen las instrucciones que se ejecutarán
    print("Bienvenido")             # al mandar llamar a la función

hola1()                              # Llamado de la función definida anteriormente

def hola2(nombre):
    print("Hola mundo!")
    print(f"Bienvenido {nombre}")

hola2("Duke")    
hola2("Niza")
hola2("Magnum")
hola2("Kaizer")
hola2("Tuno")
hola2("Moka")
hola2("Pixie")
hola2("Negro")

def hola3(nombre, apellido):        # Múltiples parámetros en una función
    print(f"Hola {nombre} {apellido}")
    
hola3("Juan", "Gutiérrez")          # Múltiples argumentos para la función

def hola4(nombre, apellido = "Feliz"):        # Múltiples parámetros en una función
    print(f"Hola {nombre} {apellido}")
    
hola4("Juan", "Gutiérrez")          # Múltiples argumentos para la función
hola4("Manuel")

hola4(apellido = "Gallegos", nombre = "Manuel")     # Argumentos nombrados, diferente orden al asignado 
                                                    # en la declaración de la función