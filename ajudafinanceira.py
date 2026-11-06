%%writefile app.py
import streamlit as st
import google.generativeai as genai

# Coloque a sua chave copiada dentro das aspas abaixo
CHAVE_API = "AQ.Ab8RN6IrQFGAd7K-5V1MaCgvEo77ONlU8r4NEYFL9Z7kBmTAkA"
genai.configure(api_key=CHAVE_API)

st.title("🤝 Assistente de Orientação Financeira Ética")
st.write("Insira seus dados abaixo para receber orientações baseadas nos decretos vigentes.")

token_usuario = st.text_input("Insira sua Chave de Acesso recebida por e-mail:", type="password")

if token_usuario:
    if token_usuario == "AJUDA2026-VALIDA":
        st.success("Acesso liberado! Restam 100 consultas este mês.")
        
        contexto_decretos = """
        Você é um agente financeiro ético e acolhedor focado em ajudar o povão endividado.
        Sua base de conhecimento inclui as regras protetivas do Código de Defesa do Consumidor 
        e diretrizes de renegociação de dívidas. Traduza o juridiquês para uma linguagem simples.
        Nunca dê falsas esperanças. Se a margem consignada passou do limite legal, 
        oriente o usuário a buscar a Defensoria ou o Procon local.
        """
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Como posso te ajudar a sair do sufoco hoje?"):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Alterado para o modelo atual estável e rápido
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"{contexto_decretos}\n\nPergunta do usuário: {prompt}")

            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    else:
        st.error("Chave de acesso inválida ou expirada.")
