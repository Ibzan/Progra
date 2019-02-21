#entradas: tres números
#salidas: producto y resultado
#restricciones: solo números enteros


def operaciones(a,b,c):
    resul_1 =a+b+c/3
    resul_2 =a*b*c
    if(a+b>c):
        print("El promedio es: ",resul_1,"y el producto es: ",resul_2)

    else:
        print("La operacíon no es posible")
