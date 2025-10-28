from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/volver')
def volver():
    return redirect(url_for('index'))

@app.route("/produccion")
def produccion():
    return render_template("produccion.html")

@app.route("/inventario")
def inventario():
    return render_template("inventario.html")

@app.route("/reportes")
def reportes():
    return render_template("reportes.html")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
