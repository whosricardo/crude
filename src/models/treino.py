class Treino:
    def __init__(self, nome, data, distancia_percorrida, tempo, localizacao, condicoes_climaticas):
        self.nome = nome
        self.data = data
        self.distancia_percorrida = distancia_percorrida
        self.tempo = tempo
        self.localizacao = localizacao
        self.condicoes_climaticas = condicoes_climaticas

    def print_string(self):
        print(f"Nome = {self.nome} / Data = {self.data} / Distancia Percorrida = {self.distancia_percorrida} / Tempo = {self.tempo} / Localização = {self.localizacao} / Condições Climáticas {self.condicoes_climaticas}")