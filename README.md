# Documentação do Gerador de Referências

Este código é um gerador de referências que utiliza a biblioteca `PySimpleGUI` para criar uma interface gráfica fácil de usar. Ele ajuda os usuários a gerar referências bibliográficas de acordo com o formato ABNT.

## Requisitos

Você precisará das seguintes bibliotecas para executar este código:

- tkinter
- PySimpleGUI
- datetime
- pyperclip
- locale

Para instalar as bibliotecas necessárias, execute o seguinte comando:

```sh
pip install pysimplegui pyperclip
```

## Como usar

O código cria uma interface gráfica que solicita várias informações sobre a fonte de referência, tais como:

- Nome do autor
- Sobrenome do autor
- Título da matéria
- Nome do site
- Ano da postagem
- Link

Após inserir as informações, o usuário pode clicar no botão "Criar referência" para gerar a referência bibliográfica formatada de acordo com a ABNT.

### Opções adicionais

- **Copiar**: Permite copiar a referência gerada para a área de transferência.
- **Limpar tela**: Limpa todos os campos de entrada e a área de saída.

## Estrutura do código

O código é dividido em duas partes principais: a classe `TelaPython` e o script principal que cria uma instância dessa classe e inicia a interface gráfica.

### Classe TelaPython

A classe `TelaPython` é responsável por criar a janela da interface gráfica e gerenciar todas as interações do usuário.

#### `__init__(self)`

O construtor da classe define o tema, cria o layout da janela e inicializa-a.

#### `Iniciar(self)`

Este método inicia o loop principal da interface gráfica e gerencia as ações do usuário.

### Script principal

O script principal cria uma instância da classe `TelaPython` e inicia a interface gráfica chamando o método `Iniciar`.

## Exemplo de uso

```python
python referencias.py
```

Ao executar o código, uma janela será exibida e o usuário poderá inserir os detalhes da fonte e gerar a referência bibliográfica.

### Exemplo de saída

```
SILVA, João. Título da matéria. Nome do site, 2021. Disponível em: <https://www.exemplo.com>. Acesso em: 18 de Maio de 2023.
```
