# Clase usuario

# Creamos las clases Usuario, Cliente y Administrador

class Usuario:
    def __init__(self, id_unico, nombre, correo):
        self.id_unico: str = id_unico
        self.nombre: str = nombre
        self.correo: str = correo

    def is_admin(self):
        return False

class Cliente(Usuario):
    def __init__(self, id_unico, nombre, correo, direccion_postal):
        super().__init__(id_unico, nombre, correo)
        self.direccion_postal = direccion_postal

class Administrador(Usuario):
    def is_admin(self) -> bool:
        return True