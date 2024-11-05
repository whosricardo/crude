class Meta:
    # Contructor da classe
    def __init__(self, nome, distancia, tempo):
        self.nome = nome
        self.distancia = distancia
        self.tempo = tempo

    def print_string(self):
        print(f"Nome = {self.nome} / Distancia = {self.distancia} / Tempo = {self.tempo}")