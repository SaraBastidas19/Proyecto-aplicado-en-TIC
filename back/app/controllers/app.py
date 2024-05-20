from flask import Flask, render_template, request
from back.app.services.inder_service import InderService

app = Flask(__name__, template_folder='')

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_login():
    result = InderService().login(request.form)
    if isinstance(result, str):
        return render_template('index.html', error_message = result)
    if result['rol'] == 'estudiante':
        return render_template('inicio.html')


# MARI
@app.route('/user', methods=['POST'])
def user():
    return InderService().create_usuario(request.form)



if __name__ == "__main__":
    app.run(debug=True)





