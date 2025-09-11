from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def aboutme():
    return render_template('aboutme.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    lenguajes_programacion = (
        "php", "python", "java", "C#", "Javascript", "perl", "ruby", "rust"
    )
    return render_template('portfolio.html', lenguajes=lenguajes_programacion)
@app.route('/sg.html')
def santiagog():
    return render_template('sg.html')

if __name__ == '__main__':
    app.run(debug=True, port=5017)

