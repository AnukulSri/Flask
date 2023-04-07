from flask import Flask
app = Flask(__name__)

@app.route('/')
def Welcome():
    return " Welcome to the Flask!"

@app.route('/Report/<int:score>') # int score means that we are taking score as an input to print. this destructor works as second page
def Report(score):
    return "Total marks obtained are : "+ str(score)

if __name__=='__main__':
    app.run(debug=True) # when we will put debug= True then it means that when we change anything in code it automatically reflects we doesn't need to rerun the code