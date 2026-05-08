from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/register',methods=["GET","POST"])
def register():
    # if request.method=="GET":  by default get method hota
    #     return render_template("register.html")
    if request.method=="POST":
        name=request.form.get("name")
        gender=request.form.get("gender")
        age=request.form.get("age")
        qual=request.form.get("qual")
        stream=request.form.get("stream")
        address=request.form.get("address")
        return render_template("review.html",name=name,gender=gender,age=age,qual=qual,stream=stream,address=address)

    
    return render_template("register.html")

@app.route("/success")
def success():
    return "<h5> your registration is successful!</h5> "
    
app.run(debug=True)