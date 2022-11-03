class Propiedad:
      Nombre_Propiedad = ""
      Direccion_Propiedad=""
      Contacto_Propiedad=""

  def __init__(self, nombre_Propiedad, direccion_Propiedad, contacto_Propiedad):
      self.Nombre_Propiedad = nombre_Propiedad,
      self.Direccion_Propiedad = direccion_Propiedad,
      self.Contacto_Propiedad = contacto_Propiedad

  def getNombre_Propiedad(self):
      return self.Nombre_Propiedad

  def getDireccion_Propiedad(self):
      return self.Direccion_Propiedad

  def getContacto_Propiedad(self):
      return self.Contacto_Propiedad

  def setNombre(self, nombre_Propiedad):
      self.Nombre_Propiedad = nombre_Propiedad

  def setDireccion(self, direccion_Propiedad):
      self.Direccion_Propiedad = direccion_Propiedad

  def setContacto(self, contacto_Propiedad):
      self.Contacto_Propiedad = contacto_Propiedad

  def __str__(self):
      return " Nombre: "+self.Nombre_Propiedad+" Direccion: "+self.Direccion_Propiedad+" Contacto: "+str(self.Contacto_Propiedad)
        
if __name__ == '__main__':
      print("Clase Propiedad")
