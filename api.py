# instala a biblioteca requests no meu programa
import requests
# importa biblioteca que imprime bonito Pretty Print
import pprint
# dando um apelido pro comando
bunitinho =  pprint.pprint
# dominio e path base da api
domain = 'https://dadosabertos.camara.leg.br/api/v2/'


def busca_deputado_nome():
    # recurso a ser utilizado
    path = 'deputados'
    # endereco a ser pesquisado
    url = domain + path
    # parametros
    params = {'nome': '', 'ordem': 'asc', 'ordenarPor': 'id'}
    params['nome'] = input('qual o nome do deputado:')
    # faz um get no site dados abertos da camara e obtem a listagem dos deputados
    r = requests.get(url,params)
    # verifica se a rquisicao deu certo
    if(r.status_code == 200):
        # converte os dados para json
        data = r.json()
        # verifica se o deputado existe
        if (data['dados']):
            # imprime somente o nome e o id do deputado
            for deputado in data['dados']:
                print('nome:',deputado['nome'],' id:',deputado['id'])
        else:
            print("não ecxiste nenhum deputado com esse nome")
    else:
        print("deu ruim, requisição com erro")
        bunitinho(r.json())

def busca_despesas_id():
    #id do deputado
    id = input('qual o id do deputado:')
    # recurso a ser utilizado
    #interpola o id do deputado junto ao path
    path = f'deputados/{id}/despesas'
    # endereco a ser pesquisado
    url = domain + path
    # faz um get no site dados abertos da camara e obtem a listagem dos deputados
    r = requests.get(url)
    # verifica se a rquisicao deu certo
    if(r.status_code == 200):
        # converte os dados para json
        data = r.json()
        # verifica se o deputado existe
        if (data['dados']):

            # imprime uma lista de despesas
            for despesa in data['dados']:
                print('=========================================================')
                print('despesa:',despesa['tipoDespesa'])
                print('data:',despesa['dataDocumento'])
                print('valor:',despesa['valorDocumento'])
                print('nota fiscal:',despesa['urlDocumento'])
        else:
            print("não ecxiste nenhum deputado com esse nome")
    else:
        print("deu ruim, requisição com erro")
        bunitinho(r.json())
busca_deputado_nome()
busca_despesas_id()