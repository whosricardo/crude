import csv 
from models.treino import Treino

# Função para adicionar novos Treinos
def adicionar_treino(nome, data, distancia_percorrida, tempo, localizacao, condicoes_climaticas):
    treino = Treino(nome, data, distancia_percorrida, tempo, localizacao, condicoes_climaticas)

    with open('data/treinos.csv', mode='a', newline='') as csvtreinos: # Abrindo o arquivo treinos
        writer = csv.writer(csvtreinos)
        writer.writerow([treino.nome, treino.data, treino.distancia_percorrida, treino.tempo, treino.localizacao, treino.condicoes_climaticas])

def atualizar_treino(nome_treino, novos_dados):
    try:
        treinos = []
        treino_encontrado = False

        with open('data/treinos.csv', mode='r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha[0] == nome_treino:
                    treinos.append(novos_dados)
                    treino_encontrado = True
                else:
                    treinos.append(linha)

        if not treino_encontrado:
            print(f"Treino [{nome_treino}] não encontrado")
            return
        
        with open('data/treinos.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerows(treinos)
            print(f"Treino [{nome_treino}] foi atualizado com sucesso!")

    except FileNotFoundError:
        print(f"Erro: Arquivo 'treinos.csv' não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
# Função para exibir o treinos.csv em lista
def ler_treinos():
    with open('data/treinos.csv', mode='r') as csvtreinos: # Abrindo o arquivo treinos csv no modo "Read"
        reader = csv.reader(csvtreinos)
        for linha in reader:
            print(linha)