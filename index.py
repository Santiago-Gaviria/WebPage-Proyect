from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
@app.route('/lenguajes')
def lenguaje():
    lenguajes_programacion=("php","python","java","C#","Javascript","perl",
    "ruby","rust")
    return render_template('/lenguajes.html', lenguajes=lenguajes_programacion)
if __name__ == '__main__':
    app.run(debug=True,port=5017)
