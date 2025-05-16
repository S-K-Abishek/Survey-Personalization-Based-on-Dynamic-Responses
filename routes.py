from flask import Flask, render_template, request, redirect, url_for
from models import db, Response

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        answer = request.form.get('q1')
        new_response = Response(q1=answer)
        db.session.add(new_response)
        db.session.commit()

        if new_response.q1 == 'Yes':
            return redirect(url_for('question2', response_id=new_response.id))
        else:
            return redirect(url_for('conclusion', response_id=new_response.id))
    return render_template('question1.html')

@app.route('/question2/<int:response_id>', methods=['GET', 'POST'])
def question2(response_id):
    if request.method == 'POST':
        answer = request.form.get('q2')
        response = Response.query.get(response_id)
        response.q2 = int(answer)
        db.session.commit()
        if response.q2 <3 :
            return redirect(url_for('question3', response_id=response_id))
        else:
            return redirect(url_for('question4', response_id=response_id))
    return render_template('question2.html')

@app.route('/question3/<int:response_id>', methods=['GET', 'POST'])
def question3(response_id):
    if request.method == 'POST':
        answer = request.form.get('q3')
        response = Response.query.get(response_id)
        response.q3 = answer
        db.session.commit()
        return redirect(url_for('question4', response_id=response_id))
    return render_template('question3.html')

@app.route('/question4/<int:response_id>', methods=['GET', 'POST'])
def question4(response_id):
    if request.method == 'POST':
        answer = request.form.get('q4')
        response = Response.query.get(response_id)
        response.q4 = answer
        db.session.commit()
        if response.q4 == 'Yes':
            return redirect(url_for('question5', response_id=response_id))
        else:
            return redirect(url_for('conclusion', response_id=response_id))
        return redirect(url_for('question5', response_id=response_id))
    return render_template('question4.html')

@app.route('/question5/<int:response_id>', methods=['GET', 'POST'])
def question5(response_id):
    if request.method == 'POST':
        answer = request.form.get('q5')
        response = Response.query.get(response_id)
        response.q5 = answer
        db.session.commit()
        return redirect(url_for('question6', response_id=response_id))
    return render_template('question5.html')

@app.route('/question6/<int:response_id>', methods=['GET', 'POST'])
def question6(response_id):
    if request.method == 'POST':
        answer = request.form.get('q6')
        response = Response.query.get(response_id)
        response.q6 = answer
        db.session.commit()
        return redirect(url_for('question7', response_id=response_id))
    return render_template('question6.html')

@app.route('/question7/<int:response_id>', methods=['GET', 'POST'])
def question7(response_id):
    if request.method == 'POST':
        answer = request.form.get('q7')
        response = Response.query.get(response_id)
        response.q7 = answer
        db.session.commit()
        return redirect(url_for('question8', response_id=response_id))
    return render_template('question7.html')

@app.route('/question8/<int:response_id>', methods=['GET', 'POST'])
def question8(response_id):
    if request.method == 'POST':
        answer = request.form.get('q8')
        response = Response.query.get(response_id)
        response.q8 = answer
        db.session.commit()
        return redirect(url_for('question9', response_id=response_id))
    return render_template('question8.html')

@app.route('/question9/<int:response_id>', methods=['GET', 'POST'])
def question9(response_id):
    if request.method == 'POST':
        answer = request.form.get('q9')
        response = Response.query.get(response_id)
        response.q9 = answer
        db.session.commit()
        return redirect(url_for('question10', response_id=response_id))
    return render_template('question9.html')

@app.route('/question10/<int:response_id>', methods=['GET', 'POST'])
def question10(response_id):
    if request.method == 'POST':
        answer = request.form.get('q10')
        response = Response.query.get(response_id)
        response.q10 = answer
        db.session.commit()
        return redirect(url_for('conclusion', response_id=response_id))
    return render_template('question10.html')

@app.route('/conclusion/<int:response_id>', methods=['GET', 'POST'])
def conclusion(response_id):
    if request.method == 'POST':
        comments = request.form.get('comments')
        response = Response.query.get(response_id)
        response.comments = comments
        db.session.commit()
        return redirect(url_for('thank_you'))
    return render_template('conclusion.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/admin')
def admin():
    responses = Response.query.all()
    return render_template('admin.html', responses=responses)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
