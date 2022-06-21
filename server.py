from flask import Flask ,render_template

app = Flask(__name__)


@app.route("/")
def hello():
    my_html = '''

     <body style="background-color: #e1eb34;">


         <h1 style="color:(0,255,0);">Hello World</h1>

     </body>

     '''
    return my_html

@app.route("/meera")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
