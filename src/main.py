import os
from utils.funcoes import *
from controllers.treino_controller import adicionar_treino, ler_treinos, atualizar_treino, filtragem_distancia_tempo, deletar_treino
from controllers.metas_controller import adicionar_meta, atualizar_meta, mostrar_metas 

def main():
    # Clear Console
    os.system('cls' if os.name == 'nt' else 'clear')
    mostrar_menu()
    resposta_usuario = pergunta_usuario()

    # Adicionar Treinos
    if resposta_usuario == 1:
        dados_treino = perguntar_valores_adicionar()
        adicionar_treino(**dados_treino)

    # Ler Treinos
    elif resposta_usuario == 2:
        ler_treinos()

    # Atualizar Treinos
    elif resposta_usuario == 3:
        nome_treino, novos_dados = perguntar_valores_atualizar()
        atualizar_treino(nome_treino, novos_dados)

    # Deletar Treinos
    elif resposta_usuario == 4:
        nome_treino = perguntar_treino_meta_deletar()
        deletar_treino(nome_treino)

    # Filtrar Treinos
    elif resposta_usuario == 5:
        valor_filtragem = pergunta_filtro()
        valor_filtragem_converter = str(valor_filtragem)
        filtragem_distancia_tempo(valor_filtragem_converter)

    # Menu Metas
    elif resposta_usuario == 6:
        #Clear Console
        os.system('cls' if os.name == 'nt' else 'clear')

        mostrar_menu_metas()

        resposta_usuario_metas = pergunta_usuario()

        # Adicionar Metas
        if resposta_usuario_metas == 1:
            dados_meta = perguntar_valores_meta_adicionar()
            adicionar_meta(**dados_meta)

        # Ler Metas
        elif resposta_usuario_metas == 2:
            mostrar_metas()

        # Atualizar Metas
        elif resposta_usuario_metas == 3:
            nome_meta, novos_dados_meta = perguntar_valores_meta_atualizar()
            atualizar_meta(nome_meta, novos_dados_meta)

        # Deletar Metas
        elif resposta_usuario_metas == 4:
            print("Template")

    return True

if __name__ == '__main__':
    main()