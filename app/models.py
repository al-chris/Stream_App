from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db, app
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80))
    email = db.Column(db.String(40), nullable=False, unique=False)
    sdate = db.Column(db.DateTime, default=datetime.now)
    gender = db.Column(db.String(6))
    description = db.Column(db.String(500))
    # ppic = db.Column(db.String(500))
    # phone_no = db.Column(db.Integer)
    # location = db.Column(db.String(30))
    # contacts = db.Column(db.String(123456788), default='{}')
    dob = db.Column(db.DateTime)
    email_confirm = db.Column(db.Boolean, default=False)
    phone_confirm = db.Column(db.Boolean, default=False)
    online = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime)
    last_seen = db.Column(db.DateTime)
    last_updated = db.Column(db.DateTime)
    level = db.Column(db.Integer) # access level
    liked = db.Column(db.String(123456788), default='[]')
    prev_usernames = db.Column(db.String(123456788), default='[]')

    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'user_id' : self.id}).decode('utf-8')

    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer(app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return Users.query.get(user_id)