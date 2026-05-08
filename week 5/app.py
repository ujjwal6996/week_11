#https://www.youtube.com/live/pO1lsAKJqI4?si=DJx_FXmfzFQykzIb
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from models import db,User,Role,Association

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myapp.sqlite3"

db.init_app(app)
with app.app_context():
    db.create_all() 
# db=SQLAlchemy(app)
app.app_context().push()

#            controllers for role model first
@app.route('/') 
def all_roles():
    roles = Role.query.all()
    print(roles)
    return render_template('index.html',roles=roles)

@app.route('/create_role',methods=['GET','POST'])#same form ke 2 roles hai tabhi dono method ka list dala
def create_role():
    # if request.method=='GET':
        
    if request.method=="POST":#form submit kerney per ye hoga trigger
        role=request.form.get('role')#role naam ke variable mai data retrieve kea jo form se arha hai
        new_role=Role(role_name=role)#object bnaya same role se
        db.session.add(new_role)# session mai add kea
        db.session.commit()#comitted to the database
        return redirect('/')
    return render_template('create_role.html')#paahla bydefault get method choose hoga aur ye trigger hoga jiskey wajah se form dikhega iss link per aker
    #get condition top pe kabhi nhi likhna

#update
@app.route('/update_role/<int:id>',methods=["GET","POST"])#dynamic end point ,by default wo string ki form mai leta iss lea usey int:id likha
def edit_role(id):
    this_role=Role.query.get(id)#retrieves particular object
    if request.method=="POST":
        role=request.form.get('role')
        this_role.role_name=role#lhs is coming from data base adn rhs is coming from form
        db.session.commit()
        return redirect('/')
    return render_template('update_role.html',this_role=this_role)

@app.route('/delete_role/<int:id>')#ismey bss delete pe click kerney per remove kerna toh post method ki jarurat nhi
def del_role(id):
    this_role=Role.query.get(id)#role object
    db.session.delete(this_role)#delete ker da object
    db.session.commit()
    return redirect('/')

#retrieve user dor a particular role
@app.route('/user/<role>')#role string ki form mai jayega
def get_users(role):#role string hai
    role_obj=Role.query.filter_by(role_name=role).first()#retrieve object wtih help of role string
    users=role_obj.users#role is object, users=[list of object] ,iss role_obj ke sarey users
    return render_template('role_users.html',users=users,role=role)
app.run(debug=True)








# #child table
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username=db.Column(db.String(20),nullable=False,unique=True)
#     password=db.Column(db.String(20),nullable=False)
#     role_id=db.Column(db.Integer,db.ForeignKey('role.id'))#table name daala tabhi user ka u small hogya kyuki table name small mai hotey
# #parent table
# class Role(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     role_name=db.Column(db.String(),nullable=False,unique=True)

#     users=db.Relationships('User',backref='role') #list of objects dega JO HAMNEY BNAYE HAI ROLE TABLE KE LEA agar role.users karegey toh
    

