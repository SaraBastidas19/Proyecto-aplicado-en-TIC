from flask import Flask, render_template, request

app = Flask(__name__, template_folder='')

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['usuario']
    password = request.form['contraseña']
    # Aquí puedes agregar la lógica de autenticación
    return f"Usuario: {username}, Contraseña: {password}"

if __name__ == "__main__":
    app.run(debug=True)
