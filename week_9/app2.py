#using flask login module

from flask import Flask,render_template,request,redirect,url_for
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user

app=Flask(__name__)
app.config["SECRET_KEY"]="ujjwal-mad1-flask-login-week9"
login_manager=LoginManager()# instance of login manager 
login_manager.init_app(app)#flask and login manager are linked
login_manager.login_view="signin"#linking login manager for signin function

users={
    "admin":{"password":"admin123","role":"super"},
    "faculty":{"password":"fac123","role":"faculty"},
    "student":{"password":"12345","role":"student"},
}

class User(UserMixin):
    def __init__(self,username):
        self.id=username

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    else:
        return None
    
@app.route("/login",methods=["GET","POST"])
def signin():
    if request.method=="POST":            
        uname=request.form.get("uname")
        pwd=request.form.get("pwd")
        
        if uname in users and users[uname]["password"]==pwd:
            user=User(uname)#instance is created
            login_user(user)#send cookie info
            return redirect(url_for("admin_dashboard"))
        else:
            return"<b>sorry</b>"
    else:
        return render_template("login.html")

  


@app.route("/dashboard")
@login_required
def admin_dashboard():    
    return render_template("dashboard.html")

    
@app.route("/logout")
@login_required
def signout():
    logout_user() # all coookies cleared
    return redirect(url_for("signin"))
if __name__=="__main__":
    app.run(debug=True)