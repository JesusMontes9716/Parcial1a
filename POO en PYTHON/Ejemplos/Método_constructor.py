class Cachorro():

    def __init__(self, color, raza):
        self.color = color
        self.raza = raza


perrito = Cachorro("Marrón claro", "Golden retriever")

print("Este es un cachorro de la raza {} y es de color {}".format(perrito.raza, perrito.color))