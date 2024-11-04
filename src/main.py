from utils.funcoes import mostrar_menu, pergunta_usuario, perguntar_valores_adicionar
from controllers.treino_controller import adicionar_treino, ler_treinos

def main():
    mostrar_menu()
    resposta_usuario = pergunta_usuario()

    if resposta_usuario == 1:
        dados_treino = perguntar_valores_adicionar()
        adicionar_treino(**dados_treino)

    elif resposta_usuario == 2:
        ler_treinos()

    return True

if __name__ == '__main__':
    main()