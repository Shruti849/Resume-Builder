from flask import Flask ,render_template
from models import User
from dbhelper import Session
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/users')
def resume():
    with Session() as session:
        users = session.query(User).all()
        return render_template("Resume.html", data=users)

@app.route('/<user_name>')
def profile(user_name):
    user_name = user_name.replace('-', ' ')
    user_name = user_name.title()
    with Session() as session:
        user = User.get_user_by_username(session=session, user_name=user_name)
        if user:
            if user_name == user.name:
                return render_template('Resume.html', detail=user)
        return "User not found!"

if __name__ == '__main__':
    app.run(debug=True)

