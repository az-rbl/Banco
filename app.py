from flask import Flask, request, jsonify
from transferencia import cuenta, realizar_deposito, realizar_retiro, realizar_transferencia

cuentas={"C123":cuenta("C123", 1000),"C124":cuenta("C124", 100), "C125":cuenta("C125", 100)}

app = Flask(__name__)
@app.route('/deposito', methods=['POST'])
def deposito():
    data = request.get_json()
    no_cuenta = data.get('no_cuenta')
    cantidad = data.get('cantidad')

    if no_cuenta in cuentas and cantidad > 0:
        realizar_deposito(cuentas[no_cuenta], cantidad)
        return jsonify({"message": "Deposito exitoso", "balance": cuentas[no_cuenta].saldo}), 200
    else:
        return jsonify({"message": "Error"}), 400

@app.route('/retiro', methods=['POST'])
def retiro():
    data = request.get_json()
    no_cuenta = data.get('no_cuenta')
    cantidad = data.get('cantidad')

    if no_cuenta in cuentas and cantidad <= cuentas[no_cuenta].saldo:
        realizar_retiro(cuentas[no_cuenta], cantidad)
        return jsonify({"message": "Retiro exitoso", "balance": cuentas[no_cuenta].saldo}), 200
    else:
        return jsonify({"message": "Error"}), 400
    
@app.route('/transferencia', methods=['POST'])
def transferencia():
    data = request.get_json()
    no_cuenta = data.get('no_cuenta')
    cantidad = data.get('cantidad')
    destino = data.get('destino')

    if no_cuenta in cuentas and cantidad <= cuentas[no_cuenta].saldo and destino in cuentas:
        realizar_transferencia(cuentas[no_cuenta], cuentas[destino], cantidad)
        return jsonify({"message": "transferencia exitosa", "balance": cuentas[no_cuenta].saldo}), 200
    else:
        return jsonify({"message": "Error"}), 400
    
if __name__ == '__main__':
    app.run(debug =True )
    