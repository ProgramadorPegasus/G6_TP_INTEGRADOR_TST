class OperatoriaComercial:
  
  Nombre_OperatoriaComercial = ""

  def __init__(self, nombre_OperatoriaComercial):
       self.Nombre_OperatoriaComercial= nombre_OperatoriaComercial

  def getNombre_OperatoriaComercial(self):
    return self.Nombre_OperatoriaComercial

  def setNombre_OperatoriaComercial(self, nombre_OperatoriaComercial):
    self.Nombre_OperatoriaComercial = nombre_OperatoriaComercial 

  def __str__(self):
     print('Nombre Operatoria Comercial:'+self.Nombre_OperatoriaComercial)

if __name__ == '__main__':
    print("Clase Operatoria Comercial")

