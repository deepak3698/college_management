from flask import Flask,render_template,request,flash,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
import math
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super-secret-key'

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)


mail = Mail(app)

db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    descc = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


class Book_data(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Student_book(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(80), nullable=False)
    bookname = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Student_login(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)

@app.route("/")
def home():
    students = Student_login.query.filter_by().all()
    name = "Student-Panel"
    name1=""
    if ('user1' in session):
        for student in students:
            if (student.studentname == session['user1']):
                return render_template('index.html', params=params,name="welcome "+session['user1'],name1=session['user1']+"-")
    return render_template('index.html',params=params,name=name,name1=name1)


@app.route("/about")
def about():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    return render_template('about.html',params=params,name=name,name1=name1)


@app.route("/news")
def news():
    if('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    return render_template('updated_news.html',params=params,name=name,name1=name1)


@app.route("/event")
def event():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    return render_template('events.html',params=params,name=name,name1=name1)


@app.route("/profile")
def profile():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    return render_template('profile.html',params=params,name=name,name1=name1)


@app.route("/chairman’s_message")
def cm():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    return render_template('cm.html',params=params,name=name,name1=name1)


@app.route("/vision_and_mission")
def vm():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    return render_template('vm.html',params=params,name=name,name1=name1)


@app.route("/certification")
def certification():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    return render_template('certification.html',params=params,name=name,name1=name1)





@app.route("/admin_login",methods = ['GET', 'POST'])
def admin_login():
    msg=""
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    if ('user' in session and session['user'] == params['admin_user']):
        return render_template('index.html', params=params,name=name)
    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        msg = " Invalid Username or Password "
        if (username == params['admin_user'] and userpass == params['admin_password']):
            #set the session variable
            session['user'] = username
            return render_template('index.html', params=params,name=name)
    return render_template('admin_login.html', params=params,name=name,msg=msg,name1=name1)


@app.route("/student_login",methods = ['GET', 'POST'])
def student_login():
    msg=""
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    students = Student_login.query.filter_by().all()
    i = 0
    if ('user1' in session):
        for student in students:
            if (student.studentname == session['user1']):
                i = 1
    if (i == 1):
        return render_template('index.html', params=params,name=name,name1=name1)
    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        students = Student_login.query.filter_by().all()
        i=0
        msg=" Invalid Username or Password "
        for student in students:
            if(student.studentname==username and student.password==userpass):
                i=1
        if (i==1):
            session['user1'] = username
            return render_template('index.html', params=params,name=name,name1=name1)
    return render_template('student_login.html',params=params,name=name,msg=msg,name1=name1)




@app.route("/it")
def it():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    return render_template('it.html',params=params,name=name,name1=name1)




@app.route("/cs")
def cs():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1 = ""
    return render_template('cs.html',params=params,name=name,name1=name1)





@app.route("/contact",methods = ['GET', 'POST'])
def contact():
    if ('user1' in session):
        namee = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        namee = "Student-Panel"
        name1 = ""
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        descc = request.form.get('message')
        entry = Contact(name=name, phone = phone, descc = descc, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('New message from ' + name,
        #                   sender=email,
        #                   recipients = [params['gmail-user']],
        #                   body = descc + "\n" + phone
        #                   )
        flash('Thanks for giving your feedback')
    return render_template('contact.html', params=params,name=namee,name1=name1)




@app.route("/library")
def library():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1=""
    books = Book_data.query.filter_by().all()
    last = math.ceil(len(books) / int(params['no_of_posts']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    books = books[(page - 1) * int(params['no_of_posts']): (page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = "#"
        next = "/library?page=" + str(page + 1)
    elif (page == last):
        prev = "/library?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/library?page=" + str(page - 1)
        next = "/library?page=" + str(page + 1)

    return render_template('library.html',params=params, books=books, prev=prev, next=next,name=name,name1=name1)




@app.route("/stu_show",methods = ['GET', 'POST'])
def stu_show():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1 = ""
    students = Student_login.query.filter_by().all()
    i = 0
    if ('user1' in session):
        for student in students:
            if (student.studentname == session['user1']):
                i = 1
    if ('user' in session and session['user'] == params['admin_user'] or i==1):
        books = Student_book.query.filter_by().all()
        last = math.ceil(len(books) / int(params['no_of_posts']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        books = books[(page - 1) * int(params['no_of_posts']): (page - 1) * int(params['no_of_posts']) + int(
            params['no_of_posts'])]
        if (page == 1):
            prev = "#"
            next = "/stu_show?page=" + str(page + 1)
        elif (page == last):
            prev = "/stu_show?page=" + str(page - 1)
            next = "#"
        else:
            prev = "/stu_show?page=" + str(page - 1)
            next = "/stu_show?page=" + str(page + 1)
        return render_template('stu_show.html',params=params, books=books, prev=prev, next=next,name=name,name1=name1)
    return render_template('admin_login.html', params=params,name=name,name1=name1)




@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1 = ""
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            bookname = request.form.get('name')
            author = request.form.get('author')
            publisher = request.form.get('publisher')
            quantity = request.form.get('quantity')
            date = datetime.now()
            books = Book_data.query.filter_by(sno=sno).first()
            books.bookname = bookname
            books.author = author
            books.publisher = publisher
            books.quantity = quantity
            books.date = date
            db.session.commit()
            flash("book edited")
            return redirect('/edit/' + sno)
        books = Book_data.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, books=books,name=name,name1=name1)



@app.route("/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        book = Book_data.query.filter_by(sno=sno).first()
        db.session.delete(book)
        db.session.commit()
    return redirect('/manipulate')



@app.route("/manipulate")
def manipulate():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1 = ""
    if ('user' in session and session['user'] == params['admin_user']):
        books = Book_data.query.filter_by().all()
        last = math.ceil(len(books) / int(params['no_of_posts']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        books = books[(page - 1) * int(params['no_of_posts']): (page - 1) * int(params['no_of_posts']) + int(
            params['no_of_posts'])]
        if (page == 1):
            prev = "#"
            next = "/manipulate?page=" + str(page + 1)
        elif (page == last):
            prev = "/manipulate?page=" + str(page - 1)
            next = "#"
        else:
            prev = "/manipulate?page=" + str(page - 1)
            next = "/manipulate?page=" + str(page + 1)

        return render_template('manipulate.html', params=params, books=books, prev=prev, next=next,name=name,name1=name1)
    return render_template('admin_login.html', params=params,name=name,name1=name1)



@app.route("/adminlogout")
def adminlogout():
    if ('user' in session):
        session.pop('user')
    return redirect('/')



@app.route("/studentlogout")
def studentlogout():
    if('user1' in session):
        session.pop('user1')
    return redirect('/')



@app.route("/addbook",methods = ['GET', 'POST'])
def addbook():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1 = ""
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == 'POST'):
            books = Book_data.query.filter_by().all()
            bookname = request.form.get('bookname')
            author = request.form.get('author')
            publisher = request.form.get('publisher')
            quantity = request.form.get('quantity')
            i=0
            for book in books:
                if(book.bookname==bookname):
                    book.quantity=int(book.quantity)+int(quantity)
                    db.session.commit()
                    i=1
            if(i!=1):
                entry = Book_data(bookname=bookname, author=author, publisher=publisher, quantity=quantity,
                                  date=datetime.now())
                db.session.add(entry)
                db.session.commit()
                flash("Successfully added")
        return render_template('addbook.html',params=params,name=name,name1=name1)
    return render_template('admin_login.html', params=params,name=name,name1=name1)



@app.route("/lendbook",methods = ['GET', 'POST'])
def lendbook():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1 = ""
    students = Student_login.query.filter_by().all()
    i = 0
    if('user1' in session):
        for student in students:
            if (student.studentname == session['user1']):
                i = 1
    if ('user1' in session and i==1):
        books = Book_data.query.filter_by().all()
        last = math.ceil(len(books) / int(params['no_of_posts']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        books = books[(page - 1) * int(params['no_of_posts']): (page - 1) * int(params['no_of_posts']) + int(
            params['no_of_posts'])]
        if (page == 1):
            prev = "#"
            next = "/lendbook?page=" + str(page + 1)
        elif (page == last):
            prev = "/lendbook?page=" + str(page - 1)
            next = "#"
        else:
            prev = "/lendbook?page=" + str(page - 1)
            next = "/lendbook?page=" + str(page + 1)
        # if(sno==0):
        #     if (request.method == 'POST'):
        #         studentname = request.form.get('bookname')
        #         bookname = request.form.get('author')
        #         entry1 = Student_book(student_name=studentname, bookname=bookname, date=datetime.now())
        #         db.session.add(entry1)
        #         db.session.commit()
        #         return render_template('contact.html', params=params)
        #     return render_template('lendbook.html', params=params,sno=sno)

        return render_template('lendbook.html', params=params, books=books, prev=prev, next=next,name=name,name1=name1)
    return render_template('student_login.html', params=params,name=name,name1=name1)


@app.route("/return",methods = ['GET', 'POST'])
def returnn():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1 = ""
    students = Student_login.query.filter_by().all()
    i = 0
    if('user1' in session):
        for student in students:
            if (student.studentname == session['user1']):
                i = 1
    if ('user1' in session and i==1):
        books = Student_book.query.filter_by(student_name=session['user1']).all()
        last = math.ceil(len(books) / int(params['no_of_posts']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        books = books[(page - 1) * int(params['no_of_posts']): (page - 1) * int(params['no_of_posts']) + int(
            params['no_of_posts'])]
        if (page == 1):
            prev = "#"
            next = "/lendbook?page=" + str(page + 1)
        elif (page == last):
            prev = "/lendbook?page=" + str(page - 1)
            next = "#"
        else:
            prev = "/lendbook?page=" + str(page - 1)
            next = "/lendbook?page=" + str(page + 1)

        return render_template('student_return.html', params=params, books=books, prev=prev, next=next,name=name,name1=name1)
    return render_template('student_login.html', params=params,name=name,name1=name1)


@app.route("/returnbook/<string:sno>",methods = ['GET', 'POST'])
def returnbook(sno):
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1 = ""
    students = Student_login.query.filter_by().all()
    j = 0
    if ('user1' in session):
        for student in students:
            if (student.studentname == session['user1']):
                j = 1
    if ('user1' in session and j == 1):
        student = Student_book.query.filter_by(sno=sno).first()
        if (request.method == 'POST'):
            books = Book_data.query.filter_by().all()
            studentname = request.form.get('studentname')
            bookname = request.form.get('bookname')
            i = 0
            if (session['user1'] == studentname):
                for book in books:
                    if (book.bookname == bookname):
                        book.quantity = book.quantity + 1
                        db.session.commit()
                        i = 1
                        db.session.delete(student)
                        db.session.commit()
                        flash("successfully returned")
            if (i != 1):
                entry = Book_data(bookname=bookname, author=book.author, publisher=book.publisher, quantity=1,
                                  date=datetime.now())
                db.session.add(entry)
                db.session.commit()
                db.session.delete(student)
                db.session.commit()
                flash("successfully returned")
        return render_template('returnbook.html', params=params, name=name, student=student, sno=sno,name1=name1)
    return render_template('student_login.html', params=params, name=name,name1=name1)


@app.route("/studentinfo/<string:sno>",methods = ['GET', 'POST'])
def studentinfo(sno):
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1 = ""
    students = Student_login.query.filter_by().all()
    i = 0
    if ('user1' in session):
        for student in students:
            if (student.studentname == session['user1']):
                i = 1
    if ('user1' in session and i==1):
        books = Book_data.query.filter_by(sno=sno).first()
        if (request.method == 'POST'):
            book = Book_data.query.filter_by(sno=sno).first()
            studentname = request.form.get('studentname')
            bookname = request.form.get('author')
            if(session['user1']==studentname):
                entry = Student_book(student_name=studentname, bookname=bookname,author=book.author,publisher=book.publisher,date=datetime.now())
                db.session.add(entry)
                db.session.commit()
                if(book.quantity>1):
                    book.quantity=book.quantity-1
                    db.session.commit()
                else:
                    db.session.delete(book)
                    db.session.commit()
                flash("Book Lended")
        return render_template('student_info.html', params=params, books=books, sno=sno,name=name,name1=name1)
    return render_template('student_login.html', params=params,name=name,name1=name1)



@app.route("/stu_reg",methods = ['GET', 'POST'])
def stu_reg():
    if ('user1' in session):
        name = "welcome " + session['user1']
        name1 = session['user1'] + "-"
    else:
        name = "Student-Panel"
        name1 =""
    if (request.method == 'POST'):
        studentname = request.form.get('studentname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        entry = Student_login(studentname=studentname,email=email,phone=phone,password=password, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        flash("successfully registered")
    return render_template('stu_reg.html', params=params,name=name,name1=name1)



if __name__ == "__main__":
    app.run(debug=True)