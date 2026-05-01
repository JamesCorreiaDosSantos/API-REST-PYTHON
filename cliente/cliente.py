import requests
import json


url = 'https://geradorapi2.james84089672.repl.co/usuarios/gerar/Bearer 00133e6b4ba85d81c1acd1200c88dfc7'


response = requests.get(url)

if response.status_code == 200:
    # A resposta contém o conteúdo da página ou API em formato de json
    content = response.json()
    print(content)
else:
    # Se a solicitação não for bem-sucedida
    print(f"Erro ao acessar a URL. Código de status: {response.status_code}")