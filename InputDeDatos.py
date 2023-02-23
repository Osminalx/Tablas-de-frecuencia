

def datosIniciales():
    numDatosTotal = int(input("ingresa la cantidad de datos: "))
    datos = []
    for i in range(numDatosTotal):
        nuevoDato = float(input("ingresa un dato: "))
        datos.append(nuevoDato)
    return datos, numDatosTotal


def rango(datos: list):
    min = datos[0]
    max = datos[0]
    for i in datos:
        if i > max:
            max = i
        elif i < min:
            min = i
    rango = max - min
    return rango, min, max


def anchoDeClase(numDatosTotal: int, rango: float):
    numClases = round(pow(numDatosTotal, 1/2))
    anchoClase = rango//numClases
    return anchoClase, numClases
