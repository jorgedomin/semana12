class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla para título y autor
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar los libros prestados al usuario

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios_registrados = set()  # Conjunto para IDs de usuarios únicos

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.add(usuario.id_usuario)

    def dar_de_baja_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario.id_usuario)

    def prestar_libro(self, libro, usuario):
        if libro.isbn in self.libros_disponibles and usuario.id_usuario in self.usuarios_registrados:
            self.libros_disponibles.pop(libro.isbn)
            usuario.libros_prestados.append(libro)

    def devolver_libro(self, libro, usuario):
        if libro in usuario.libros_prestados:
            usuario.libros_prestados.remove(libro)
            self.libros_disponibles[libro.isbn] = libro

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor in libro.titulo_autor[0]:
                resultados.append(libro)
            elif criterio == "autor" and valor in libro.titulo_autor[1]:
                resultados.append(libro)
            elif criterio == "categoria" and valor == libro.categoria:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, usuario):
        return usuario.libros_prestados

# Ejemplo de uso
if __name__ == "__main__":
    # Crear libros
    libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", "Fantasía", "978-84-450-7359-2")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "978-84-376-0494-7")

    # Crear usuarios
    usuario1 = Usuario("Juan", 1)
    usuario2 = Usuario("Ana", 2)

    # Crear biblioteca
    biblioteca = Biblioteca()

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro(libro1, usuario1)
    biblioteca.prestar_libro(libro2, usuario2)

    # Mostrar libros prestados a un usuario
    print("Libros prestados a Juan:", biblioteca.listar_libros_prestados(usuario1))

    # Devolver libros
    biblioteca.devolver_libro(libro1, usuario1)

    # Mostrar libros prestados después de la devolución
    print("Libros prestados a Juan después de la devolución:", biblioteca.listar_libros_prestados(usuario1))

    # Buscar libros por título
    resultados_busqueda = biblioteca.buscar_libros("titulo", "soledad")
    print("Resultados de la búsqueda por título:", resultados_busqueda)
