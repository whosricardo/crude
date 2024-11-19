# Função para converter para INT
def convercao_int(valor):
    return int(valor)

# Função para mostrar menu
def mostrar_menu():
    print(f"1 - Adicionar Treino")
    print(f"2 - Ler Treinos")
    print(f"3 - Atualizar Treino")
    print(f"4 - Deletar Treino")
    print(f"5 - Filtragem [Distância / Tempo]")
    print(f"6 - Área de [Metas]")
    print(f"7 - Sugestão de treino aleatório")
    print(f"8 - Sair")

# Função para mostrar menu metas
def mostrar_menu_metas():
    print(f"1 - Adicionar Meta")
    print(f"2 - Ler Metas")
    print(f"3 - Atualizar Meta")
    print(f"4 - Deletar Meta")

# Função para perguntar ao usuário
def pergunta_usuario():
    while True:
        try:
            input_usuario = int(input("Insira um numero (1 - 8): "))

            if 1 <=input_usuario <= 8:
                return input_usuario
            # Tratamento de ERRO
            else:
                print("Insira um valor dentro de [1 - 8]")
        # Tratamento de ERRO
        except ValueError:
            print("Por favor insira um [Número]")
        except Exception as e:
            print(f"Ocorreu um ERRO: {e}")

# Função para armazenar os valores para posteriormente usar no controlador adicionar_treino
def perguntar_valores_adicionar():
    while True:
        try:
            nome = input("Insira o nome do treino / competição: ")
            data = input("Insira a data do treino (DD/MM/AAAA): ")
            distancia_percorrida = float(input("Insira a distância percorrida (em KM): "))
            tempo = input("Insira o tempo gasto (formato HH:MM:SS): ")
            localizacao = input("Insira a localização do treino: ")
            condicoes_climaticas = input("Descreva as condições climáticas: ")

            # Cria um dicionario que posteriormente será usado com a função adicionar que recebe os parámetros
            if data and distancia_percorrida >= 0 and nome and tempo and localizacao and condicoes_climaticas:
                return {
                    "nome" : nome,
                    "data" : data,
                    "distancia_percorrida" : distancia_percorrida,
                    "tempo" : tempo,
                    "localizacao" : localizacao,
                    "condicoes_climaticas" : condicoes_climaticas
                }
            else:
                # Tratamento de ERRO
                print("Por favor, preencha os campos corretamente")
        # Tratamento de ERRO
        except ValueError:
            print("Erro na entrada de dados. Por favor, insira os valores corretos.")
        except Exception as e:
            print(f"Ocorreu um ERRO: {e}")

# Função para perguntar os novos valores para atualização
def perguntar_valores_atualizar():
    while True:
        try:
            nome = input("Insira o nome do treino que vai ser atualizado: ")
            nome_novos = input("Insira o nome do treino / competição: ")
            data_novos = input("Insira a data do treino (DD/MM/AAAA): ")
            distancia_percorrida_novos = float(input("Insira a distância percorrida (em km): "))
            tempo_novos = input("Insira o tempo gasto (formato HH:MM:SS): ")
            localizacao_novos = input("Insira a localização do treino: ")
            condicoes_climaticas_novos = input("Descreva as condições climáticas: ")

            if data_novos and distancia_percorrida_novos >= 0 and nome_novos and tempo_novos and localizacao_novos and condicoes_climaticas_novos:
                # Retorna o nome do treino a ser atualizado e uma lista com os novos dados
                return nome, [nome_novos, data_novos, distancia_percorrida_novos, tempo_novos, localizacao_novos, condicoes_climaticas_novos]
            # Tratamento de ERRO
            else:
                print("Por favor, preencha os campos corretamente")
        # Tratamento de ERRO
        except ValueError:
            print("Erro na entrada de dados. Por favor, insira os valores corretos.")
        except Exception as e:
            print(f"Ocorreu um ERRO: {e}")

# Função para armazenar os valores para posteriormente usar no controlador adicionar_meta
def perguntar_valores_meta_adicionar():
    # Tratamento de Entrada
    while True:
        try:
            nome = input("Insira o nome da meta: ")
            distancia = float(input("Insira a distância desejada da meta (em KM): "))
            tempo = input("Insira o tempo desejado para a meta: ")

            # Dicionário para posteriormente ser usado como entrada nos paramêtros
            if distancia >= 0 and nome and tempo:
                return {
                    "nome" : nome,
                    "distancia" : distancia,
                    "tempo" : tempo
                }
            #Tratamento de Erro
            else:
                print("Por favor, preencha os campos corretamente")
        # Tratamento de Erro
        except ValueError:
            print("Erro na entrada de dados. Por favor, insira os valores corretos.")
        except Exception as e:
            print(f"Ocorreu um ERRO: {e}")

def perguntar_valores_meta_atualizar():
    # Tratamento de Entrada
    while True:
        try:
            nome = input("Insira o nome da meta que vai ser atualizada: ")
            nome_novo = input("Insira o nome da meta: ")
            distancia_novo = float(input("Insira a distância desejada da meta (em KM): "))
            tempo_novo = input("Insira o tempo desejado para a meta: ")

            if distancia_novo >= 0 and nome_novo and tempo_novo:
                # Retorna o nome do treino a ser atualizado e uma lista com os novos dados 
                return nome, [nome_novo, distancia_novo, tempo_novo]
            # Tratamento de ERRO
            else:
                print("Por favor, preencha os campos corretamente")
        # Tratamento de ERRO
        except ValueError:
            print("Erro na entrada de dados. Por favor, insira os valores corretos.")
        except Exception as e:
            print(f"Ocorreu um ERRO: {e}")

# Função para receber o valor que será usado para deletar um treino
def perguntar_treino_meta_deletar():
    while True:
        try:
            nome_treino_meta_deletar = str(input("Insira o nome do treino que será deletado: "))
            break
        except ValueError:
            print("Digite uma String")
    return nome_treino_meta_deletar

# Função para receber o valor que será usado para filtrar os treinos
def pergunta_filtro():
    #Tratamento de Entrada
    while True:
        try:
            valor_filtragem = float(input("Insira um valor para usar como filtro: "))
            break
        except ValueError:
            print("Por favor insira um número")

    return valor_filtragem

def mensagem_aleatoria():
    import random

    mensagens = [
        "Ótimo trabalho! Cada passo te deixa mais perto do seu objetivo!",
        "Continue se superando! Você está no caminho certo!",
        "Você é mais forte do que pensa. Vamos para o próximo desafio!",
        "Lembre-se: cada quilômetro é uma vitória!",
        "A consistência é o segredo do sucesso. Continue assim!"
    ]

    mensagem_escolhida = random.choice(mensagens)

    print(f'"{mensagem_escolhida}"')

# Função que será utilizada para o treino aleatorio
def treino_especifico():
    import csv
    treinos = []
    with open("data/treinos.csv", "r") as arquivo:
        reader = csv.reader(arquivo)
        next(reader)  
        for linha in reader:
            treinos.append(linha[0])  
    return treinos

# Função treino Aleatorio
def treino_aleatorio():
    import random
    treinos = treino_especifico()  
    treinos_select = list(treinos)  
    
    treino_random = random.choice(treinos_select)
    print (f" O melhor treino para você hoje é o {treino_random}. Por favor consultar no menu principal")






        
            
            
            
            
            
    
    