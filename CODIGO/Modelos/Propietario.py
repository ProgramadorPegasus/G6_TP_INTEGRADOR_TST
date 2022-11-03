class Propietario:
  Nombre_Propietario = ""
  Direccion_Propietario=""
  Contacto_Propietario=""

  def __init__(self, nombre_Propietario, direccion_Propietario, contacto_Propietario):
       self.Nombre_Propietario= nombre_Propietario,
       self.Direccion_Propietario= direccion_Propietario,
       self.Contacto_Propietario= contacto_Propietario

  def get_nombre_Propietario(self):
    return self.Nombre_Propietario
  
  def get_direccion_Propietario(self):
    return self.Direccion_Propietario
  
  def get_contacto_Propietario(self):
    return self.Contacto_Propietario  

  def set_nombre_Propietario(self, nombre_Propietario):
    self.Nombre_Propietario = nombre_Propietario 
  
  def set_direccion_Propietario(self, direccion_Propietario):
    self.Direccion_Propietario = direccion_Propietario 

  def set_contacto_Propietario(self, contacto_Propietario):
    self.Contacto_Propietario = contacto_Propietario 
  
  def __str__(self):
    return "Nombre del propietario: " + str(self.Nombre_Propietario) + " Direccion: " + str(self.Direccion_Propietario) + "  Contacto: " + str(self.Contacto_Propietario)

  if __name__ == '__main__':
    print("Clase Propietario")