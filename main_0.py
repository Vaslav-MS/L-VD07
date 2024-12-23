from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

with app.app_context():
    db.create_all()

@app.route('/add_user')
def add_user():
    new_user = User(username='new_username')
    db.session.add(new_user)
    db.session.commit()
    return 'User added'

@app.route('/users')
def get_users():
    users = User.query.all()
    return str(users)

if __name__ == '__main__':
    app.run(debug=True)
