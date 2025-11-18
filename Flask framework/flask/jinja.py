## building URL dynamically
##variable rule
## Jinja 2 Template engine
'''
{{   }} expresions to print output in html
{%...%} conditions for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request
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

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name'] 
        return f'Hello {name}'
    return render_template('form.html')

#variable rule (when u type cast a particular variable )
@app.route("/success/<int:score>")
def success(score):
    if score>50:
        res="PASSED"
    else:
        res='FAILED'
    return render_template("results.html",results=res)#in this line we created results (parameter) and passed res into it
#used for condition ,table in html file 
@app.route("/successres/<int:score>")
def success1(score):
    if score>50:
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






if __name__ == "__main__":
    app.run(debug=False)


'''
first we used ("/success/<score>") a string value
then we used  ("/success/<int:score>") defining u need to give a int value here

(we typcasted score to use as int and because we have to agn convert it to str to concatinate)
return "The marks you got is "+ str(score)


'''