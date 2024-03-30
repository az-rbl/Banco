from flask import Blueprint, redirect, url_for

from .extensions import db
from .models import Account
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    accounts = Account.query.all()
    account_list_html = [f"<li>{ account.balance }</li>" for account in accounts]
    return f"<ul>{''.join(account_list_html)}</ul>"

@main.route('/add/<username>')
def add_user(username):
    db.session.add(User(username=username))
    db.session.commit()
    return redirect(url_for("main.index"))