#using sessions

from flask import Flask,render_template,request,redirect,url_for
from flask import session
app=Flask(__name__)
app.config["SECRET_KEY"]="ujjwal-mad1-flask-login-week9"

@app.route("/login",methods=["GET","POST"])
def signin():
    if request.method=="POST":            
        uname=request.form.get("uname")
        pwd=request.form.get("pwd")
        session["u"]=uname#stored in browser
        session["p"]=pwd
        if uname=="admin" and pwd =="12345":
            return redirect(url_for("admin_dashboard"))
        else:
            return"<b>sorry<b>"
    else:
        return render_template("login.html")

  



@app.route("/dashboard")
def admin_dashboard():
    uname=session.get("u",None)
    pwd=session.get("p",None)
    if uname:
        return render_template("dashboard.html")
    else:
        return "unauthorised access ,<a href='/login'>Login here </a>"
    
@app.route("/logout")
def signout():
    session.clear() #every cookie info is deleeted
    # session.pop("u",None)# specific deleteeion by name 
    return redirect(url_for("signin"))
if __name__=="__main__":
    app.run(debug=True)