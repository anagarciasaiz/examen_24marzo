class Libro:
    def __init__(self, titulo, autor, año, paginas):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.paginas = paginas 
        

    def describir(self):
        print(f"titulo: {self.titulo}")
        print(f"autor: {self.autor}")
        print(f"año: {self.año}")
        print(f"paginas: {self.paginas}")


#ejemplo
libro = Libro("El Principito","Antoine de Saint-Exupéry","1943","120")
libro.describir()





    
