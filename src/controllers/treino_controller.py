import csv 
from models.treino import Treino

# Função para adicionar novos Treinos
def adicionar_treino(data, distancia_percorrida, tempo, localizacao, condicoes_climaticas):
    treino = Treino(data, distancia_percorrida, tempo, localizacao, condicoes_climaticas)

    with open('data/treinos.csv', mode='a', newline='') as csvtreinos: # Abrindo o arquivo treinos
        writer = csv.writer(csvtreinos)
        writer.writerow([treino.data, treino.distancia_percorrida, treino.tempo, treino.localizacao, treino.condicoes_climaticas])

# Função para exibir o treinos.csv em lista
def ler_treinos():
    with open('data/treinos.csv', mode='r') as csvtreinos: # Abrindo o arquivo treinos csv no modo "Read"
        reader = csv.reader(csvtreinos)
        for linha in reader:
            print(linha)