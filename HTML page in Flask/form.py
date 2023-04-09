from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('form.html')


@app.route('/success/<int:score>')
def success(score):
    return 'The student is passed'+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The student is failed'+ str(score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score =(science+maths+c+data_science)/4
    return redirect(url_for('results',marks=total_score))

@app.route('/results/<int:marks>')
def results(marks):
    res = ''
    if marks>35:
        res ='success'
    else:
        res = 'fail'
    return redirect(url_for(res,score=marks))
if __name__ =='__main__':
    app.run(debug=True)