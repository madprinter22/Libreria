class FileController():
  def __init__(self,file_clientes,file_empleados,file_libros) -> None:
    self.file_clientes= file_clientes
    self.file_empleados= file_empleados
    self.file_libros = file_libros
    
  #!metodos para clientes
  def load_clientes(self):
    with open(self.file_clientes,"r") as txt_clientes:
      return txt_clientes.readlines()
  def write_clientes(self,clientes):
    with open(self.file_clientes,"w") as txt_clientes:
      txt_clientes.writelines(clientes)
    
  #!metodos para libros
  def load_libros(self):
    with open(self.file_libros,"r") as txt_libros:
      return txt_libros.readlines()
  def write_libros(self,libros):
    with open(self.file_libros,"w") as txt_libros:
      txt_libros.writelines(libros)
  
  #!metodos para clientes
  def load_empleados(self):
    with open(self.file_empleados,"r") as txt_empleados:
      return txt_empleados.readlines()
  def write_empleados(self,empleados):
    with open(self.file_empleados,"w") as txt_empleados:
      txt_empleados.writelines(empleados)