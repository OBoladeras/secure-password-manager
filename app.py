from flask import Flask, render_template, request
from password_manager import save_password, retrieve_password, generate_password

app = Flask(__name__)
password_file = 'data.txt'


@app.route('/')
def index():
    data = []

    try:
        with open(password_file, 'r') as f:
            for line in f.readlines():
                save = {}
                save['web'] = line.split(',')[0]
                save['username'] = line.split(',')[1]

                data.append(save)
    except:
        with open(password_file, 'w') as f:
            f.write('')

    return render_template('index.html', data=data)


@app.route('/', methods=['GET', 'POST'])
def index_post():
    requestMade = request.form.get("form_name")

    if requestMade == 'save':
        web = request.form['web']
        username = request.form['username']
        password = request.form['password']

        save_password(web, username, password)
        return 'password saved'

    elif requestMade == 'other':
        web_username = request.form['show_password']
        web, username = web_username.split('-')

        password = retrieve_password(web, username)
        return render_template('serve.html', password=password)

    elif requestMade == 'generate_password':
        with open(password_file, 'r') as f:
            data = []

            for line in f.readlines():
                save = {}
                save['web'] = line.split(',')[0]
                save['username'] = line.split(',')[1]

                data.append(save)

        return render_template('index.html', data=data, password=generate_password())


if __name__ == '__main__':
    port = 18824
    app.run(port=port)
