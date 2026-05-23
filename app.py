from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json

    order = {
        "id": len(orders) + 1,
        "cliente": data["cliente"],
        "produto": data["produto"],
        "quantidade": data["quantidade"]
    }

    orders.append(order)

    return jsonify(order), 201

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    for order in orders:
        if order["id"] == id:
            return jsonify(order)

    return jsonify({"erro": "Pedido não encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
