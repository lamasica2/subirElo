from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

def pulsar(tecla):
    keyboard.press(tecla)
    keyboard.release(tecla)

while(True):
    time.sleep(90)
    pulsar(Key.enter)
    pulsar('g')
    pulsar('j')
    pulsar(Key.enter)
