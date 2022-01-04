import requests
def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://globallabs.academy/')
    print(response)
    #cep_informado = input('Informe o cep que deseja consultar(somente os números): ')
    #retorna_dados_cep(cep_informado)