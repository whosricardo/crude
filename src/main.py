import os
from utils.funcoes import *
from controllers.treino_controller import adicionar_treino, ler_treinos, atualizar_treino
from controllers.metas_controller import adicionar_meta, atualizar_meta, mostrar_metas

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
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
        os.system('cls' if os.name == 'nt' else 'clear')

        mostrar_menu_metas()

        resposta_usuario_metas = pergunta_usuario()

        if resposta_usuario_metas == 1:
            dados_meta = perguntar_valores_meta_adicionar()
            adicionar_meta(**dados_meta)

        elif resposta_usuario_metas == 2:
            mostrar_metas()

        elif resposta_usuario_metas == 3:
            nome_meta, novos_dados_meta = perguntar_valores_meta_atualizar()
            atualizar_meta(nome_meta, novos_dados_meta)

        elif resposta_usuario_metas == 4:
            print("Template")

    return True

if __name__ == '__main__':
    main()