def get_product(**datos):       # key word arguments (kwargs) requiere doble asterisco
    print(datos)                # imprime todos los kwargs que se definen como argumentos 
    print(datos["id"], datos["name"], datos["desc"])    # imprime solo los argumentos especificados entre []
    print(datos["id"], datos["desc"])
    
#get_product(id = "id")          # imprime un diccionario: {'id': 'id'}, estos son bajo demanda

get_product(id = "23",
            name = "Iphone", 
            desc = "Esto es un Iphone")