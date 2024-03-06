from flask import Flask, request, jsonify
from transferencia_DB import connect, deposit, withdraw, add_account, transfer
import os

app = Flask(__name__)

def get_db_connection():
    try:
        connection = connect(
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            host=os.environ.get('DB_HOST'),
            port=os.environ.get('DB_PORT'),
            database=os.environ.get('DB_NAME')
        )
        return connection
    except Exception as e:
        print("Error connecting to database:", e)
        return None

@app.route('/deposito', methods=['POST'])
def deposito():
    data = request.get_json()
    no_cuenta = data.get('no_cuenta')
    cantidad = data.get('cantidad')
    connection = get_db_connection()
    if connection:
        deposit(connection, no_cuenta, cantidad)
        connection.close()
        return jsonify({"message": "Deposited successfully"}), 200
    else:
        return jsonify({"message": "Error connecting to database"}), 500

@app.route('/retiro', methods=['POST'])
def retiro():
    data = request.get_json()
    no_cuenta = data.get('no_cuenta')
    cantidad = data.get('cantidad')
    connection = get_db_connection()
    if connection:
        withdraw(connection, no_cuenta, cantidad)
        connection.close()
        return jsonify({"message": "Withdrawn successfully"}), 200
    else:
        return jsonify({"message": "Error connecting to database"}), 500

@app.route('/transferencia', methods=['POST'])
def transferencia():
    data = request.get_json()
    no_cuenta = data.get('no_cuenta')
    cantidad = data.get('cantidad')
    destino = data.get('destino')
    connection = get_db_connection()
    if connection:
        transfer(connection, no_cuenta, destino, cantidad)
        connection.close()
        return jsonify({"message": "Transferred successfully"}), 200
    else:
        return jsonify({"message": "Error connecting to database"}), 500

@app.route('/nueva_cuenta', methods=['POST'])
def nueva_cuenta():
    data = request.get_json()
    cantidad = data.get('cantidad')
    connection = get_db_connection()
    if connection:
        add_account(connection, cantidad)
        connection.close()
        return jsonify({"message": "Account created successfully"}), 200
    else:
        return jsonify({"message": "Error connecting to database"}), 500

if __name__ == '__main__':
    app.run(debug=True)
