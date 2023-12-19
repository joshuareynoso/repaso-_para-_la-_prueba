class Rectangulo:
    def __init__(self,ancho,largo):
        self.ancho=ancho
        self.largo=largo    
        
    def calculo(self):
        perimetro = 2 * self.ancho + 2*self.largo
        return perimetro
    
    def calculo2 (self):
        area = self.ancho * self.largo
        return area
    
    
    
