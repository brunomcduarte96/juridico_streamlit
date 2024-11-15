import streamlit as st
from streamlit_option_menu import option_menu

def main():

    # Configuração inicial da página
    st.set_page_config(
        page_title="Smart Legal",
        page_icon="⚖️",
        layout="wide"
    )

    # Criação do menu na sidebar usando streamlit-option-menu
    with st.sidebar:
        escolha = option_menu(
            menu_title="Menu",  # Oculta o título do menu
            options=["Home", "Base de Clientes", "Open Ai"],  # Opções do menu
            icons=["house", "person", "people"],  # Ícones correspondentes (usando ícones do Bootstrap)
            menu_icon="cast",  # Ícone do menu (canto superior esquerdo)
            default_index=0,  # Página padrão selecionada
            orientation="vertical",  # Orientação vertical
        )

    # Conteúdo condicional baseado na escolha do menu
    if escolha == "Home":
        st.title("🏠 Página Home")
        st.write("Bem-vindo à página inicial!")

    elif escolha == "Base de Clientes":
        st.title("👤 Players")
        st.write("Aqui estão os jogadores.")

    elif escolha == "Open Ai":
        st.title("👥 Teams")
        st.write("Aqui estão os times.")


if __name__ == "__main__":
    main()
