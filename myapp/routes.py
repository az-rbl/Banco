from flask import Blueprint, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin
from .extensions import db
from .models import Accounts
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    accounts = Accounts.query.all()
    account_list_html = [f"<li>{account.account_id}:      { account.balance }</li>" for account in accounts]
    return f"<ul>{''.join(account_list_html)}</ul>"


@main.route('/new_account', methods=['POST'])
@cross_origin()
def new_account():
    data = request.get_json()
    amount = data.get('amount')
    db.session.add(Accounts(balance=amount))
    db.session.commit()
    return jsonify({"message": "Account created successfully"}), 200

@main.route('/accounts', methods=['GET'])
@cross_origin()
def get_accounts():
    accounts = Accounts.query.all()
    resultado = []
    for account in accounts:
        account_datos ={'account_id': account.account_id, 'estado': account.balance}
        resultado.append(account_datos)
    return jsonify(resultado)

@main.route('/deposit/<int:account_id>', methods=['POST'])
@cross_origin()
def deposit(account_id):
    data = request.get_json()
    account = Accounts.query.get(account_id)
    amount = int(data.get('amount'))
    if account:
        account.balance += amount
        db.session.commit()
        return jsonify({"message": f"Deposited {amount} into account {account_id}"}), 200
    else:
        return jsonify({"error": "Account not found"}), 404
    
@main.route('/withdraw/<int:account_id>', methods=['POST'])
@cross_origin()
def withdraw(account_id):
    data = request.get_json()
    account = Accounts.query.get(account_id)
    amount = int(data.get('amount'))
    if account:
        if account.balance >= amount:
            account.balance -= amount
            db.session.commit()
            return jsonify({"message": f"Withdrew {amount} from account {account_id}"}), 200
        else:
            return jsonify({"error": "Insufficient balance"}), 400
    else:
        return jsonify({"error": "Account not found"}), 404
    
@main.route('/transfer/<int:account_id>', methods=['POST'])
@cross_origin()
def transfer(account_id):
    data = request.get_json()
    destination_account = Accounts.query.get(account_id)
    amount = int(data.get('amount'))
    origin_account_id = data.get('account_id')
    if destination_account:
        withdraw(origin_account_id)
        deposit(account_id)
        return jsonify({"message": f"Transfered {amount} from account {origin_account_id} to account {account_id}"}), 200
    else:
        return jsonify({"error": "Account not found"}), 404


@main.route('/add/<username>')
def add_user(username):
    db.session.add(User(username=username))
    db.session.commit()
    return redirect(url_for("main.index"))