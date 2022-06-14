def bisiesto_o_no (x):
    if x%4 == 0 and (not (x%100==0) or x%400==0):
        print("Es un año bisiesto.")
    else:
        print("Es un año común.")
    return print()
x= int(input("Introduzca cualquier año: "))
print(x, bisiesto_o_no(x))