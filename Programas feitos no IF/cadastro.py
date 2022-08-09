from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key = 'usuario')],
    [sg.Text('Senha'), sg.Input(key = 'senha', password_char=('*'))],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Logar')]
]    
# janela
janela = sg.Window('Paulão da Regulagem', layout)
# ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Logar':
        if valores['usuario'] == 'Fabricio' and valores['senha'] == 'fabricio122':
            print('ESTAAA VIVOOOOOOOOOO')
        else:
            print('TEU PC PEGOU VIRUS VACILÃO!!!')