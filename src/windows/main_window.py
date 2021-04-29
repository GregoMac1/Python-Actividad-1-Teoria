import PySimpleGUI as sg
from src import constants

sg.theme('DefaultNoMoreNagging')

texto_uno = 'Obtener las canciones de la banda Foo Fighters cuya fecha de lanzamiento sea entre el 2000 y el 2010 en un archivo JSON.'
texto_dos = ''

def build():
    left_col_layout = [
        [sg.Text(texto_uno,size=(35,4),justification='c')],
        [sg.Button('Analizar canciones de Rock',key=('-OPTION_ONE-'),size=(30,1))],
        [sg.Text(f'Dataset:\n{constants.first}',size=(30,4),justification='c')]
    ]
    right_col_layout = [
        [sg.Text(texto_dos,size=(35,4),justification='c')],
        [sg.Button('Analizar resultados de fútbol',key=('-OPTION_TWO-'),size=(30,1))],
        [sg.Text(f'Dataset:\n{constants.second}',size=(30,4),justification='c')]
    ]

    layout = [
        [sg.Text('Escoja los datos a analizar',font=('Bahnschrift SemiLight',32),size=(30,2),justification='center')],
        [sg.Column(left_col_layout, element_justification='c'), sg.Column(right_col_layout, element_justification='c')],
        [sg.Button('Salir',key='-EXIT-',size=(30,1))]
    ]

    window = sg.Window('',layout,font=('Bahnschrift SemiLight',16),element_justification='center',no_titlebar=True,grab_anywhere=True)
    return window
