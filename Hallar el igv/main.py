print("Ingresar su mombre:")
nombre = input()
print("Ingresar la fecha de ventas:")
fecha = input()
print("Ingresar la cantidad de ventas:")
cantidadventas = int(input())
i = 1
sumamontoventas = 0
while i <= cantidadventas:
    print("Ingresar monto de venta: ", i, " : ")
    montoventas = float(input())
    sumamontoventas = sumamontoventas + montoventas
    i += 1
print("El igv del monto será: ", sumamontoventas * 0.18)
igv = sumamontoventas * 0.18
print("El monto total es: ", igv + sumamontoventas)