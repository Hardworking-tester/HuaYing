# encoding:utf-8
# author:wwg
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from nameForm import NameForm
from tableClass import *
app=Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY']='wwg'
@app.route('/',methods=['GET','POST'])
def index():
    name=None
    form2=NameForm()
    if form2.validate_on_submit():
        user=User(name=form2.name.data,password=form2.password.data)
        # print form2.name.data
        # print form2.password.data
        db.session.add(user)
        db.session.commit()
        name=form2.name.data
        # return redirect(url_for('index'))
        form2.name.data=''
        form2.password.data=''
    return render_template('t1.html',form1=form2,name=name)

if __name__=="__main__":
    app.run(debug=True)