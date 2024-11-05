from utils.funcoes import mostrar_menu, pergunta_usuario, perguntar_valores_adicionar, perguntar_valores_atualizar
from controllers.treino_controller import adicionar_treino, ler_treinos, atualizar_treino

def main():
    mostrar_menu()
    resposta_usuario = pergunta_usuario()

    if resposta_usuario == 1:
        dados_treino = perguntar_valores_adicionar()
        adicionar_treino(**dados_treino)

    elif resposta_usuario == 2:
        ler_treinos()

    elif resposta_usuario == 3:
        nome_treino, novos_dados = perguntar_valores_atualizar()
        atualizar_treino(nome_treino, novos_dados)

    elif resposta_usuario == 4:
        print("Template")

    return True

if __name__ == '__main__':
    main()