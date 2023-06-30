<h1 align="center">🔒 Secure Password Manager</h1>

A Python application to securely store and manage passwords.  
  
🔒 This app saves passwords using encryption, and they can be decrypted only with the correct encryption key. The encryption key is automatically generated during the first use of the app.

## Usage
To run the password manager app, execute startup.py. On the first run, you will be prompted to set a master password. This master password will be required to access all the saved passwords, so make sure to remember it.

Once the master password is set, the main page will be displayed, offering the following options:

- **💾 Save Passwords**: You can save passwords by entering the website, username, and password details.

- **🔍 See Saved Passwords**: You can view the saved passwords. They will be decrypted using the master password.

- **🔑 Generate Random and Secure Passwords**: You can generate random and secure passwords for your accounts.

To stop the app, you can use the system tray icon (Windows) by right-clicking it. Two options will be available:

- **▶️ Start**: It will start the app and open the main page.

- **⏹️ Stop**: It will stop the app, but the system tray icon will still be visible.

## Dependencies
The project has the following dependencies:

1. **Flask**: A web framework for building Python applications.
2. **Pystray**: A library for creating system tray icons and menus.
3. **Cryptography**: A library for secure encryption and decryption operations.

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
````


## Disclaimer
Please note that while this password manager app aims to provide enhanced security, no system can guarantee absolute security. Always exercise caution when handling sensitive information and regularly update your passwords. The developer(s) of this app are not responsible for any misuse or loss of data.
