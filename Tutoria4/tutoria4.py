"""
    @CarlosCastillo10
"""

class Materia(object):
    
    #Constructor
    def __init__(self):
        self.codigo = ""
        self.nombre = ""

    #Metodos de agregar
    def agregar_codigo(self, c):
        self.codigo = c

    def agregar_nombre(self, n):  
        self.nombre = n

     #  Metodos de obtener   
    def obtener_codigo(self):
        return self.codigo


    def obtener_nombre(self):
        return self.nombre

    # Metodo de presentar datos
    def presentar_datos(self):
        return "%s-%s" % (self.obtener_codigo(),self.obtener_nombre())


class MateriaPresencial(Materia):
    #clase que hereda de la clase padre "Materia"

    #Constructor
    def __init__(self):
        
        #Llamamos al constructor de la clase padre "Materia"
        super(Materia, self).__init__()       
        self.num_creditos = 0

    #Metodos de agregar  
    def agregar_num_creditos(self, nc):  
        self.num_creditos = nc

    #Metodos de obtener 
    def obtener_num_creditos(self):
        return self.num_creditos

    #Metodo de presentar datos(Llama al metodo presentar_datos de la clase padre "Materia")
    def presentar_datos(self):
        return "%s-%s" % (super(MateriaPresencial, self).presentar_datos(), self.obtener_num_creditos())


    