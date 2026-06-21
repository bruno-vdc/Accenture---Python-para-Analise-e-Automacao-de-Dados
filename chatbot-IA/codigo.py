# ============ bibliotecas ============
import json
import pandas as pd
import requests
import streamlit as st
from pathlib import Path

# ======= diretórios e arquivos =======
diretorio = Path(__file__).parent
dir_dados = diretorio / "dados"

perfil = json.load(open(dir_dados / 'perfil_investidor.json'))
transacoes = pd.read_csv(dir_dados / 'transacoes.csv')
historico = pd.read_csv(dir_dados / 'historico_atendimento.csv')
produtos = json.load(open(dir_dados / 'produtos_financeiros.json'))

# ========= interface do chat =========
url_ollama = "http://localhost:11434/api/generate"
modelo_ollama = "gpt-oss"

# ============== prompts ==============
promt_contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

prompt_regras = """
OBJETIVO:
Como assisitente financeiro, você deve instruir o cliente sobre investimentos usando os dados do mesmo como exemplos práticos.

REGRAS:
- Tire dúvidas sobre os tipos de investimentos presentes nos dados;
- Você pode sugerir os investimentos mais adequados para o perfil, mas não pode ordernar o uso de nenhum dos produtos;
- Atenha-se a responder apenas sobre os assuntos de finanças e investimentos presentes nos dados passados;
- Use os dados fornecidos para dar exemplos personalizados;
- Caso alguma pergunta fora do escopo seja feita, lamente por não poder ajudar;
- Caso não saiba a resposta, lamente por não poder ajudar, mas não invente dados sob nenhuma hipótese;
- Use linguagem simples e dê respostas curtas e completas."""

# ========== usando o chatbot =========
def perguntar(msg):
    prompt = f"""
    {prompt_regras}

    CONTEXTO DO CLIENTE:
    {promt_contexto}

    Pergunta: {msg}"""

    r = requests.post(url_ollama, json={"model": modelo_ollama, "prompt": prompt, "stream": False})
    return r.json()['response']


st.title("Assistente Financeiro")

if pergunta := st.chat_input("Sua mensagem"):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))