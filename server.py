from flask import Flask, render_template, redirect,request
from users import User

app = Flask(__name__)
#ruta que redirecciona a users
@app.route('/')
def index():
    return redirect('/users')

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("users.html", usuarios = users)

@app.route('/user/new')
def new():
    return render_template("new.html")

#agregar
@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
    