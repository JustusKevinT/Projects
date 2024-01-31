from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking.db'
app.config['SECRET_KEY'] = '12345JSPK67890'
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    loans = db.relationship('Loan', backref='customer', lazy=True)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    loan_period = db.Column(db.Integer, nullable=False)  # In years
    interest_rate = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    interest = db.Column(db.Float, nullable=False)
    balance_amount = db.Column(db.Float, nullable=False)
    balance_period = db.Column(db.Integer, nullable=False)
    payments = db.relationship('Payment', backref='loan', lazy=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'), nullable=False)
    payment_amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/lend', methods=["POST", "GET"])
def lend():
    # Implement LEND functionality
    return render_template('lend.html')

@app.route('/lendApplication', methods=["POST", "GET"])
def lendApplication():
    customerid = int(request.form["customer_id"])
    loanamount = int(request.form["loan_amount"])
    loanperiod = int(request.form["loan_period"])
    rateofinterest = float(request.form["rate_of_interest"])
    customer = Customer.query.filter_by(id=customerid).first()
    if customer:
        interest = loanamount * (loanperiod*12) * (rateofinterest / 100)
        total_amount = interest + loanamount
        loan = Loan(customer_id=customer.id, loan_amount = loanamount, loan_period = loanperiod, interest_rate = rateofinterest / 100, interest = interest, total_amount = total_amount, balance_amount=total_amount, balance_period = int(loanperiod))
        db.session.add(loan)
        db.session.commit()
        return render_template("lendComplete.html", totalamount = total_amount, interest = interest, id = loan.id)

@app.route('/payment', methods=['POST',"GET"])
def payment():
    return render_template("payment.html")

@app.route("/payment-emi", methods=['POST',"GET"])
def payment_emi():
    emi = float(request.form["emi"])
    loanid = int(request.form["loan_id"])
    temp = Loan.query.filter_by(id=loanid).first()
    if temp:
        balanceAmount = temp.balance_amount - emi
        balancePeriod = temp.balance_period - 1
        stmt = update(Loan).where(temp.id == loanid).values(balance_amount=balanceAmount,  balance_period=balancePeriod)
        db.session.execute(stmt)
        db.session.commit()
        payment = Payment(loan_id = temp.id, payment_amount = emi,  payment_date = datetime.now())
        db.session.add(payment)
        db.session.commit()
        content = "Payment successful"
        del temp, balanceAmount, balancePeriod
        return render_template("paymentResult.html",content=content)
    else:
        content = "Payment failed"
        del temp
        return render_template("paymentResult.html",content=content)

@app.route("/payment-lump", methods=['POST',"GET"])
def payment_lump():
    lump = float(request.form["lump"])
    loanid = int(request.form["loan_id"])
    temp = Loan.query.filter_by(id=loanid).first()
    if temp:
        balanceAmount = temp.balance_amount - lump
        loanperiod = temp.interest//(temp.loan_amount * temp.interest_rate)
        balancePeriod -= loanperiod
        stmt = update(Loan).where(temp.id == loanid).values(balance_amount=balanceAmount, balance_period = balancePeriod)
        db.session.execute(stmt)
        db.session.commit()
        payment = Payment(loan_id = temp.id, payment_amount = lump,  payment_date = datetime.now())
        db.session.add(payment)
        db.session.commit()
        content = f"Payment successful. EMI is left for {loanperiod} years."
        del temp, balanceAmount, balancePeriod, loanperiod
        return render_template("paymentResult.html",content=content)
    else:
        content = "Payment failed"
        del temp
        return render_template("paymentResult.html",content=content)

@app.route('/ledger', methods=['GET',"POST"])
def ledger():
    return render_template('ledger.html')

@app.route("/check",methods=['GET',"POST"])
def check():
    loanid = int(request.form["loan_id"])
    loan = Loan.query.filter_by(id=loanid).first()
    if loan:
        payments = Payment.query.filter_by(loan_id=loanid)
        balance = loan.balance_amount
        emi = loan.interest
        balanceEMI = balance//emi
        return render_template("ledgerResult.html", payments = payments, balance = balance, emi=emi, balance_emi = balanceEMI, id = loan.id)
    else:
        return render_template("LedgerFail.html",content = "Tansactions for the given loan doesn't exist")


@app.route('/account-overview', methods=['GET',"POST"])
def account_overview():
    return render_template("overview.html")

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template('index.html')

@app.route("/show", methods=["POST","GET"])
def show():
    customerid = int(request.form["customer_id"])
    customer = Customer.query.filter_by(id=customerid).first()
    if customer:
        loans = Loan.query.filter_by(customer_id=customer.id)
        return render_template("overviewResult.html", loans = loans)


@app.route("/createAccount", methods=['POST','GET'])
def createAccount():
    username = request.form["name"]
    temp = None
    if Customer.query.filter_by(name=username).first():
        temp = Customer.query.filter_by(name=username).first()
        return render_template('index3.html', id = temp.id)
    del temp
    new_user = Customer(name=username)
    db.session.add(new_user)
    db.session.commit()
    return render_template('index2.html', id = new_user.id)

if __name__ == '__main__':
    app.run(debug=True)