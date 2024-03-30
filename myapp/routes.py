from flask import Blueprint, redirect, url_for, request

from .extensions import db
from .models import Accounts
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    accounts = Accounts.query.all()
    account_list_html = [f"<li>{ account.balance }</li>" for account in accounts]
    return f"<ul>{''.join(account_list_html)}</ul>"


@main.route('/new_account', methods=['POST'])
def new_account():
    data = request.get_json()
    amount = data.get('amount')
    db.session.add(Accounts(balance=amount))
    db.session.commit()
    return redirect(url_for("main.index"))




@main.route('/add/<username>')
def add_user(username):
    db.session.add(User(username=username))
    db.session.commit()
    return redirect(url_for("main.index"))