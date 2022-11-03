class Estado:
  
  Nombre_Estado = ""

  def __init__(self, nombre_Estado):
       self.Nombre_Estado= nombre_Estado

  def getNombre_Estado(self):
    return self.Nombre_Estado

  def setNombre_Estado(self, nombre_Estado):
    self.Nombre_Estado = nombre_Estado 

  def __str__(self):
     print('Nombre_Estado: '+self.Nombre_Estado)

if __name__ == '__main__':
    print("Clase Estado")
