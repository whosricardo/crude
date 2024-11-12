import csv
from models.meta import Meta

# Função para adicionar Metas no arquivo metas.csv
def adicionar_meta(nome, distancia, tempo):
    meta = Meta(nome, distancia, tempo)

    #Tratamento de ERRO
    try:
        with open('data/metas.csv', mode='a', newline='') as csvmetas:
            writer = csv.writer(csvmetas)
            writer.writerow([meta.nome, meta.distancia, meta.tempo])
    except FileNotFoundError:
        print("Arquivo não existe")

# Função para atualizar a meta
def atualizar_meta(nome_meta, novos_dados):
    try:
        metas = [] # Lista vazia que será utilizada posteriormente para atualizar os valores
        meta_encontrado = False # Será usada posteriormente para verificação

        with open('data/metas.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for linha in reader:
                if len(linha) == 0: # Verifica o tamanho da linha para não dar erro quando for pedir novos dados
                    continue 
                if linha[0] == nome_meta:
                    if isinstance(novos_dados, list) and len(novos_dados) == len(linha): # Veriricia o tamanho da linha para não dar conflito com os novos valores de OUT of RANGE
                        metas.append(novos_dados)
                    # Tratamento de ERRO
                    else:
                        print("Erro: Os novos dados devem ser uma lista com o mesmo número de colunas.")
                        return
                    meta_encontrado = True
                else:
                    metas.append(linha)
        # Tratamento de ERRO
        if not meta_encontrado:
            print(f"Meta [{nome_meta}] não encontrado")
            return
        # Sobrescrever no arquivo os novos valores
        with open('data/metas.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(metas)
            print(f"Meta [{nome_meta}] foi atualizado com sucesso!")
    # Tratamento de ERRO
    except FileNotFoundError:
        print(f"Erro: Arquivo 'metas.csv' não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Função para deletar o Treino
def deletar_meta(nome_meta):
    try:
        metas = [] # Cria uma lista que posteriromente será usada para sobrescrever os valores no arquivo
        metas_encontrado = False # Check para saber se o treino foi encontrado

        with open('data/metas.csv', mode='r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha[0] != nome_meta: # Vai armazenar em uma lista todos os dados que não sejam o nome que não quer ser deletado
                    metas.append(linha)
                else:
                    metas_encontrado = True # Foi encontrado o treino

        # Tratamento de ERRO
        if not metas_encontrado:
            print(f"Meta [{nome_meta}] não encontrado")
            return
        
        # Vai sobrescrever o arquivo atual com a lista treinos[] sem o dado que foi deletado
        with open('data/metas.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerows(metas)
            print(f"Meta [{nome_meta}] foi deletado com sucesso!")

    # Tratamento de ERRO
    except FileNotFoundError:
        print(f"Erro: Arquivo 'metas.csv' não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Print Metas Função
def mostrar_metas():
    # Tratamento de ERRO
    try:
        with open('data/metas.csv', mode='r') as csvmetas:
            reader = csv.reader(csvmetas)
            
            for linhas in reader:
                print(linhas)
    # Tratamento de ERRO
    except FileNotFoundError:
        print("Arquivo [metas.csv] não encontrado")