from flask import Flask,redirect,url_for,render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') # render template is used to redirect to next page

if __name__ == '__main__':
    app.run(debug=True)