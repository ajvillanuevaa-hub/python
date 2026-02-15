entrada = input("Ingresa un número para duplicar: ")

if entrada.isdigit():
    numero = int(entrada)
    resultado = numero * 2
    print(f"El doble es: {resultado}")
else:
    print("Error: Debes ingresar un número válido.")