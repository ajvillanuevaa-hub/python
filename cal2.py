# Pedir datos al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Validar división entre cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
