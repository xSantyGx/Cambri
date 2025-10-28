from flask import Flask, render_template, request, redirect, url_for, jsonify
from pedidos_data import pedidos, next_id

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

# === READ ===
@app.route('/pedidos')
def pedidos_view():
    return render_template('pedidos.html', pedidos=pedidos)

# === CREATE ===
@app.route('/pedidos/crear', methods=['POST'])
def crear_pedido():
    nuevo_pedido = {
        "id": next_id(),
        "cliente": request.form['cliente'],
        "estado": request.form['estado'],
        "contacto": request.form['contacto'],
        "fecha": request.form['fecha'],
        "costo": float(request.form['costo']),
        "descripcion": request.form['descripcion']
    }
    pedidos.append(nuevo_pedido)
    return redirect(url_for('pedidos_view'))

# === UPDATE ===
@app.route('/pedidos/actualizar/<int:id>', methods=['POST'])
def actualizar_pedido(id):
    nuevo_estado = request.json.get('estado')
    for p in pedidos:
        if p['id'] == id:
            p['estado'] = nuevo_estado
            break
    return jsonify({"mensaje": f"Pedido {id} actualizado a {nuevo_estado}"})

# === DELETE ===
@app.route('/pedidos/eliminar/<int:id>', methods=['POST'])
def eliminar_pedido(id):
    global pedidos
    pedidos = [p for p in pedidos if p['id'] != id]
    return redirect(url_for('pedidos_view'))


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
