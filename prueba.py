class RECTANGULO:
    def __init__(self,ancho,longitud) :
        self.ancho=ancho
        self.longitud=longitud

    def CalculoPerimetro(self):
        return 2 * self.ancho + 2*self.longitud
            
    def CalculoArea (self):
        return self.ancho * self.longitud
    
objeto1 = RECTANGULO(20,15)

objto2= objeto1.CalculoArea()+objeto1.CalculoPerimetro()
print("El perímetro del rectángulo es:", objeto1.CalculoPerimetro())
print("El área del rectángulo es:", objeto1.CalculoArea())


