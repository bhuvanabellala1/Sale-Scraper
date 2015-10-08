from flask import Flask
from jcrew import findSales
app = Flask(__name__)

@app.route('/')
def hello_world():
    findSales("https://www.jcrew.com/index.jsp")
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
