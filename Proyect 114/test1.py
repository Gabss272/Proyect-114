a = int(input("Ingrese el primer número "))
b = int(input("Ingrese el segundo número "))

print(f"a = {a} b = {b}")

if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")