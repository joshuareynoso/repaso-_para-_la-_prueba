class RECTANGULO:
    def __init__(self,ancho,longitud) :
        self.ancho=ancho
        self.longitud=longitud

    def CalculoPerimetro(self):
        return 2 * self.ancho + 2*self.longitud
            
    def CalculoArea (self):
        return self.ancho * self.longitud
    
