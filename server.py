from flask import Flask ,render_template , url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]=("sqlite:///testSQL.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route("/" , methods=['GET','POST'])
def imdex():
    return   render_template("index.html")

#pip install -U Flask-SQLAlchemy pip install Flask-SQLAlchemy
if __name__ =="__main__":

    app.run(debug=True)