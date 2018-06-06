from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Collection(db.Model):
    colle_id = db.Column(db.Integer, primary_key=True)
    colle_name = db.Column(db.String(64), index=True)
    colle_initials = db.Column(db.String(10), index=True)
    colle_age = db.Column(db.String(60), index=True, unique=True)
    colle_releasedate = db.Column(db.String(10))
    colle_piecequantity = db.Column(db.Integer)
    units = db.relationship('Units', backref='unit', lazy='dynamic')

    def __repr__(self):
        return '<Collection {}>'.format(self.colle_name)

class Units(db.Model):
    units_id = db.Column(db.Integer, primary_key=True)
    units_name = db.Column(db.String(64), index=True)
    units_realname = db.Column(db.String(64), index=True)
    units_number = db.Column(db.String, index=True)
    units_trait = db.Column(db.String(300), index=True)
    units_improvedtarget = db.Column(db.String(50), index=True)
    units_improvedmoviment = db.Column(db.String(50), index=True)
    units_range = db.Column(db.Integer)
    units_bolts = db.Column(db.Integer)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.colle_id'))
    dial_move = db.relationship('Dial_Move', backref='dmove', lazy='dynamic')
    dial_datack = db.relationship('Dial_Atack', backref='datack', lazy='dynamic')
    dial_defense = db.relationship('Dial_Defense', backref='ddefense', lazy='dynamic')
    dial_damage = db.relationship('Dial_Damage', backref='ddamage', lazy='dynamic')

    def __repr__(self):
        return '<Units {}>'.format(self.units_name)

class Dial_Move(db.Model):
    dmove_id = db.Column(db.Integer, primary_key=True)
    dmove_pos1 = db.Column(db.Integer, index=True)
    dmove_pos2 = db.Column(db.Integer, index=True)
    dmove_pos3 = db.Column(db.Integer, index=True)
    dmove_pos4 = db.Column(db.Integer, index=True)
    dmove_pos5 = db.Column(db.Integer, index=True)
    dmove_pos6 = db.Column(db.Integer, index=True)
    dmove_pos7 = db.Column(db.Integer, index=True)
    dmove_pos8 = db.Column(db.Integer, index=True)
    dmove_pos9 = db.Column(db.Integer, index=True)
    dmove_pos10 = db.Column(db.Integer, index=True)
    dmove_pos11 = db.Column(db.Integer, index=True)
    dmove_pos12 = db.Column(db.Integer, index=True)
    dmove_cor1 = db.Column(db.String(30), index=True)
    dmove_cor2 = db.Column(db.String(30), index=True)
    dmove_cor3 = db.Column(db.String(30), index=True)
    dmove_cor4 = db.Column(db.String(30), index=True)
    dmove_cor5 = db.Column(db.String(30), index=True)
    dmove_cor6 = db.Column(db.String(30), index=True)
    dmove_cor7 = db.Column(db.String(30), index=True)
    dmove_cor8 = db.Column(db.String(30), index=True)
    dmove_cor9 = db.Column(db.String(30), index=True)
    dmove_cor10 = db.Column(db.String(30), index=True)
    dmove_cor11 = db.Column(db.String(30), index=True)
    dmove_cor12 = db.Column(db.String(30), index=True)
    units_id = db.Column(db.Integer, db.ForeignKey('units.units_id'))

    def __repr__(self):
        return '<Dial_Move {}>'.format(self.dmove_id)

class Dial_Atack(db.Model):
    datack_id = db.Column(db.Integer, primary_key=True)
    datack_pos1 = db.Column(db.Integer, index=True)
    datack_pos2 = db.Column(db.Integer, index=True)
    datack_pos3 = db.Column(db.Integer, index=True)
    datack_pos4 = db.Column(db.Integer, index=True)
    datack_pos5 = db.Column(db.Integer, index=True)
    datack_pos6 = db.Column(db.Integer, index=True)
    datack_pos7 = db.Column(db.Integer, index=True)
    datack_pos8 = db.Column(db.Integer, index=True)
    datack_pos9 = db.Column(db.Integer, index=True)
    datack_pos10 = db.Column(db.Integer, index=True)
    datack_pos11 = db.Column(db.Integer, index=True)
    datack_pos12 = db.Column(db.Integer, index=True)
    datack_cor1 = db.Column(db.String(30), index=True)
    datack_cor2 = db.Column(db.String(30), index=True)
    datack_cor3 = db.Column(db.String(30), index=True)
    datack_cor4 = db.Column(db.String(30), index=True)
    datack_cor5 = db.Column(db.String(30), index=True)
    datack_cor6 = db.Column(db.String(30), index=True)
    datack_cor7 = db.Column(db.String(30), index=True)
    datack_cor8 = db.Column(db.String(30), index=True)
    datack_cor9 = db.Column(db.String(30), index=True)
    datack_cor10 = db.Column(db.String(30), index=True)
    datack_cor11 = db.Column(db.String(30), index=True)
    datack_cor12 = db.Column(db.String(30), index=True)
    units_id = db.Column(db.Integer, db.ForeignKey('units.units_id'))

    def __repr__(self):
        return '<Dial_atack {}>'.format(self.datack_id)


class Dial_Defense(db.Model):
    ddefense_id = db.Column(db.Integer, primary_key=True)
    ddefense_pos1 = db.Column(db.Integer, index=True)
    ddefense_pos2 = db.Column(db.Integer, index=True)
    ddefense_pos3 = db.Column(db.Integer, index=True)
    ddefense_pos4 = db.Column(db.Integer, index=True)
    ddefense_pos5 = db.Column(db.Integer, index=True)
    ddefense_pos6 = db.Column(db.Integer, index=True)
    ddefense_pos7 = db.Column(db.Integer, index=True)
    ddefense_pos8 = db.Column(db.Integer, index=True)
    ddefense_pos9 = db.Column(db.Integer, index=True)
    ddefense_pos10 = db.Column(db.Integer, index=True)
    ddefense_pos11 = db.Column(db.Integer, index=True)
    ddefense_pos12 = db.Column(db.Integer, index=True)
    ddefense_cor1 = db.Column(db.String(30), index=True)
    ddefense_cor2 = db.Column(db.String(30), index=True)
    ddefense_cor3 = db.Column(db.String(30), index=True)
    ddefense_cor4 = db.Column(db.String(30), index=True)
    ddefense_cor5 = db.Column(db.String(30), index=True)
    ddefense_cor6 = db.Column(db.String(30), index=True)
    ddefense_cor7 = db.Column(db.String(30), index=True)
    ddefense_cor8 = db.Column(db.String(30), index=True)
    ddefense_cor9 = db.Column(db.String(30), index=True)
    ddefense_cor10 = db.Column(db.String(30), index=True)
    ddefense_cor11 = db.Column(db.String(30), index=True)
    ddefense_cor12 = db.Column(db.String(30), index=True)
    units_id = db.Column(db.Integer, db.ForeignKey('units.units_id'))

    def __repr__(self):
        return '<Dial_defense {}>'.format(self.ddefense_id)

class Dial_Damage(db.Model):
    ddamage_id = db.Column(db.Integer, primary_key=True)
    ddamage_pos1 = db.Column(db.Integer, index=True)
    ddamage_pos2 = db.Column(db.Integer, index=True)
    ddamage_pos3 = db.Column(db.Integer, index=True)
    ddamage_pos4 = db.Column(db.Integer, index=True)
    ddamage_pos5 = db.Column(db.Integer, index=True)
    ddamage_pos6 = db.Column(db.Integer, index=True)
    ddamage_pos7 = db.Column(db.Integer, index=True)
    ddamage_pos8 = db.Column(db.Integer, index=True)
    ddamage_pos9 = db.Column(db.Integer, index=True)
    ddamage_pos10 = db.Column(db.Integer, index=True)
    ddamage_pos11 = db.Column(db.Integer, index=True)
    ddamage_pos12 = db.Column(db.Integer, index=True)
    ddamage_cor1 = db.Column(db.String(30), index=True)
    ddamage_cor2 = db.Column(db.String(30), index=True)
    ddamage_cor3 = db.Column(db.String(30), index=True)
    ddamage_cor4 = db.Column(db.String(30), index=True)
    ddamage_cor5 = db.Column(db.String(30), index=True)
    ddamage_cor6 = db.Column(db.String(30), index=True)
    ddamage_cor7 = db.Column(db.String(30), index=True)
    ddamage_cor8 = db.Column(db.String(30), index=True)
    ddamage_cor9 = db.Column(db.String(30), index=True)
    ddamage_cor10 = db.Column(db.String(30), index=True)
    ddamage_cor11 = db.Column(db.String(30), index=True)
    ddamage_cor12 = db.Column(db.String(30), index=True)
    units_id = db.Column(db.Integer, db.ForeignKey('units.units_id'))

    def __repr__(self):
        return '<Dial_damage {}>'.format(self.ddamage_id)
