

def Principal():
    numDatosTotal = int(input("ingresa la cantidad de datos: "))
    numClases = round(pow(numDatosTotal, 1/2))
    rango = 0
    datos = []
    for i in range(numDatosTotal):
        nuevoDato = float(input("ingresa un dato: "))
        datos.append(nuevoDato)
    print(datos)


Principal()
