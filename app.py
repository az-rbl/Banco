from flask import Flask, request, jsonify

from transferencia_DB import connect, deposit, withdraw, add_account, transfer

app = Flask(__name__)
@app.route('/deposito', methods=['POST'])
def deposito():
    data = request.get_json()
    no_cuenta = data.get('no_cuenta')
    cantidad = data.get('cantidad')
    connection = connect()
    deposit(connection, no_cuenta, cantidad)
    

@app.route('/retiro', methods=['POST'])
def retiro():
    data = request.get_json()
    no_cuenta = data.get('no_cuenta')
    cantidad = data.get('cantidad')
    connection = connect()
    
    withdraw(connection, no_cuenta, withdraw)
    
@app.route('/transferencia', methods=['POST'])
def transferencia():
    data = request.get_json()
    no_cuenta = data.get('no_cuenta')
    cantidad = data.get('cantidad')
    destino = data.get('destino')
    connection = connect()
    
    transfer(connection, no_cuenta, destino, cantidad)
    
@app.route('/nueva_cuenta', method =['POST'])
def nueva_cuenta():
    data = request.get_json()
    cantidad = data.get('cantidad')
    connection = connect()
    
    add_account(connection, cantidad)
    
if __name__ == '__main__':
    app.run(debug =True )
    