import PySimpleGUI as sg
from src.windows import main_window
from src.handlers import dataset_one
from src import constants

def start():
    window = main_window.build()
    while True:
        event, values = window.read()

        if event in ('Salir','-EXIT-'):
            break

        if event == '-OPTION_ONE-':
            dataset_one.start(constants.first)
            sg.popup('Archivo JSON generado exitosamente.',title='Éxito',font=('Bahnschrift SemiLight',16))
        '''elif event == '-OPTION_TWO-':
            dataset_two.start(constants.second)
            sg.popup('Archivo JSON generado exitosamente.',title='Éxito',font=('Bahnschrift SemiLight',16))'''

    window.close()
