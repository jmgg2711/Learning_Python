print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

num1 = ""
while True:
    if not num1:
        num1 = input("Ingresa número: ")
        if num1.lower() == "salir":
            break
        num1 = int(num1)
    oper = input("Ingresa operación: ")
    if oper.lower() == "salir":
        break
    else:
        num2 = input("Ingresa siguiente número: ")
        if num2.lower() == "salir":
            break
        else:
            num2 = int(num2)
            if oper == "suma":
                num1 += num2
            elif oper == "resta":
                num1 -= num2
            elif oper == "multi": 
                num1 *= num2
            elif oper == "div":
                num1 /= num2
            else:
                print("Operación inválida")
                break
            print(f"Resultado: {num1}")        

