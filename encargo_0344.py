
print("jireh correa 0344\n")

# Zona de clases
class producto0344:
    # Zona de atributos
    producto = ""
    direcciondeenvio = " "
    tipo_transporte = " "
    fecha_salida = " "
    fecha_entrega = ""
    costo  = 0
    lote_id = 0

    # Zona de funciones dentro de la clase
    def mi_Lista0344(self):
        frutas = ["platano", "naranja", "manzana", "pepino", "guayaba"]
        for x in frutas:
            print(x)

    def mi_Tupla0344(self):
        camiones = ("camion1", "camion2", "camion3", "camion4", "camion5")
        for y in camiones:
            print(y)

    def mi_Diccionario0344(self):
        diccionarioprecios = {
            "platano: ": 100,
            "naranja ": 200,
            "manzana: ": 300,
            "pepino: ": 400,
            "guayaba: ": 500
        }
        for x, y in diccionarioprecios.items():
            print(x, y)

    def mostrardatos0344(self):
        print(f" producto: {self.producto}")
        print(f"precio: {self.direcciondeenvio}")
        print(f"transporte: {self.tipo_transporte}")
        print(f"salida: {self.fecha_salida}")
        print(f"entrega: {self.fecha_entrega}")
        print(f"costo: {self.costo}")
        print(f"lote: {self.lote_id}")

    def altas0344(self):
        print("El registro se realizo correctamente")
        
    def bajas0344(self):
        print("El registro no se realizo correctamente")
        
# Zona de creación de objetos
jireh = producto0344()

# Asignación de valores 
jireh.lote_id = 0
jireh.direcciondeenvio = 150
jireh.tipo_transporte = "camion"
jireh.fecha_salida = "ayer"
jireh.fecha_entrega = 24
jireh.costo = 100
jireh.producto = "platano"

# Usando el objeto Rodolfo para mostrar la información
print("\nListado de alumnos")
jireh.mi_Lista0344()
print("\nListado de materias")
jireh.mi_Diccionario0344()
print("\nListado de maestros")
jireh.mi_Tupla0344()
print("\nResultados")
jireh.mostrardatos0344()
print("  ")
jireh.altas0344()
print("  ")
jireh.bajas0344()