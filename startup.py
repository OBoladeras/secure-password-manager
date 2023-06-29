import hashlib
import subprocess
import tkinter as tk

contrasenya = ''


def encrypt_password(password):
    sha256 = hashlib.sha256()

    sha256.update(password.encode('utf-8'))

    hashed_password = sha256.hexdigest()

    return hashed_password


def start():
    subprocess.Popen(['python', 'icon.py'])


class PasswordPage(tk.Frame):
    def __init__(self, parent, on_password_entered):
        super().__init__(parent)
        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.submit_button = tk.Button(
            self, text="Submit", command=self.submit_password)

        self.password_label.pack()
        self.password_entry.pack()
        self.submit_button.pack()

        self.on_password_entered = on_password_entered

    def submit_password(self):
        password = self.password_entry.get()
        password = encrypt_password(password)

        try:
            with open('password.txt', 'r') as f:
                contrasenya = f.read()
        except:
            with open('password.txt', 'w') as f:
                contrasenya = password
                f.write(contrasenya)

        if password == contrasenya:
            start()
            self.on_password_entered()
        else:
            error_label = tk.Label(self, text="Incorrect password")
            error_label.pack()


class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.close_button = tk.Button(self, text="Close", command=self.close)
        self.close_button.pack()

    def close(self):
        self.master.destroy()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password App")
        self.geometry("300x200")

        self.show_password_page()

    def show_password_page(self):
        self.clear_window()
        self.password_page = PasswordPage(self, self.show_home_page)
        self.password_page.pack()

    def show_home_page(self):
        exit()
        self.clear_window()
        self.home_page = HomePage(self)
        self.home_page.pack()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()


app = App()
app.mainloop()
