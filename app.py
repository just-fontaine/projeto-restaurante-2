import requests; import json

# endpoint
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
# solicitar informações
response = requests.get(url)

# print(response)

# Se der tudo certo
if response.status_code == 200:
    # transforma a response em json
    dados_json = response.json()
    # cria um dicionario vazio
    dados_restaurante = {}
    # para cada item nos dados json
    for item in dados_json:
        # armazena o nome do restaurante numa variavel
        nome_restaurante = item['Company']
        # se o nome não estiver no dicionario
        if nome_restaurante not in dados_restaurante:
            # cria uma chave (nome do restaurante) com uma lista vazia
            dados_restaurante[nome_restaurante] = []
        # adiciona os dados do restaurante na lista criada
        dados_restaurante[nome_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
# Se der errado
else:
    # Mostra o codigo do erro
    print(f'Erro: {response.status_code}')

# Criando arquivo de cada restaurante separado
# para cada restaurante, e seus dados no dicionario do restaurante
for nome_do_restaurante, dados in dados_restaurante.items():
    # o nome do arquivo vai ser nome_do_restaurante.json
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    # cria um arquivo
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        # escreve nele os dados do arquivo
        json.dump(dados, arquivo_restaurante, indent=4)
