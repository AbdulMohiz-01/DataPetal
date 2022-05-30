from datetime import date
from re import M
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app);

class MyAttributes(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Integer, nullable = False)
    phoneNo = db.Column(db.Integer, nullable = False)
    cnic = db.Column(db.Integer, nullable = False)
    forAccused = db.Column(db.String(100), nullable = False)
    caseDesc = db.Column(db.String(300), nullable = False)
    dateOfAttestation = db.Column(db.String(25), nullable = False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name} - {self.phoneNo} -{self.cnic}  - {self.forAccused} - {self.caseDesc} - {self.dateOfAttestation}"
    

@app.route('/',methods = ['GET', 'POST'])
def home():
    if request.method=='POST':
        name = request.form['name']
        phoneNo = request.form['phoneNo']
        cnic = request.form['cnic']
        forAccused = request.form['forAccused']
        caseDesc = request.form['caseDesc']
        dateOfAttestation = request.form['dateOfAttestation']
        data = MyAttributes(name = name + " S/O dono types ka namea mai", phoneNo = phoneNo, cnic = cnic, forAccused = forAccused+" S/O dono types ka namea mai", caseDesc = caseDesc, dateOfAttestation = dateOfAttestation)
        db.session.add(data)
        db.session.commit()

    alldata = MyAttributes.query.all()
    return render_template("index.html",alldata = alldata)

@app.route('/update/<int:sno>',methods = ['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        name = request.form['name']
        phoneNo = request.form['phoneNo']
        cnic = request.form['cnic']
        forAccused = request.form['forAccused']
        caseDesc = request.form['caseDesc']
        dateOfAttestation = request.form['dateOfAttestation']
        data = MyAttributes.query.filter_by(sno = sno).first()
        data.name = name
        data.phoneNo = phoneNo
        data.cnic = cnic
        data.forAccused = forAccused
        data.caseDesc = caseDesc
        data.dateOfAttestation = dateOfAttestation
        db.session.add(data)
        db.session.commit()
        return redirect('/')

    data = MyAttributes.query.filter_by(sno = sno).first()
    return render_template("update.html", data = data)

@app.route('/delete/<int:sno>')
def delete(sno):
    data = MyAttributes.query.filter_by(sno = sno).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)