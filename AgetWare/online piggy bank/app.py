from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
app.config['SECRET_KEY'] = '12345JSPK67890'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    transactions = db.relationship('Transaction', backref='user', lazy=True)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    if User.query.filter_by(username=username).first():
        flash('Username already exists.')
        return redirect(url_for('index'))
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    flash('User created successfully.')
    return redirect(url_for('index'))

@app.route('/deposit', methods=['POST'])
def deposit():
    username = request.form['username']
    amount = request.form['amount']
    user = User.query.filter_by(username=username).first()
    if user:
        new_transaction = Transaction(amount=amount, user_id=user.id)
        db.session.add(new_transaction)
        db.session.commit()
        flash('Deposit successful.')
    else:
        flash('User not found.')
    return redirect(url_for('index'))

@app.route('/transactions', methods=['POST'])
def transactions():
    username = request.form['username']
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template('transactions.html', transactions=user.transactions, username=username)
    else:
        flash('User not found.')
        return redirect(url_for('index'))

@app.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form['username']
    user = User.query.filter_by(username=username).first()
    if user:
        transactions = user.transactions
        total_amount = sum(transaction.amount for transaction in transactions)
        db.session.delete(user)
        deleted = Transaction.query.filter(Transaction.user_id == None).delete()
        del deleted
        db.session.commit()
        return render_template('deleted_transactions.html', transactions=transactions, username=username, total_amount=total_amount)
    else:
        flash('User not found.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
