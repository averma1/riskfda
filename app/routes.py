from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('welcome.html', title='RiskFDA', tabisactive='activetab')

@app.route('/recalls')
def recalls():
    return render_template('recalls.html', title='RiskFDA', tabisactive='activetab')

@app.route('/advevents')
def advevents():
    return render_template('adverse-events.html', title='RiskFDA', tabisactive='activetab')

@app.route('/faq')
def faq():
    return render_template('faq.html', title='RiskFDA', tabisactive='activetab')

@app.route('/risk')
def risk():
    return render_template('risk.html', title='RiskFDA', tabisactive='activetab')