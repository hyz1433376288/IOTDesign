from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from db import *
app=Flask(__name__)

from wtforms import Form,TextField,PasswordField,validators

class LoginForm(Form):
    username = TextField("username",[validators.Required()])
    password = PasswordField("password",[validators.Required()])
   # print("----")
@app.route("/login",methods=['GET','POST'])
def login():
    #print("*********8")
    myForm=LoginForm(request.form)

   # print(myForm.password.data)

    if request.method =='POST':
        if (isExisted(myForm.username.data,myForm.password.data)):
            return redirect("http://Waynicshine.github.io")
        else:
            return "Login Failed"
    return render_template("login.html", form=myForm)

if __name__=="__main__":
   app.run(debug=True)