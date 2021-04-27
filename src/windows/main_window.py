import PySimpleGUI as sg

def build():
    layout = [
        [sg.Text('¿Qué datos analizamos?',justification='center')],
        [sg.Button('Series de Netflix',key=('-OPTION_ONE-'),size=(30,1))],
        [sg.Button('Vacunas COVID',key=('-OPTION_TWO-'),size=(30,1))], [sg.Text('',size=(1,1))],
        [sg.Button('Salir',key='-EXIT-',size=(30,1))]
    ]

    window = sg.Window(f'Actividad 1 de Teoría',layout,font=('Arial',16),element_justification='center')
    return window
