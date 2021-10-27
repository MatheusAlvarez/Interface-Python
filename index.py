from tkinter.constants import FALSE
from PySimpleGUI import PySimpleGUI as sg

sg.theme('BlueMono')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(30, 1))],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(30, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Tela de Login (Matheus Maia Alvarez)', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'matheus' and valores['senha'] == '123456':
            print('Bem-vindo')