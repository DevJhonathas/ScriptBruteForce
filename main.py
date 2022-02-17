import requests

class buscandoInformacoes:
    def __init__(self):
        self.requisicaoApi()
        pass
    def requisicaoApi(self):
        self.requisicao = requests.get("http://sistema.fiscaldefender.com.br/admin/login")
        print(self.requisicao.content)
buscandoInformacoes()