from flask import Flask, render_template
from jcrew import findSales
app = Flask(__name__)

#Error checking has not been implemented yet
@app.route('/')
def home_page():

    #Error checking is not done
    promoText, details = findSales("jcrew", "https://www.jcrew.com/index.jsp")

    if promoText:
        return render_template("index.html", promoText = promoText)
    else:
        return "Failed"

if __name__ == '__main__':
    app.run()
