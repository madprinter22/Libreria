from Libreria import Libreria 
from FileController import FileController
if __name__ == '__main__':
  fc = FileController(
    "data/clientes.txt",
    "data/empleados.txt",
    "data/libros.txt"
  )
  lib = Libreria(fc)
  
  lib.load_data()
  
  print("Clientes: ",lib.get_clientes()) 
  print("Empleados: ",lib.get_empleados())
  print("Libros: ",lib.get_libros())
  
  lib.remove_libro(lib.get_libros()[0])
  print("Ahora los libros son: ",lib.get_libros())
  print("Escribimos los datos en el archivo")
  lib.write_data()