from tkinter.font import BOLD
import PySimpleGUI as sg
from datetime import date
import pyperclip
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

data_atual = date.today()
data_em_texto = data_atual.strftime('%d de %B de %Y')

class TelaPython:
    sg.theme('Purple')
    def __init__(self):
        layout = [
            [sg.Menu([['Sobre',['Versão']],
                ['Sair',['Sair']]], font=("Arial", 8))],
            [sg.Text('Nome do autor', size=(18,0)), sg.Input(size=(32,0), key='autor')],
            [sg.Text('Sobrenome do autor', size=(18,0)), sg.Input(size=(32,0), key='sobrenome')],
            [sg.Text('Titulo da matéria', size=(18,0)), sg.Input(size=(32,0), key='titulo')],
            [sg.Text('Nome do site', size=(18,0)), sg.Input(size=(32,0), key='nome_site')],
            [sg.Text('Ano da postagem', size=(18,0)), sg.Input(size=(32,0), key='ano')],
            [sg.Text('Link', size=(18,0)), sg.Input(size=(32,0), key='link')],
            [sg.Button('Criar referência', font=("Arial", 10, BOLD)), 
                sg.Button('Copiar', font=("Arial", 10, BOLD)),
                sg.Button('Limpar tela', font=("Arial", 10, BOLD))], 
            [sg.Output(size=(50,15), key='_OUTPUT_')]
        ]
        self.janela = sg.Window("Criar referências", font=("Arial", 12)).layout(layout)
    
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            if self.button in (None, sg.WINDOW_CLOSED, 'Sair'):
                break
            if self.button == 'Versão':
                sg.popup('''Versão: 0.7.0 \nData da modificação: 18-05-2022
                                    \nMudanças: \nMelhorias na criação de referências. \nCorreção de bugs.
                                    \nCreated by: @manteguinha_mantega''',
                     font=("Arial", 10, BOLD))

            if self.button == 'Criar referência':
                if self.values['autor'] == '':
                    nome_autor = ''
                else:
                    nome_autor = self.values['autor'].title()+'. '
              
                if self.values['sobrenome'] == '':
                    sobrenome_autor = ''
                else:
                    sobrenome_autor = self.values['sobrenome'].upper()+', '
               
                if self.values['titulo'] == '':
                    titulo_materia = ''
                else:
                    titulo_materia = self.values['titulo']+'. '
              
                if self.values['nome_site'] == '':
                    site = ''
                else:
                    site = self.values['nome_site']+', '
          
                if self.values['ano'] == '':
                    ano_post = ''
                else:
                    ano_post = self.values['ano']+'. '
           
                if self.values['link'] == '':
                    link_site = ''
                else:
                    link_site = self.values['link']
                    
                print(f'{sobrenome_autor}{nome_autor}{titulo_materia}{site}{ano_post}Disponível em: <{link_site.replace(" ", "")}>. Acesso em: {data_em_texto}.\n')
                self.janela.find_element('autor').Update('')
                self.janela.find_element('sobrenome').Update('')
                self.janela.find_element('titulo').Update('')
                self.janela.find_element('nome_site').Update('')
                self.janela.find_element('ano').Update('')
                self.janela.find_element('link').Update('')

            if self.button == 'Limpar tela':
                self.janela['_OUTPUT_'].update(value='')
                self.janela.find_element('autor').Update('')
                self.janela.find_element('sobrenome').Update('')
                self.janela.find_element('titulo').Update('')
                self.janela.find_element('nome_site').Update('')
                self.janela.find_element('ano').Update('')
                self.janela.find_element('link').Update('')

            if self.button == 'Copiar':
                output = self.janela.find_element('_OUTPUT_').Get()
                pyperclip.copy(output)
                sg.popup_quick_message('Referência compiada!', background_color = 'LightGray', font=("Arial", 8, BOLD))   

tela = TelaPython()
tela.Iniciar()
