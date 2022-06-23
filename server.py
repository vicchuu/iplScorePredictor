from flask import Flask , url_for,redirect ,render_template,request
app= Flask(__name__)

"""
JINJA technique {%.....%} for statements
{{ }}expression to print
{# ...} internel comments
"""


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/fail/<int:score>')
def fail(score):
    return "I'm failed with this mark  :"+str(score)

@app.route('/succcess/<int:score>')
def succcess(score):
    #print("method in success ....!")
    return "I'm passed with the mark i got is   :"+str(score)

@app.route('/checkResult/<int:marks>')
def checkResult(marks):
    #print("scheck result :",marks)
    result = ""
    if marks>50:
         result="succcess"
    else:
         result="fail"
    return redirect(url_for(result,score =marks))

@app.route("/submit",methods=["POST","GET"])
def submit():
    answer=1
    print(request.method)
    if request.method =="POST":
        science = float(request.form["science"])
        social = float(request.form["social"])
        maths = float(request.form["maths"])
        philosophy = float(request.form["philosophy"])

        answer =  (science+social+maths+philosophy)/4
        result= ""
        if answer>50:
            result = "succcess"
        else:
            result = "fail"
        dic ={"result":result,"marks":answer}
    return render_template("resultPub.html", score=dic)




if __name__ =="__main__":
    app.run(debug = True)