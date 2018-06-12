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
    id = db.Column(db.Integer, primary_key=True)
    colle_name = db.Column(db.String(64), index=True)
    colle_initials = db.Column(db.String(10), index=True)
    colle_age = db.Column(db.String(60), index=True, unique=True) #tirar atrubuto unique
    colle_releasedate = db.Column(db.String(10))
    colle_piecequantity = db.Column(db.Integer)
    pieces = db.relationship('Pieces', backref='colle_owner', lazy='dynamic')

    def __repr__(self):
        return '<Collection {}>'.format(self.colle_name)

class Dial_Movement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dmov_pos1 = db.Column(db.String(2), index=True)
    dmov_pos2 = db.Column(db.String(2), index=True)
    dmov_pos3 = db.Column(db.String(2), index=True)
    dmov_pos4 = db.Column(db.String(2), index=True)
    dmov_pos5 = db.Column(db.String(2), index=True)
    dmov_pos6 = db.Column(db.String(2), index=True)
    dmov_pos7 = db.Column(db.String(2), index=True)
    dmov_pos8 = db.Column(db.String(2), index=True)
    dmov_pos9 = db.Column(db.String(2), index=True)
    dmov_pos10 = db.Column(db.String(2), index=True)
    dmov_pos11 = db.Column(db.String(2), index=True)
    dmov_pos12 = db.Column(db.String(2), index=True)
    dmov_cor1 = db.Column(db.String(30), index=True)
    dmov_cor2 = db.Column(db.String(30), index=True)
    dmov_cor3 = db.Column(db.String(30), index=True)
    dmov_cor4 = db.Column(db.String(30), index=True)
    dmov_cor5 = db.Column(db.String(30), index=True)
    dmov_cor6 = db.Column(db.String(30), index=True)
    dmov_cor7 = db.Column(db.String(30), index=True)
    dmov_cor8 = db.Column(db.String(30), index=True)
    dmov_cor9 = db.Column(db.String(30), index=True)
    dmov_cor10 = db.Column(db.String(30), index=True)
    dmov_cor11 = db.Column(db.String(30), index=True)
    dmov_cor12 = db.Column(db.String(30), index=True)
    #pieces = db.relationship('Pieces', uselist=False, back_populates='dial_movement')
    pieces_id = db.Column(db.Integer, db.ForeignKey('pieces.id'))

    def __repr__(self):
        return '<Dial_Movement {}>'.format(self.id)

class Dial_Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datk_pos1 = db.Column(db.String(2), index=True)
    datk_pos2 = db.Column(db.String(2), index=True)
    datk_pos3 = db.Column(db.String(2), index=True)
    datk_pos4 = db.Column(db.String(2), index=True)
    datk_pos5 = db.Column(db.String(2), index=True)
    datk_pos6 = db.Column(db.String(2), index=True)
    datk_pos7 = db.Column(db.String(2), index=True)
    datk_pos8 = db.Column(db.String(2), index=True)
    datk_pos9 = db.Column(db.String(2), index=True)
    datk_pos10 = db.Column(db.String(2), index=True)
    datk_pos11 = db.Column(db.String(2), index=True)
    datk_pos12 = db.Column(db.String(2), index=True)
    datk_cor1 = db.Column(db.String(30), index=True)
    datk_cor2 = db.Column(db.String(30), index=True)
    datk_cor3 = db.Column(db.String(30), index=True)
    datk_cor4 = db.Column(db.String(30), index=True)
    datk_cor5 = db.Column(db.String(30), index=True)
    datk_cor6 = db.Column(db.String(30), index=True)
    datk_cor7 = db.Column(db.String(30), index=True)
    datk_cor8 = db.Column(db.String(30), index=True)
    datk_cor9 = db.Column(db.String(30), index=True)
    datk_cor10 = db.Column(db.String(30), index=True)
    datk_cor11 = db.Column(db.String(30), index=True)
    datk_cor12 = db.Column(db.String(30), index=True)
    #pieces = db.relationship('Pieces', uselist=False, back_populates='dial_attack')
    pieces_id = db.Column(db.Integer, db.ForeignKey('pieces.id'))

    def __repr__(self):
        return '<Dial_Attack {}>'.format(self.id)

class Dial_Defense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ddef_pos1 = db.Column(db.String(2), index=True)
    ddef_pos2 = db.Column(db.String(2), index=True)
    ddef_pos3 = db.Column(db.String(2), index=True)
    ddef_pos4 = db.Column(db.String(2), index=True)
    ddef_pos5 = db.Column(db.String(2), index=True)
    ddef_pos6 = db.Column(db.String(2), index=True)
    ddef_pos7 = db.Column(db.String(2), index=True)
    ddef_pos8 = db.Column(db.String(2), index=True)
    ddef_pos9 = db.Column(db.String(2), index=True)
    ddef_pos10 = db.Column(db.String(2), index=True)
    ddef_pos11 = db.Column(db.String(2), index=True)
    ddef_pos12 = db.Column(db.String(2), index=True)
    ddef_cor1 = db.Column(db.String(30), index=True)
    ddef_cor2 = db.Column(db.String(30), index=True)
    ddef_cor3 = db.Column(db.String(30), index=True)
    ddef_cor4 = db.Column(db.String(30), index=True)
    ddef_cor5 = db.Column(db.String(30), index=True)
    ddef_cor6 = db.Column(db.String(30), index=True)
    ddef_cor7 = db.Column(db.String(30), index=True)
    ddef_cor8 = db.Column(db.String(30), index=True)
    ddef_cor9 = db.Column(db.String(30), index=True)
    ddef_cor10 = db.Column(db.String(30), index=True)
    ddef_cor11 = db.Column(db.String(30), index=True)
    ddef_cor12 = db.Column(db.String(30), index=True)
    #pieces = db.relationship('Pieces', uselist=False, back_populates='dial_defense')
    pieces_id = db.Column(db.Integer, db.ForeignKey('pieces.id'))

    def __repr__(self):
        return '<Dial_Defense {}>'.format(self.id)

class Dial_Damage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ddam_pos1 = db.Column(db.String(2), index=True)
    ddam_pos2 = db.Column(db.String(2), index=True)
    ddam_pos3 = db.Column(db.String(2), index=True)
    ddam_pos4 = db.Column(db.String(2), index=True)
    ddam_pos5 = db.Column(db.String(2), index=True)
    ddam_pos6 = db.Column(db.String(2), index=True)
    ddam_pos7 = db.Column(db.String(2), index=True)
    ddam_pos8 = db.Column(db.String(2), index=True)
    ddam_pos9 = db.Column(db.String(2), index=True)
    ddam_pos10 = db.Column(db.String(2), index=True)
    ddam_pos11 = db.Column(db.String(2), index=True)
    ddam_pos12 = db.Column(db.String(2), index=True)
    ddam_cor1 = db.Column(db.String(30), index=True)
    ddam_cor2 = db.Column(db.String(30), index=True)
    ddam_cor3 = db.Column(db.String(30), index=True)
    ddam_cor4 = db.Column(db.String(30), index=True)
    ddam_cor5 = db.Column(db.String(30), index=True)
    ddam_cor6 = db.Column(db.String(30), index=True)
    ddam_cor7 = db.Column(db.String(30), index=True)
    ddam_cor8 = db.Column(db.String(30), index=True)
    ddam_cor9 = db.Column(db.String(30), index=True)
    ddam_cor10 = db.Column(db.String(30), index=True)
    ddam_cor11 = db.Column(db.String(30), index=True)
    ddam_cor12 = db.Column(db.String(30), index=True)
    #pieces = db.relationship('Pieces', uselist=False, back_populates='dial_damage')
    pieces_id = db.Column(db.Integer, db.ForeignKey('pieces.id'))

    def __repr__(self):
        return '<Dial_Damage {}>'.format(self.id)

class Pieces(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    piece_name = db.Column(db.String(64), index=True)
    piece_real_name = db.Column(db.String(64), index=True)
    piece_number = db.Column(db.String, index=True)
    piece_trait = db.Column(db.String(300), index=True)
    piece_improved_target = db.Column(db.String(50), index=True)
    piece_improved_mov = db.Column(db.String(50), index=True)
    piece_mov_type = db.Column(db.String(20), index=True)
    piece_atk_type = db.Column(db.String(20), index=True)
    piece_def_type = db.Column(db.String(20), index=True)
    piece_dam_type = db.Column(db.String(20), index=True)
    piece_range = db.Column(db.Integer)
    piece_bolts = db.Column(db.Integer)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))
    #dial_movement_id = db.Column(db.Integer, db.ForeignKey('Dial_Movement.id'))
    #dial_movement = db.relationship('Dial_Movement', back_populates='pieces')
    #dial_attack_id = db.Column(db.Integer, db.ForeignKey('Dial_Attack.id'))
    #dial_attack = db.relationship('Dial_Attack', back_populates='pieces')
    #dial_defense_id = db.Column(db.Integer, db.ForeignKey('Dial_Defense.id'))
    #dial_defense = db.relationship('Dial_Defense', back_populates='pieces')
    #dial_damage_id = db.Column(db.Integer, db.ForeignKey('Dial_Damage.id'))
    #dial_damage = db.relationship('Dial_Damage', back_populates='pieces')
    dial_mov = db.relationship('Dial_Movement', backref='dmove', lazy='dynamic')
    dial_atk = db.relationship('Dial_Attack', backref='datack', lazy='dynamic')
    dial_def = db.relationship('Dial_Defense', backref='ddefense', lazy='dynamic')
    dial_dam = db.relationship('Dial_Damage', backref='ddamage', lazy='dynamic')

    def __repr__(self):
        return '<Piece {}>'.format(self.piece_name)
