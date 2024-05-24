from flask import Flask, render_template, request
from backend.app.services.inder_service import InderService    

app = Flask(__name__, template_folder='../../../frontend/templates', static_folder='../../../frontend/assets', static_url_path="/frontend/assets")


@app.route('/')
def login():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_login():
    result = InderService().login(dict(request.form))
    if isinstance(result, str):
        return render_template('index.html', error_message = result)
    if result['rol'] == 'estudiante':
        return render_template('inicio.html')

@app.route('/user', methods=['POST'])
def user():
    response = InderService().create_usuario(dict(request.form))
    return render_template('registro.html', response=response)

@app.route('/registration')
def registration():
    return render_template('registro.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/courses/basketball')
def courses_basketball():
    return render_template('course-baloncesto.html')

@app.route('/courses/swimming')
def courses_swimming():
    return render_template('course-natacion.html')

@app.route('/courses/soccer')
def courses_soccer():
    return render_template('course-futbol.html')

@app.route('/attendance')
def attendance():
    return render_template('pricing.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/trainers')
def trainers():
    return render_template('trainers.html')

@app.route('/enrollment')
def enrollment():
    return render_template('inscribirse.html')

@app.route('/student-home')
def student_home():
    return render_template('inicio.html')

@app.route('/create-enrollment', methods=["POST"])
def create_enrollment():
    response = InderService().create_matricula(dict(request.form))
    return render_template("inscribirse.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)





