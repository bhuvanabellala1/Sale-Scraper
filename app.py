import json
import flask
from flask import Flask, jsonify, Response, request
from jcrew import findSales

app = Flask(__name__)

@app.route('/')
def home_page():
    return flask.render_template('index.html')

@app.route('/deals', methods=['GET', 'POST'])
def get_deals():
    return jsonify(jcrew="30% off", myRes="hedslo",)


if __name__ == '__main__':
    app.run()
