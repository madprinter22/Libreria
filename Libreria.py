class Libreria():
  def __init__(self,file_controller) -> None:
    self.libros = []
    self.empleados = []
    self.clientes = []
    self.file_controller = file_controller
  def load_data(self):
    self.clientes=self.file_controller.load_clientes()
    self.empleados=self.file_controller.load_empleados()
    self.libros=self.file_controller.load_libros()
  def write_data(self):
    self.file_controller.write_clientes(self.clientes)
    self.file_controller.write_empleados(self.empleados)
    self.file_controller.write_libros(self.libros)
  #libros
  def add_libro(self, libro):
    self.libros.append(libro)
  def remove_libro(self, libro):
    self.libros.remove(libro)
  def get_libros(self):
    return self.libros
  
  #Empleados
  def add_empleado(self, empleado):
    self.empleados.append(empleado)
  def get_empleados(self):
    return self.empleados
  def remove_empleado(self, empleado):
    self.empleados.remove(empleado)
  
  #Clientes
  def add_cliente(self, cliente):
    self.clientes.append(cliente)
  def remove_cliente(self, cliente):
    self.clientes.remove(cliente)
  def get_clientes(self):
    return self.clientes
    