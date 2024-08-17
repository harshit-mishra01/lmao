from flask_mail import Message
from PIL import Image
from werkzeug.utils import secure_filename
from random import randint
from secrets import token_hex
from student_insight.models import Admin,Student
from student_insight import app,bcrypt,db,mail
from flask_login import current_user,login_user
import os

def login_procedure(data):
    status = None
    id = data['userid']
    pwd = data['password']
    try:
        if 'ADM' == id[0:3]:
            user = Admin.query.filter_by(id = id).first()
            if user:
                password = bcrypt.check_password_hash(user.password,pwd)
                if password:
                    if login_user(user,remember = False):

                        status = 1

        else:
            student = Student.query.filter_by(id = id).first()
            if student:
                password = bcrypt.check_password_hash(student.password,pwd)
                print(password)
                # status = 6
                if password:
                    status = 2
    except:
        status = 4 
    finally:     
            # status = 4
        return status


def student_entry(data,file):
    status=None
    name = data['name'].upper()
    course = data['course']
    ran = randint(10000,99999)
    space = name.find(" ")
    id = course + name[0] + name[space+1] + str(ran)
    id = id.upper()
    pwd = str(token_hex(8)).upper()
    print(pwd)
    hashed_pwd = bcrypt.generate_password_hash(pwd).decode('utf-8')
    image_name = save_image(file)
    student = Student(id = id ,
                      name = name ,
                      dob = data['dob'] ,
                      fname = data['fname'] ,
                      mob = data['mob'] ,
                      fmob = data['fmob'] ,
                      image_file = image_name,
                      email = data['email'] ,
                      course = course ,
                      password = hashed_pwd)
    try:
        print(type(data['dob']))
        print(data)
        with app.app_context():
            db.session.add(student)
            db.session.commit()
            status = [1,(id,data['email'],pwd)]
        
    except:
        status = 0
    finally:
        return status
    

def save_image(file):
    if file:
        filename = secure_filename(file.filename)
        pic_fname = token_hex(8)
        _ , _ext = os.path.splitext(filename)
        image = pic_fname + _ext
        image_path = os.path.join(app.root_path,'static/profile_pics/',image)
        # file.save(image_path)

        output_size = (250,250)
        i = Image.open(file)
        i.thumbnail(output_size)
        i.save(image_path)
        return image
    else:
        return "Something went wrong"


def send_mail(student):
    with app.app_context():
        # email = current_user.email
        # print(email)
        msg = Message('Student Entry Confirmation', sender = 'noreply@demo.com', recipients = [current_user.email])
        msg.body = f'''The student has been successfully registered in the Database with
            USERID : {student[1][0]}
            Password : {student[1][2]}
    '''
        mail.send(msg)

        msg2 = Message('Successful Registration', sender = 'noreply@demo.com', recipients = [student[1][1]])
        msg2.body = f'''Your are Successfully Registered with us
            (This is system generated password)
            
            Credentials :
            USERID : {student[1][0]}
            Password : {student[1][2]}

    ps: Use this Credentials to change password

    Thanks , for choosing our University.
    '''
        mail.send(msg2)
