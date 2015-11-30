
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

    deals = []
    promoText, details = findSales("jcrew", "https://www.jcrew.com/index.jsp")
    deals.append({'company': 'jcrew', 'image': 'static/jcrew.png', 'promo' : promoText, 'details': details})
    deals.append({'company': 'jcrew', 'image': 'static/jcrew.png', 'promo' : promoText, 'details': details})
   # deals.append({'company': 'jcrew', 'image': 'static/jcrew.png', 'promo' : promoText, 'details': details})
    #deals.append({'company': 'jcrew', 'image': 'static/jcrew.png', 'promo' : promoText, 'details': details})
    #deals.append({'company': 'jcrew', 'image': 'static/jcrew.png', 'promo' : promoText, 'details': details})
    #deals.append({'company': 'jcrew', 'image': 'static/jcrew.png', 'promo' : promoText, 'details': details})

    print "here"

    return Response(json.dumps(deals), mimetype='application/json', headers={'Cache-Control': 'no-cache'})

if __name__ == '__main__':
    app.run()
