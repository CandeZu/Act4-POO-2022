class Ventana:
    __titulo = ""
    __xsupizq = 0
    __ysupizq = 0
    __xinfder = 0
    __yinfder = 0

    def __init__(self, titulo, xsupizq=0, ysupizq=0, xinfder=500, yinfder=500):
        self.__titulo = titulo
        self.__xsupizq = xsupizq
        self.__ysupizq = ysupizq
        self.__xinfder = xinfder
        self.__yinfder = yinfder
    
    def mostrar(self):
        print("{} \nCoordenadas vertice inferior: ({},{}) \nCoordenadas vertice superior: ({},{})\n".format(self.__titulo, self.__xinfder, self.__yinfder, self.__xsupizq, self.__ysupizq))

    def alto(self):
        return self.__yinfder - self.__ysupizq

    def ancho(self):
        return self.__xinfder - self.__xsupizq
    
    def getTitulo(self):
        return self.__titulo
    
    def moverDerecha(self, x=10):
        if (self.__xinfder <500) and (self.__xsupizq > 0):
            self.__xsupizq += x
            self.__xinfder += x
        
    def moverIzquierda(self, x = 10):
        if (self.__xinfder <500) and (self.__xsupizq > 0):
            self.__xsupizq -= x
            self.__xinfder -= x
        
    def bajar(self,y = 10):
        if (self.__yinfder <500) and (self.__ysupizq > 0):
            self.__ysupizq += y
            self.__yinfder += y
    
    def subir (self,y= 10):
        if (self.__yinfder <500) and (self.__ysupizq > 0):
            self.__ysupizq -= y
            self.__yinfder -= y
    




