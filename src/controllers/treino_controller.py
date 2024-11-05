import csv 
from models.treino import Treino

# Função para adicionar novos Treinos
def adicionar_treino(nome, data, distancia_percorrida, tempo, localizacao, condicoes_climaticas):
    treino = Treino(nome, data, distancia_percorrida, tempo, localizacao, condicoes_climaticas)

    with open('data/treinos.csv', mode='a', newline='') as csvtreinos: # Abrindo o arquivo treinos
        writer = csv.writer(csvtreinos)
        writer.writerow([treino.nome, treino.data, treino.distancia_percorrida, treino.tempo, treino.localizacao, treino.condicoes_climaticas])

# Função para atualizar treinos
def atualizar_treino(nome_treino, novos_dados):
    try:
        treinos = [] # Cria uma lista que posteriromente será usada para sobrescrever os valores no arquivo
        treino_encontrado = False # Check para saber se o treino foi encontrado

        with open('data/treinos.csv', mode='r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha[0] == nome_treino: # Vai tentar procurar algum treino que seja com o nome inserido pelo usuário
                    treinos.append(novos_dados) # Caso o treino for encontrado, vai ser adicionadado os novos dados na linha
                    treino_encontrado = True
                else:
                    treinos.append(linha) # Caso não tenha nenhum treino igual com o nome, so vai copiar o arquivo novamente

        # Tratamento de ERRO
        if not treino_encontrado:
            print(f"Treino [{nome_treino}] não encontrado")
            return
        
        # Sobrescrever o arquivo com os novos dados contidos na lista treinos[]
        with open('data/treinos.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerows(treinos)
            print(f"Treino [{nome_treino}] foi atualizado com sucesso!")

    # Tratamento de ERRO
    except FileNotFoundError:
        print(f"Erro: Arquivo 'treinos.csv' não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Função para deletar o Treino
def deletar_treino(nome_treino):
    try:
        treinos = [] # Cria uma lista que posteriromente será usada para sobrescrever os valores no arquivo
        treino_encontrado = False # Check para saber se o treino foi encontrado

        with open('data/treinos.csv', mode='r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha[0] != nome_treino: # Vai armazenar em uma lista todos os dados que não sejam o nome que não quer ser deletado
                    treinos.append(linha)
                else:
                    treino_encontrado = True # Foi encontrado o treino

        # Tratamento de ERRO
        if not treino_encontrado:
            print(f"Treino [{nome_treino}] não encontrado")
            return
        
        # Vai sobrescrever o arquivo atual com a lista treinos[] sem o dado que foi deletado
        with open('data/treinos.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerows(treinos)
            print(f"Treino [{nome_treino}] foi deletado com sucesso!")

    # Tratamento de ERRO
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