import csv 
from models.treino import Treino

# Função para adicionar novos Treinos
def adicionar_treino(nome, data, distancia_percorrida, tempo, localizacao, condicoes_climaticas):
    treino = Treino(nome, data, distancia_percorrida, tempo, localizacao, condicoes_climaticas)

    with open('data/treinos.csv', mode='a', newline='') as csvtreinos: # Abrindo o arquivo treinos
        writer = csv.writer(csvtreinos)
        writer.writerow([treino.nome, treino.data, treino.distancia_percorrida, treino.tempo, treino.localizacao, treino.condicoes_climaticas])

# Função para atualizar o treino
def atualizar_treino(nome_treino, novos_dados):
    try:
        treinos = [] # Lista vazia que será utilizada posteriormente para atualizar os valores
        treino_encontrado = False # Será usada posteriormente para verificação

        with open('data/treinos.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for linha in reader:
                if len(linha) == 0: # Verifica o tamanho da linha para não dar erro quando for pedir novos dados
                    continue 
                if linha[0] == nome_treino:
                    if isinstance(novos_dados, list) and len(novos_dados) == len(linha): # Veriricia o tamanho da linha para não dar conflito com os novos valores de OUT of RANGE
                        treinos.append(novos_dados)
                    # Tratamento de ERRO
                    else:
                        print("Erro: Os novos dados devem ser uma lista com o mesmo número de colunas.")
                        return
                    treino_encontrado = True
                else:
                    treinos.append(linha)
        # Tratamento de ERRO
        if not treino_encontrado:
            print(f"Treino [{nome_treino}] não encontrado")
            return
        # Sobrescrever no arquivo os novos valores
        with open('data/treinos.csv', mode='w', newline='') as file:
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

# Função para filtrar treinos por tempo / distância
def filtragem_distancia_tempo(valor_inserido):
    treinos = [] # Cria uma lista que posteriormente será usada para mostrar filtragem
    valor_encontrado = False # Check para saber se o valor foi encontrado
    try:
        with open('data/metas.csv', mode='r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if valor_inserido in linha: # Vai verificar se o valor inserido está presente nas linhas
                    treinos.append(linha)
                    valor_encontrado = True
                else:
                    # Tratamento de ERRO
                    print("Não existe algum treino com esse valor inserido")
                    return
    
        # Tratamento de ERRO
        if not valor_encontrado:
            print(f"Valor [{valor_inserido}] não foi encontrado na planilha de [treinos.csv]")
            return

        print(treinos) # Print dos valores filtrados

    except FileNotFoundError:
        print(f"ERRO: Arquivo [treinos.csv] não encontrado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")