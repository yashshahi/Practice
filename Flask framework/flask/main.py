from flask import Flask,render_template



#WSGI application 
app =Flask(__name__) #which will further interact with web server itself

'''
have to create html pages inside the 'templates' folders
as render_template will fetch it from there

'''
@app.route("/") #whenevr i am using this route it will run the function
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>" 

@app.route("/index")# creating new routes
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=False)