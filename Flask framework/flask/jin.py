## building URL dynamically
##variable rule
## Jinja 2 Template engine
'''
{{   }} expresions to print output in html
{%...%} conditions for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for
#import requests



#WSGI application 
app =Flask(__name__) #which will further interact with web server itself

'''Jinja 2 template engine

'''
@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>" 

@app.route("/index",methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name'] 
#         return f'Hello {name}'
#     return render_template('form.html')

#variable rule (when u type cast a particular variable )
@app.route("/success/<int:score>")
def success(score):
    if score>=50:
        res="PASSED"
    else:
        res='FAILED'
    return render_template("results.html",results=res)#in this line we created results (parameter) and passed res into it

#used for condition ,table in html file 
@app.route("/successres/<int:score>")
def success1(score): #this function is called not the url in the last lines
    res=""
    if score>=50:
        res="PASSED"
    else:
        res='FAILED'

    exp= {'score':score,'res':res}
    return render_template("result1.html",results=exp)

#using if condition
@app.route("/successif/<int:score>")
def success2(score):
    # if score>50:
    #     res="PASSED"
    # else:
    #     res='FAILED'   we are adding these conditions in the html file
    return render_template("result2.html",results=score)

@app.route("/fail/<int:score>")
def fail(score):
    
    return render_template("result.html",results=score)

@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('success1',score=total_score))

''' imported more from flask (redirect , url_for)
this will allow me the get_result function to redirect to either
success or failure

url_for :helps in building dynamic url ,creating and redirecting
'''


if __name__ == "__main__":
    app.run(debug=False)