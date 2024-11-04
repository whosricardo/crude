# Função para converter para INT
def convercao_int(valor):
    return int(valor)

# Função para mostrar menu
def mostrar_menu():
    print(f"1 - Adicionar Treino")
    print(f"2 - Ler Treinos")

# Função para perguntar ao usuário
def pergunta_usuario():
    while True:
        try:
            input_usuario = int(input("Insira um numero (1 - 2)"))

            if 1 <=input_usuario <= 2:
                return input_usuario
            else:
                print("Insira um valor dentro de [1 - 2]")

        except ValueError:
            print("Por favor insira um [Número]")
        except Exception as e:
            print(f"Ocorreu um ERRO: {e}")

# Função para armazenar os valores para posteriormente usar no controlador adicionar_treino
def perguntar_valores_adicionar():
    while True:
        try:
            data = input("Insira a data do treino (DD/MM/AAAA): ")
            distancia_percorrida = float(input("Insira a distância percorrida (em km): "))
            tempo = input("Insira o tempo gasto (formato HH:MM:SS): ")
            localizacao = input("Insira a localização do treino: ")
            condicoes_climaticas = input("Descreva as condições climáticas: ")

            if data and distancia_percorrida >= 0 and tempo and localizacao and condicoes_climaticas:
                return {
                    "data" : data,
                    "distancia_percorrida" : distancia_percorrida,
                    "tempo" : tempo,
                    "localizacao" : localizacao,
                    "condicoes_climaticas" : condicoes_climaticas
                }
            else:
                print("Por favor, preencha os campos corretamente")
            
        except ValueError:
            print("Erro na entrada de dados. Por favor, insira os valores corretos.")
        except Exception as e:
            print(f"Ocorreu um ERRO: {e}")