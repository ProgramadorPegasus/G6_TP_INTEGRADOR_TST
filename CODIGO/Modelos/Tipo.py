class Tipo:
  Nombre_Tipo = ""

  def __init__(self, nombre_Tipo):
       self.Nombre_Tipo= nombre_Tipo

  def get_Nombre_Tipo(self):
    return self.get_nombre_Tipo

  def set_nombre_Tipo(self, nombre_Tipo):
    self.Nombre_Tipo = nombre_Tipo 

  def __str___(self):
     print('Nombre_Tipo: '+str(self.Nombre_Tipo))
     