from flask import Flask # import Flask module
app = Flask(__name__) # creating obj of Flask class

@app.route('/') # this  is a decorator. in this we give the url of the web age
def hello_world(): # creating a function
   return 'Hello World' # returing the output to the webpage

if __name__ == '__main__': # checking for main function
   app.run() # this is to run the Flask program

