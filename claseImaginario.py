class imaginario:
    def __init__(self):
        pass
    def calcular(self, pro):
        partes = pro.split("=")
        partes2 = partes[1].replace("i", "")
        partes2 = eval(partes2)
        resultado = str(partes[0]) + "=" + str(partes2) + "i"
        return resultado