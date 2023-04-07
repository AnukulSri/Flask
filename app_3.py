from flask import Flask,redirect,url_for # redirect is used to get from one page to another, url_for is used to store the url of specific page
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the first page of the Flask.....'

# creating a program in which it checks that the student is pass or fail & then then it will be redirected to the specific page

@app.route('/success/<int:score>') # creating a success page
def success(score):
    return "The student is Passed and scored : " + str(score)

@app.route('/fail/<int:score>') # creating a fail page
def fail(score):
    return 'The student is failed and scored : '+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = ""

    if marks<35:
        result ='fail' # here we have to store same name as the function to redirect
    else:
        result ='success'
    return redirect(url_for(result,score=marks))

if __name__ =='__main__':
    app.run(debug=True)