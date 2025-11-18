from flask import Flask

'''
It creates an instance of the flask class
which will be your WSGI(web server gatway interface)
'''

#WSGI application 
app =Flask(__name__) #which will further interact with web server itself

@app.route("/") #whenevr i am using this route it will run the function
def welcome():
    return "Welcome to this page, this should be an amazing journey " 

@app.route("/index")# creating new routes
def index():
    return ' welcome to the index page'


if __name__ == "__main__":
    app.run(debug=False)

''' 
with debug =true you dont always have to restart the server 
to see the changes pythonb will do it automatically 

Need to turn off autosave as it makes the sever restarts on its own
 '''

