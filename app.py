from flask import Flask
from jcrew import findSales
app = Flask(__name__)

@app.route('/')
def home_page():
    promoText, details = findSales("https://www.jcrew.co/index.jsp")
    print "here"
    if promoText:
        return promoText
    else:
        return "Failed"

if __name__ == '__main__':
    app.run()
