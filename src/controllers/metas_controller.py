import csv
from models.meta import Meta

# Função para adicionar Metas no arquivo metas.csv
def adicionar_meta(nome, distancia, tempo):
    meta = Meta(nome, distancia, tempo)

    try:
        with open('data/metas.csv', mode='a', newline='') as csvmetas:
            writer = csv.writer(csvmetas)
            writer.writerow([meta.nome, meta.distancia, meta.tempo])
    except FileNotFoundError:
        print("Arquivo não existe")