import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from dotenv import load_dotenv

# ==========================================
# 1. CARREGAMENTO SEGURO DE CHAVES
# ==========================================
load_dotenv()
CHAVE_GEMINI = os.getenv("GEMINI_API_KEY")
EDGE_FUNCTION_URL = os.getenv("EDGE_FUNCTION_URL")
MINHA_CHAVE_MESTRA = os.getenv("EXTERNAL_API_KEY")

# Dicionário de feeds da BBC por categoria
FEEDS_BBC = {
    "World": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "Technology": "http://feeds.bbci.co.uk/news/technology/rss.xml",
    "Sports": "http://feeds.bbci.co.uk/sport/rss.xml",
    "Entertainment": "http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml"
}

def buscar_noticias(url, categoria):
    print(f"🤖 Buscando notícias de {categoria} na BBC...")
    try:
        resposta = requests.get(url, timeout=10)
        sopa = BeautifulSoup(resposta.content, features="xml")
        noticias = sopa.find_all('item')[:2] # Pegamos as 2 melhores de cada categoria
        
        textos = [f"Manchete: {n.title.text}\nResumo: {n.description.text}" for n in noticias]
        return textos
    except Exception as e:
        print(f"⚠️ Erro ao buscar {categoria}: {e}")
        return []

def gerar_flashcards_ia(textos_noticias, categoria):
    print(f"🧠 Cérebro Gemini analisando {categoria}...")
    noticias_juntas = "\n---\n".join(textos_noticias)
    
    modelo_correto = "gemini-2.5-flash" 
    url_gemini = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo_correto}:generateContent?key={CHAVE_GEMINI}"
    
    comando = f"""
    Leia as notícias de {categoria} abaixo e extraia as 5 palavras/expressões em inglês mais úteis.
    Retorne EXATAMENTE um array JSON puro. Formato:
    [
      {{"front": "palavra", "back": "Tradução: x | Exemplo: y"}}
    ]
    
    Notícias:
    {noticias_juntas}
    """

    payload = {"contents": [{"parts": [{"text": comando}]}]}
    resposta = requests.post(url_gemini, json=payload)
    dados = resposta.json()

    if "candidates" in dados:
        texto_ia = dados['candidates'][0]['content']['parts'][0]['text']
        texto_limpo = texto_ia.replace('```json', '').replace('```', '').strip()
        return json.loads(texto_limpo), noticias_juntas
    else:
        print(f"❌ Erro na IA ({categoria}): {json.dumps(dados, indent=2)}")
        return None, None

def salvar_no_banco(cartoes_json, texto_das_noticias, categoria):
    print(f"💾 Enviando {categoria} para o Lovable...")
    hoje = datetime.now().strftime("%d/%m/%Y")
    
    payload = {
        "deck": {
            "title": f"{categoria} News - {hoje}",
            "source_context": texto_das_noticias,
            "category": categoria # IMPORTANTE: Enviando a categoria
        },
        "flashcards": cartoes_json
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MINHA_CHAVE_MESTRA}"
    }
    
    resposta = requests.post(EDGE_FUNCTION_URL, json=payload, headers=headers)
    
    if resposta.status_code in [200, 201]:
        print(f"✅ Categoria {categoria} salva com sucesso!")
    else:
        print(f"❌ Erro {resposta.status_code} em {categoria}: {resposta.text}")

# === MOTOR PRINCIPAL ===
if __name__ == "__main__":
    for categoria, url in FEEDS_BBC.items():
        textos = buscar_noticias(url, categoria)
        if textos:
            cartoes, texto_fonte = gerar_flashcards_ia(textos, categoria)
            if cartoes:
                salvar_no_banco(cartoes, texto_fonte, categoria)
    print("\n🚀 Processo concluído para todos os temas!")