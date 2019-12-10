class elemento:
    cod=0
    nombre=""
    precio=0
    cantidad=0

    def __init__(self,codigo,nombre,precio,cantidad):
        self.cod=codigo
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
    
    def toString(self):
        return {
            'codigo': str(self.cod),
            'nombre': self.nombre,
            'precio': str(self.precio),
            'cantidad': str(self.cantidad),
            'total':str(self.total())
        }
    def total(self):
        return str(int(self.precio)*int(self.cantidad))