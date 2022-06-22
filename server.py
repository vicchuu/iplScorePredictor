from flask import Flask , url_for,redirect ,render_template
app= Flask(__name__)

@app.route("/")
def home():
    return "home method calls"

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



if __name__ =="__main__":
    app.run(debug = True)