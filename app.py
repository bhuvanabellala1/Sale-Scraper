
import json
import flask
from flask import Flask, jsonify, Response, request
from jcrew import findSales

app = Flask(__name__)

#Error checking has not been implemented yet
@app.route('/')
def home_page():

    return flask.render_template('index.html')

@app.route('/deals', methods=['GET', 'POST'])
def get_deals():

    print "fsfsd"
    promoText, details = findSales("jcrew", "https://www.jcrew.com/index.jsp")
    return jsonify(jcrew=promoText, myRes="hedslo",)

if __name__ == '__main__':
    app.run()
