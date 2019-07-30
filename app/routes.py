from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('risk.html', title='RiskFDA')

@app.route('/recalls')
def recalls():
    return render_template('recalls.html', title='RiskFDA')

@app.route('/advevents')
def advevents():
    return render_template('adverse-events.html', title='RiskFDA')

@app.route('/faq')
def faq():
    return render_template('faq.html', title='RiskFDA')