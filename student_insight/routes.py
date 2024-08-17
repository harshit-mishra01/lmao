from student_insight import app
from flask import render_template,request,redirect,url_for,flash
from student_insight.utils import login_procedure, send_mail, student_entry
import os
from flask_login import logout_user,current_user,login_required


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    message = None
    if request.method == 'POST':
        data = request.form.to_dict()
        status = login_procedure(data)
        if status == 1:
            flash("You are Successfully Logged In")
            
            return redirect(url_for('admin'))
        elif status == 2:
            flash("You are Successfully Logged In")
            return redirect(url_for('home'))
        elif status == 4:
            message = "Something Went Wrong"
        else:
            message = "Invalid Credentials"
            
    return render_template("login.html",message = message)

@app.route('/admin', methods = ['POST','GET'])

def admin():
    state1 = None
    state2 = None
    state3 = None
    if request.method == 'POST':
        data = request.form.to_dict()
        file = request.files['profile']
        _ , f_ext = os.path.splitext(file.filename)
        # print(file.filename,_,f_ext)
        if data['course'] != 'Choose...':
            if f_ext in ['.png','.jpg']:
                state3 = student_entry(data,file)
                if state3:
                    send_mail(state3)
                else:
                    state3 = "Something went Wrong"

            else:
                state1 = "Invalid File Format"
        else:
            state2 = "Choose the Course"
    return render_template("AdminForm2.html",message = [state1,state2,state3])
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
