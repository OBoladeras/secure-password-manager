import pystray
import subprocess
import webbrowser
from PIL import Image
import multiprocessing

script_path = "app.py"
image_path = "icon.png"
script_process = None


def start(icon, item):
    global script_process

    if script_process == None:
        script_process = subprocess.Popen(["python", script_path])

    webbrowser.open('http://127.0.0.1:18824')


def exit(icon, item):
    global script_process
    if script_process != None:
        subprocess.Popen(
            ["taskkill", "/F", "/T", "/PID", str(script_process.pid)])
        script_process = None


def create_icon():
    start(1, 1)

    image = Image.open(image_path)

    item1 = pystray.MenuItem("Iniciar", start)
    item2 = pystray.MenuItem("Salir", exit)

    menu = (item1, item2,)

    icon = pystray.Icon("password saver", image, "Passwords", menu)
    icon.run()


if __name__ == '__main__':
    icon_process = multiprocessing.Process(target=create_icon)
    icon_process.start()
