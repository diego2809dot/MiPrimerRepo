from flask import Flask

app = Flask(__name__)

# Ruta simple
@app.route('/')
def home():
    return 'Hola Mundo, FLASK!'

# Ruta con parámetro
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f'Hola {nombre}!!!'

# Ruta try-catch
@app.errorhandler(404)
def paginaNoE(error):
    return 'Cuidado: Error 404, Ruta no encontrada', 404

# Ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'Yo soy el mismo recurso del servidor'

# Ruta POST
@app.route('/post', methods=['POST'])
def formulario():
    return 'Soy un Formulario'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
