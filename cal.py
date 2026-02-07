# numero1 = None
# numero2 = None

# def pedir_numero():
#    pass

#def mostrar_menu():
 #   pass

#def suma():
 #   pass

#def resta():
 #   pass

#def multiplicacion():
 #   pass

#def division():
#   pass

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

print("Seleccione una operación")
print("Sus operaciones son las siguientes: ")
print("Suma: +")
print("Resta: -")
print("Multiplicación: *")
print("Division: /")
operacion = print("Ingrese el simbolo de la operación a realizar")

if operacion == "+":
    print(f"Resultado: {num1 + num2}")
elif operacion == "-":
    print(f"Resultado: {num1 - num2}")
elif operacion == "*":
    print(f"Resultado: {num1 * num2}")
elif operacion == "/":
    if num2 == 0:
        print("Error: División por cero no permitida")
    else:   
        print(f"Resultado: {num1 / num2}")
else:
    print("La operación no es válida")