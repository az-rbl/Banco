from flask import Flask, render_template, request, flash, redirect, url_for
import sys
from form import MyForm
from transferencia import cuenta

cuentas={123:cuenta(123, 1000),124:cuenta(124, 100), 125:cuenta(125, 100)}

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for CSRF protection

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     form = MyForm()
#     if form.validate_on_submit():
#         # Process valid form data (e.g., save to database)
#         flash('Registration Successful!')
#         return redirect(url_for('form'))
#     return render_template('form.html', form=form)



@app.route("/",methods=['GET', 'POST'])
def index():
    global cuentas
    if request.method == 'POST':
        if request.form['transactionType']=='deposito':
            cuentas[123].deposito(int(request.form['cantidad'])) 
        elif request.form['transactionType']=='retiro':
            cuentas[123].retiro(int(request.form['cantidad']))
        elif request.form['transactionType']=='transferencia':
            cuentas[123].transferencia(cuentas[int(request.form['destino'])], int(request.form['cantidad']))
            
    return render_template('index.html', saldo = cuentas[123].saldo)

    

if __name__ == '__main__':
    app.run(debug=True)
