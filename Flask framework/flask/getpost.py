from flask import Flask,render_template,request
#import requests



#WSGI application 
app =Flask(__name__) #which will further interact with web server itself

'''setting get and set methods inside the app.route

'''
@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>" 

@app.route("/index",methods=["GET"])# methods are set to GET by default
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name'] #helps in extracting the name
        return f'Hello {name}'#displays it
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=False)

'''
further tasks is to take the value and push it to the next webpage
and pass this specific information in jinja 2 template engine

further i added action parameter in the form.html 
we added action= submit so whenever we press submit the html will take /submit route

'''