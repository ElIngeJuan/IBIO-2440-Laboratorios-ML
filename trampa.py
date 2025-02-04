from pynput.keyboard import Controller, Listener, Key
import time

keyboard = Controller()

# Variable para controlar la activación
enable_script = False

def on_press(key):
    global enable_script
    if key == Key.ctrl_l:
        enable_script = not enable_script
        if enable_script:
            print("Script activado. Presionando 'X' cada 3 segundos.")
        else:
            print("Script detenido.")

print("Presiona Ctrl + I para activar/desactivar el script.")

def run_script():
    global enable_script
    while True:
        if enable_script:
            keyboard.press('x')  # Presiona 'X'
            time.sleep(0.1)
            keyboard.release('x')  # Suelta 'X'
            time.sleep(3)  # Espera 3 segundos
        else:
            time.sleep(0.1)  # Pequeña espera para evitar consumo excesivo de CPU

# Iniciar listener para capturar Ctrl + I
with Listener(on_press=on_press) as listener:
    run_script()
    listener.join()