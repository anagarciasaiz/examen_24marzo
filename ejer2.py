class animal():
    def __init__(self, animalito):
        self.animalito= animalito

class mamifero(animal):
    pass

class oviparo(animal):
    pass

class gato(mamifero):
    pass

class ornitorrinco(mamifero, oviparo):
    pass

class pollo(oviparo):
    pass



#si se puede implementar en python con la herencia de clases
#las clases mamifero y oviparo heredan de la clase animal 







