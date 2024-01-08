
from app import db
from marshmallow import fields, Schema

class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    data=fields.Str()
    user_id=fields.Int(dump_only=True)
    
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    email = fields.Str()
    paasword = fields.Str(dump_only=True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')   

    