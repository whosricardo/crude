# Função para converter para INT
def convercao_int(valor):
    return int(valor)

# Função para mostrar menu
def mostrar_menu():
    print(f"1 - Adicionar Treino")
    print(f"2 - Ler Treinos")
    print(f"3 - Atualizar Treinos")

# Função para perguntar ao usuário
def pergunta_usuario():
    while True:
        try:
            input_usuario = int(input("Insira um numero (1 - 3)"))

            if 1 <=input_usuario <= 3:
                return input_usuario
            # Tratamento de ERRO
            else:
                print("Insira um valor dentro de [1 - 3]")
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
            distancia_percorrida = float(input("Insira a distância percorrida (em km): "))
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
