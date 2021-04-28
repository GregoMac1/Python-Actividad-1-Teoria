import PySimpleGUI as sg
sg.theme('DefaultNoMoreNagging')

def build():
    layout = [
        [sg.Text('¿Qué datos analizamos?',justification='center')],
        [sg.Button('Series de Netflix',key=('-OPTION_ONE-'),size=(30,1))],
        [sg.Button('Vacunas COVID',key=('-OPTION_TWO-'),size=(30,1))], [sg.Text('',size=(1,1))],
        [sg.Button('Salir',key='-EXIT-',size=(30,1))]
    ]

    window = sg.Window('',layout,font=('Bahnschrift SemiLight',16),element_justification='center',no_titlebar=True,grab_anywhere=True)
    return window
