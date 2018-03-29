from app import app
from flask import render_template, flash, redirect
from .Forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'jiang'}
    # return render_template("index.html", title='HOME', user= user)
    posts= [{
            'author': { 'nickname': 'Jiang'},
            'body': 'Beautiful day in Portland!'},
        {
            'author': { 'nickname': 'Chao' },
            'body': 'The Avengers movie was so cool!'
        }]
    LearnFrom=[{'teacher': {'nickname':'可汗爷爷'},
                'link':'https://www.jianshu.com/p/23e2bc731598'}]
    return render_template("index.html", title='Home', user=user, posts=posts, LearnFrom=LearnFrom)
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Name:' + form.name.data)
        flash('passwd:' + form.password.data)
        flash('remember_me:' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign in', form=form)
