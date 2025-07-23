
import streamlit as st
import pandas as pd
import webbrowser

# Simulação de base de dados com perfis (normalmente seria buscado via API)
PERFIS_SIMULADOS = [
    {"nome": "Restaurante Sabor", "usuario": "restaurante_sabor", "telefone": "+5511999998888", "descricao": "Culinária brasileira, delivery rápido."},
    {"nome": "Lanches Express", "usuario": "lanches_express", "telefone": "+5511988887777", "descricao": "Hot dogs e hambúrgueres artesanais."},
    {"nome": "Psiquiatra Dr. Silva", "usuario": "psi_dr_silva", "telefone": "+5511977776666", "descricao": "Atendimento humanizado, plantão 24h."},
    {"nome": "Doces da Ana", "usuario": "doces_ana", "telefone": "+5511966665555", "descricao": "Confeitaria e delivery de doces."},
    {"nome": "Scooters DT", "usuario": "scooters_dt", "telefone": "+5511955554444", "descricao": "Scooters elétricas para locomoção fácil."}
]

st.title("Automação de Prospecção - Protótipo")

# Entrada da palavra-chave
palavra_chave = st.text_input("Digite a palavra-chave para busca (ex: culinária, psiquiatra, scooter)")

if palavra_chave:
    # Filtrar perfis que contenham a palavra-chave na descrição (case insensitive)
    resultados = [perfil for perfil in PERFIS_SIMULADOS if palavra_chave.lower() in perfil["descricao"].lower()]
    
    if resultados:
        st.write(f"Perfis encontrados com a palavra-chave '{palavra_chave}':")
        df = pd.DataFrame(resultados)
        st.dataframe(df[["nome", "usuario", "descricao", "telefone"]])

        # Selecionar um perfil para contato
        selecionado = st.selectbox("Selecione um perfil para enviar mensagem via WhatsApp", df["nome"])
        perfil_selecionado = next((p for p in resultados if p["nome"] == selecionado), None)

        if perfil_selecionado:
            mensagem_default = f"Olá {perfil_selecionado['nome']}, tudo bem? Vi que você trabalha com {palavra_chave} e gostaria de apresentar uma proposta que pode ajudar seu negócio."
            mensagem = st.text_area("Edite a mensagem para enviar:", mensagem_default)

            # Botão para abrir o WhatsApp
            if st.button("Enviar mensagem no WhatsApp"):
                numero = perfil_selecionado["telefone"].replace("+", "").replace(" ", "")
                url_whatsapp = f"https://wa.me/{numero}?text={mensagem.replace(' ', '%20')}"
                st.markdown(f"[Clique aqui para abrir o WhatsApp](https://wa.me/{numero}?text={mensagem.replace(' ', '%20')})")
    else:
        st.warning("Nenhum perfil encontrado para essa palavra-chave.")
