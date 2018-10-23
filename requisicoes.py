# requests lib
import requests

''' Requisições - Request Method:
    get
    post
    São as principais.


Status:
    200 = Deu bom
    404 = Deu ruim

'''


url = str(input('site: '))
cabecalho = {'USER-AGENT': 'Win12'}

'''requisicao = requests.get(url)'''
requisicao = requests.post(url, headers=cabecalho)
print(requisicao.text)



# Site para testar as requisições: https://putsreq.com