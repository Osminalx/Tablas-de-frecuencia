

def datosIniciales(numDatosTotal: int):
    datos = []
    for i in range(numDatosTotal):
        nuevoDato = float(input("ingresa un dato: "))
        datos.append(nuevoDato)
    return datos


def Max(datos: list):
    max = datos[0]
    for i in datos:
        if i > max:
            max = i
    return max


def Min(datos: list):
    min = datos[0]
    for i in datos:
        if i < min:
            min = i
    return min


def anchoDeClase(numClases, rango: float):
    anchoClase = rango//numClases
    return anchoClase, numClases


def limitesInferiores(min: float, anchoClase: int):
    limiteInf = []
    limiteInf[0] = min-1
    for i in range(1, 5):
        limiteInf[i] = limiteInf[i-1]+anchoClase
    return limiteInf


def limitesSuperiores(limiteInf: list, anchoClase: int):
    limiteSup = []
    for i in limiteSup:
        limiteSup[i] = limiteInf[i]+anchoClase
    return limiteSup


def Marcas(limiteInf: list, limiteSup: list):
    marca = []
    suma = 0
    for i in limiteInf:
        suma = limiteInf[i]+limiteSup[i]
        marca[i] = suma/2
        suma = 0
    return marca


def Frecuencias(datos: list, limiteInf: list, limiteSup: list):
    cuenta = 0
    frecuencia = []
    for i in limiteInf:
        for j in datos:
            if datos[j] >= limiteInf[i] and datos[j] < limiteSup[i]:
                cuenta += 1
        frecuencia[i] = cuenta
        cuenta = 0
    return frecuencia


def frecAcumulada(frecuencia: list):
    frecuenAcumulada = []
    frecuenAcumulada[0] = frecuencia[0]
    for i in range(1, len(frecuencia)-1):
        frecuenAcumulada[i] = frecuencia[i] + frecAcumulada[i-1]
    return frecuenAcumulada


def frecRelativa(numDatosTotal: int, frecuencia: list):
    frecuenciaR = []
    for i in frecuencia:
        frecuenciaR[i] = frecuencia/numDatosTotal
    return frecuenciaR


def frecRelativaAcumulada(numDatosTotal: int, frecuenAcumulada: list):
    frecuenciaRA = []
    for i in frecuenAcumulada:
        frecuenciaRA[i] = frecuenAcumulada/numDatosTotal
    return frecuenciaRA


def main():
    numDatosTotal = int(input("ingresa la cantidad de datos: "))
    primerTabla = datosIniciales(numDatosTotal)
    maximo = Max(primerTabla)
    minimo = Min(primerTabla)
    rango = maximo - minimo
    numClases = round(pow(numDatosTotal, 1/2))
    anchClase = anchoDeClase(numClases, rango)
    infLimit = limitesInferiores(minimo, anchClase)
    upLimit = limitesSuperiores(infLimit, anchClase)
    mark = Marcas(infLimit, upLimit)
    frequency = Frecuencias(primerTabla, infLimit, upLimit)
    accFrequency = frecAcumulada(frequency)
    relFrequency = frecRelativa(numDatosTotal, frequency)
    relAccFrequency = frecRelativaAcumulada(numDatosTotal, accFrequency)


print(main())
