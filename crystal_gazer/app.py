from flask import Flask, redirect, render_template, request, url_for
from sklearn.metrics import auc, roc_curve

from gazer import Gazer

app = Flask(__name__)
app.debug = True
crystal_gazer = Gazer()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/healthcheck', method)
def healthcheck():
    return {
        'status': 200,
        'status_text': 'OK'
    }


@app.route('/get_prediction', method=['POST'])
def get_prediction():
    verdict = crystal_gazer.check_this_out([])
    print verdict
    return {
        'status': 200
    }
