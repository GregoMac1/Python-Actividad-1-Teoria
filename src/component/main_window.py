import PySimpleGUI as sg
from src.windows import main_window
from src.handlers import process_dataset
from src import constants

def start():
    window = main_window.build()
    while True:
        event, _values = window.read()

        if event in ('Salir','-EXIT-'):
            break

        if event == '-OPTION_ONE-':
            process_dataset.start(constants.first,constants.function_one)
            sg.popup('Archivo JSON generado exitosamente.',title='Éxito',font=('Bahnschrift SemiLight',16))
        elif event == '-OPTION_TWO-':
            process_dataset.start(constants.second,constants.function_two)
            sg.popup('Archivo JSON generado exitosamente.',title='Éxito',font=('Bahnschrift SemiLight',16))

    window.close()
