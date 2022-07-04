from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class finalDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    timethis = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = finalDB(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = finalDB.query.order_by(finalDB.timethis).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    curr_id =  finalDB.query.get_or_404(id)

    try:
        db.session.delete(curr_id)
        db.session.commit()
        return redirect('/')
    except:
        return "Issue in deleteing id"


@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    task = finalDB.query.get_or_404(id)

    if request.method=='POST':
        task.content = request.form['content']

        try :
            db.session.commit()

            return redirect('/')
        except:
            return "please check the updated content ,issue is noted"
    else:
        return render_template('update.html',task=task)


if __name__ == "__main__":
    app.run(debug=True)
