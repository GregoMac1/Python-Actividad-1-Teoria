import PySimpleGUI as sg
from src.windows import main_window

def start():
    window = main_window.build()
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED,'Salir','-EXIT-'):
            break
        
    window.close()
