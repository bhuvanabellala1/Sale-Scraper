
import json
import flask
from flask import Flask, Response
from sales import findSales

app = Flask(__name__)

#Error checking has not been implemented yet
@app.route('/')
def home_page():

    return flask.render_template('index.html')

@app.route('/deals', methods=['GET', 'POST'])
def get_deals():
    """Returns all the deals as a json object"""

    deals = []
    promoText, details = findSales("jcrew", "https://www.jcrew.com/index.jsp")
    deals.append({'company': 'jcrew', 'image': 'static/jcrew.png', 'promo' : promoText, 'details': details})
    promoText, details = findSales("nyc", "http://www.nyandcompany.com/nyco/")
    deals.append({'company': 'nyc', 'image': 'static/nyc.png', 'promo' : promoText, 'details': details})
    promoText, details = findSales("vra", "http://www.verabradley.com/")
    deals.append({'company': 'vra', 'image': 'static/vra.jpg', 'promo' : promoText, 'details': details})

    return Response(json.dumps(deals), mimetype='application/json', headers={'Cache-Control': 'no-cache'})

if __name__ == '__main__':
    app.run()
