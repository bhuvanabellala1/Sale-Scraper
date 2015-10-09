from flask import Flask
from jcrew import findSales
app = Flask(__name__)

@app.route('/')
def hello_world():
    promoText, details = findSales("https://www.jcrew.com/index.jsp")
    return promoText

if __name__ == '__main__':
    app.run()
