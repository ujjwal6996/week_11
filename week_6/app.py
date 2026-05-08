from flask import Flask,request

app=Flask(__name__)


data=[{'username':"mad1","password":"12345","course":"MADI"},
    {'username':"mad2","password":"54321","course":"MADII"},
    {'username':"test_user3","password":"1234","course":"DBMS"},
    {'username':"test_user4","password":"0987","course":"PDSA"}]
        

@app.route("/my_data")
def get_data():
    return data#return data in the form of json,any func that return data in the form of json is called api

@app.route("/userdata/<user>")
def get_user(user):
    for user_dict in data:
        if user_dict["username"]==user:
            return user_dict
        
    return {"message": "user not found!"},404#json mai isi form mai return ker sktey

# @app.route("/adduser",methods=['POST']) ya toh nichey wali line likh lo
@app.post("/adduser")
def new_user():
    newuser=request.json
    data.append(newuser)
    return {
        "message":"user added succesfully"
    }






app.run(debug=True)