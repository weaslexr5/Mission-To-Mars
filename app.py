
import pymongo
import scrape_mars
from flask import Flask, render_template, redirect

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.marsdataDB
collection = db.marsdata

marsdata = list(db.marsdata.find())
# print(marsdata)


@app.route('/')
def index():
    #marsdata = list(db.marsdata.find())
    return render_template('index.html', marsdata=marsdata)


@app.route('/scrape')
def scrape():
    marsdata = scrape_mars.scrape()
    db.marsdata.update(
        {},
        marsdata,
        upsert=True
    )
    return redirect('http://localhost:5000/', code=302)

if __name__ == '__main__':
    app.run(debug=True)