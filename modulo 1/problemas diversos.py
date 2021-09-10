#problema 1
inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año: " + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año: " + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año: " + str(round(balance3, 2)))

#problema 2
def main():
    print("ECUACIÓN AX² + BX + C = 0")
    a = float(input("Escriba el valor del coeficiente a: "))
    b = float(input("Escriba el valor del coeficiente b: "))
    c = float(input("Escriba el valor del coeficiente c: "))
    d = b * b - 4 * a * c
    if a == b == c == 0:
        print("Todos los números son solución.")
    elif a == b == 0:
        print("La ecuación no tiene solución.")
    elif a == 0:
        print(f"La ecuación tiene una solución: {- c / b}")
    elif d < 0:
        print("La ecuación no tiene solución real.")
    elif d == 0:
        print(f"La ecuación tiene una solución: {- b / (2 * a)}")
    else:
        print(
            f"La ecuación tiene dos soluciones: {(-b - d ** 0.5) / (2 * a)} y {(-b + d ** 0.5) / (2 * a)}"
        )
if __name__ == "__main__":
    main()