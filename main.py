#importar o App, Builder(GUI)
#Criar nosso Aplicativo
#criar a funçao build

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("Tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI #Até aqui é tudo padrao do kivy

    def on_start(self): #Aqui são as mudanças que desejo fazer no app #self = sempre faz referencia ao MeuAplicativo
        self.root.ids["moeda1"].text = f"Dólar R${self.pegar_cotacao('USD')}" #root = referencia pra Tela.kv #ids = referencia aos id das moedas
        self.root.ids["moeda2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicativo().run() #roda o app