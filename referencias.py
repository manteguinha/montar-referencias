import PySimpleGUI as sg
from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

data_atual = date.today()
data_em_texto = data_atual.strftime('%d de %B de %Y')

class TelaPython:
    sg.theme('Purple')
    def __init__(self):
        layout = [
            [sg.Text('Nome do autor', size=(18,0)), sg.Input(size=(30,0), key='autor')],
            [sg.Text('Sobrenome do autor', size=(18,0)), sg.Input(size=(30,0), key='sobrenome')],
            [sg.Text('Titulo da matéria', size=(18,0)), sg.Input(size=(30,0), key='titulo')],
            [sg.Text('Nome do site', size=(18,0)), sg.Input(size=(30,0), key='nome_site')],
            [sg.Text('Ano da postagem', size=(18,0)), sg.Input(size=(30,0), key='ano')],
            [sg.Text('Link', size=(18,0)), sg.Input(size=(30,0), key='link')],
            [sg.Button('Criar referência',  font=("Arial", 10)), sg.Button('Fechar', font=("Arial", 10))],
            
            [sg.Output(size=(50,10))]
        ]
        self.janela = sg.Window("Criar referências",  font=("Arial", 12)).layout(layout)
    
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            if self.button == 'Fechar':
                break
            nome_autor = self.values['autor']
            nomeAutor = nome_autor.capitalize()
            sobrenome_autor = self.values['sobrenome']
            sobrenomeAutor = sobrenome_autor.upper()
            titulo_materia = self.values['titulo']
            site = self.values['nome_site']
            ano_post = self.values['ano']
            link_site = self.values['link']
            print(f'{" ".join(sobrenomeAutor.split())}, {" ".join(nomeAutor.split())}. {" ".join(titulo_materia.split())}. {" ".join(site.split())}, {" ".join(ano_post.split())}. Disponível em: <{link_site.replace(" ", "")}>. Acesso em: {data_em_texto}.')
            print(f'\n')

tela = TelaPython()
tela.Iniciar()

