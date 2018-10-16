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
    team = db.relationship('Team', backref='team_owner', lazy='dynamic')

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
    colle_age = db.Column(db.String(60), index=True)
    colle_releasedate = db.Column(db.String(10)) #mudar tipo para date
    colle_piecequantity = db.Column(db.Integer)
    pieces = db.relationship('Pieces', backref='colle_owner', lazy='dynamic')

    def __repr__(self):
        return '<Collection {}>'.format(self.colle_name)

#many-to-many relationship between Team and Pieces
team_and_pieces = db.Table('team_and_pieces',
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
    db.Column('piece_id',  db.Integer,  db.ForeignKey('pieces.id'))
)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(64), index=True)
    team_point = db.Column(db.Integer, index=True)
    team_desc = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pieces_team = db.relationship('Pieces', secondary=team_and_pieces, backref=db.backref('teampi', lazy='dynamic'))

    def __repr__(self):
        return '<Team {}>'.format(self.team_name)




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
    dmov_pos13 = db.Column(db.String(2), index=True)
    dmov_pos14 = db.Column(db.String(2), index=True)
    dmov_pos15 = db.Column(db.String(2), index=True)
    dmov_pos16 = db.Column(db.String(2), index=True)
    dmov_pos17 = db.Column(db.String(2), index=True)
    dmov_pos18 = db.Column(db.String(2), index=True)
    dmov_pos19 = db.Column(db.String(2), index=True)
    dmov_pos20 = db.Column(db.String(2), index=True)
    dmov_pos21 = db.Column(db.String(2), index=True)
    dmov_pos22 = db.Column(db.String(2), index=True)
    dmov_pos23 = db.Column(db.String(2), index=True)
    dmov_pos24 = db.Column(db.String(2), index=True)
    dmov_pos25 = db.Column(db.String(2), index=True)
    dmov_pos26 = db.Column(db.String(2), index=True)
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
    dmov_cor13 = db.Column(db.String(30), index=True)
    dmov_cor14 = db.Column(db.String(30), index=True)
    dmov_cor15 = db.Column(db.String(30), index=True)
    dmov_cor16 = db.Column(db.String(30), index=True)
    dmov_cor17 = db.Column(db.String(30), index=True)
    dmov_cor18 = db.Column(db.String(30), index=True)
    dmov_cor19 = db.Column(db.String(30), index=True)
    dmov_cor20 = db.Column(db.String(30), index=True)
    dmov_cor21 = db.Column(db.String(30), index=True)
    dmov_cor22 = db.Column(db.String(30), index=True)
    dmov_cor23 = db.Column(db.String(30), index=True)
    dmov_cor24 = db.Column(db.String(30), index=True)
    dmov_cor25 = db.Column(db.String(30), index=True)
    dmov_cor26 = db.Column(db.String(30), index=True)
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
    datk_pos13 = db.Column(db.String(2), index=True)
    datk_pos14 = db.Column(db.String(2), index=True)
    datk_pos15 = db.Column(db.String(2), index=True)
    datk_pos16 = db.Column(db.String(2), index=True)
    datk_pos17 = db.Column(db.String(2), index=True)
    datk_pos18 = db.Column(db.String(2), index=True)
    datk_pos19 = db.Column(db.String(2), index=True)
    datk_pos20 = db.Column(db.String(2), index=True)
    datk_pos21 = db.Column(db.String(2), index=True)
    datk_pos22 = db.Column(db.String(2), index=True)
    datk_pos23 = db.Column(db.String(2), index=True)
    datk_pos24 = db.Column(db.String(2), index=True)
    datk_pos25 = db.Column(db.String(2), index=True)
    datk_pos26 = db.Column(db.String(2), index=True)
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
    datk_cor13 = db.Column(db.String(30), index=True)
    datk_cor14 = db.Column(db.String(30), index=True)
    datk_cor15 = db.Column(db.String(30), index=True)
    datk_cor16 = db.Column(db.String(30), index=True)
    datk_cor17 = db.Column(db.String(30), index=True)
    datk_cor18 = db.Column(db.String(30), index=True)
    datk_cor19 = db.Column(db.String(30), index=True)
    datk_cor20 = db.Column(db.String(30), index=True)
    datk_cor21 = db.Column(db.String(30), index=True)
    datk_cor22 = db.Column(db.String(30), index=True)
    datk_cor23 = db.Column(db.String(30), index=True)
    datk_cor24 = db.Column(db.String(30), index=True)
    datk_cor25 = db.Column(db.String(30), index=True)
    datk_cor26 = db.Column(db.String(30), index=True)
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
    ddef_pos13 = db.Column(db.String(2), index=True)
    ddef_pos14 = db.Column(db.String(2), index=True)
    ddef_pos15 = db.Column(db.String(2), index=True)
    ddef_pos16 = db.Column(db.String(2), index=True)
    ddef_pos17 = db.Column(db.String(2), index=True)
    ddef_pos18 = db.Column(db.String(2), index=True)
    ddef_pos19 = db.Column(db.String(2), index=True)
    ddef_pos20 = db.Column(db.String(2), index=True)
    ddef_pos21 = db.Column(db.String(2), index=True)
    ddef_pos22 = db.Column(db.String(2), index=True)
    ddef_pos23 = db.Column(db.String(2), index=True)
    ddef_pos24 = db.Column(db.String(2), index=True)
    ddef_pos25 = db.Column(db.String(2), index=True)
    ddef_pos26 = db.Column(db.String(2), index=True)
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
    ddef_cor13 = db.Column(db.String(30), index=True)
    ddef_cor14 = db.Column(db.String(30), index=True)
    ddef_cor15 = db.Column(db.String(30), index=True)
    ddef_cor16 = db.Column(db.String(30), index=True)
    ddef_cor17 = db.Column(db.String(30), index=True)
    ddef_cor18 = db.Column(db.String(30), index=True)
    ddef_cor19 = db.Column(db.String(30), index=True)
    ddef_cor20 = db.Column(db.String(30), index=True)
    ddef_cor21 = db.Column(db.String(30), index=True)
    ddef_cor22 = db.Column(db.String(30), index=True)
    ddef_cor23 = db.Column(db.String(30), index=True)
    ddef_cor24 = db.Column(db.String(30), index=True)
    ddef_cor25 = db.Column(db.String(30), index=True)
    ddef_cor26 = db.Column(db.String(30), index=True)
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
    ddam_pos13 = db.Column(db.String(2), index=True)
    ddam_pos14 = db.Column(db.String(2), index=True)
    ddam_pos15 = db.Column(db.String(2), index=True)
    ddam_pos16 = db.Column(db.String(2), index=True)
    ddam_pos17 = db.Column(db.String(2), index=True)
    ddam_pos18 = db.Column(db.String(2), index=True)
    ddam_pos19 = db.Column(db.String(2), index=True)
    ddam_pos20 = db.Column(db.String(2), index=True)
    ddam_pos21 = db.Column(db.String(2), index=True)
    ddam_pos22 = db.Column(db.String(2), index=True)
    ddam_pos23 = db.Column(db.String(2), index=True)
    ddam_pos24 = db.Column(db.String(2), index=True)
    ddam_pos25 = db.Column(db.String(2), index=True)
    ddam_pos26 = db.Column(db.String(2), index=True)
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
    ddam_cor13 = db.Column(db.String(30), index=True)
    ddam_cor14 = db.Column(db.String(30), index=True)
    ddam_cor15 = db.Column(db.String(30), index=True)
    ddam_cor16 = db.Column(db.String(30), index=True)
    ddam_cor17 = db.Column(db.String(30), index=True)
    ddam_cor18 = db.Column(db.String(30), index=True)
    ddam_cor19 = db.Column(db.String(30), index=True)
    ddam_cor20 = db.Column(db.String(30), index=True)
    ddam_cor21 = db.Column(db.String(30), index=True)
    ddam_cor22 = db.Column(db.String(30), index=True)
    ddam_cor23 = db.Column(db.String(30), index=True)
    ddam_cor24 = db.Column(db.String(30), index=True)
    ddam_cor25 = db.Column(db.String(30), index=True)
    ddam_cor26 = db.Column(db.String(30), index=True)
    pieces_id = db.Column(db.Integer, db.ForeignKey('pieces.id'))

    def __repr__(self):
        return '<Dial_Damage {}>'.format(self.id)

#many-to-many relationship between pieces and traits
#pieces_and_traits = db.Table('pieces_and_traits',
#    db.Column('piece_id', db.Integer, db.ForeignKey('pieces.id'), primary_key=True),
#    db.Column('trait_id', db.Integer, db.ForeignKey('traits.id'), primary_key=True)
#)

#many-to-many relationship between pieces and keywords
# pieces_and_keywords = db.Table('pieces_and_keywords',
#     db.Column('piece_id', db.Integer, db.ForeignKey('pieces.id'), primary_key=True),
#     db.Column('keyword_id', db.Integer, db.ForeignKey('keywords.id'), primary_key=True)
# )

#many-to-many relationship between pieces and team habilities
#pieces_and_team_habilites = db.Table('pieces_and_team_habilites',
#    db.Column('piece_id', db.Integer, db.ForeignKey('pieces.id'), primary_key=True),
#    db.Column('team_hability_id', db.Integer, db.ForeignKey('team_habilities.id'), primary_key=True)
#)

class Pieces(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    piece_name = db.Column(db.String(64), index=True)
    piece_real_name = db.Column(db.String(64), index=True)
    piece_number = db.Column(db.String, index=True)
    piece_point = db.Column(db.Integer, index=True)
    piece_rarity = db.Column(db.String(10), index=True)
    piece_improved_target = db.Column(db.String(50), index=True)
    piece_improved_mov = db.Column(db.String(50), index=True)
    piece_mov_type = db.Column(db.String(20), index=True)
    piece_atk_type = db.Column(db.String(20), index=True)
    piece_def_type = db.Column(db.String(20), index=True)
    piece_dam_type = db.Column(db.String(20), index=True)
    piece_range = db.Column(db.Integer)
    piece_bolts = db.Column(db.Integer)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))
    dial_mov = db.relationship('Dial_Movement', backref='dmove', lazy='dynamic')
    dial_atk = db.relationship('Dial_Attack', backref='datack', lazy='dynamic')
    dial_def = db.relationship('Dial_Defense', backref='ddefense', lazy='dynamic')
    dial_dam = db.relationship('Dial_Damage', backref='ddamage', lazy='dynamic')
    #pieces_traits = db.relationship('Traits', secondary=pieces_and_traits, backref=db.backref('trait', lazy='dynamic'))
    #pieces_keywords = db.relationship('Keywords', secondary=pieces_and_keywords, backref=db.backref('keyword', lazy='dynamic'))
    #pieces_team_habilites = db.relationship('Team_Habilities', secondary=pieces_and_team_habilites, backref=db.backref('team_hability', lazy='dynamic'))

    def __repr__(self):
        return '<Piece {}>'.format(self.piece_name)

class Traits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trait_name = db.Column(db.String(20), index=True)
    trait_description = db.Column(db.String(3000), index=True)

    def __repr__(self):
        return '<Trait {}>'.format(self.trait_name)

#many-to-many relationship between keywords and additional team habilities
#keywords_and_additional_thab = db.Table('keywords_and_additional_thab',
#    db.Column('keyword_id', db.Integer, db.ForeignKey('keywords.id'), primary_key=True),
#    db.Column('additional_thab_id', db.Integer, db.ForeignKey('add_team_habilities.id'), primary_key=True)
#)

class Keywords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key_name = db.Column(db.String(25), index=True)
    #keywords_add_team_habilities = db.relationship('Add_Team_Habilities', secondary=keywords_and_additional_thab, backref=db.backref('additional_team_hability', lazy='dynamic'))

    def __repr__(self):
        return '<Keyword {}>'.format(self.key_name)

#class Team_Habilities(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    teamh_name = db.Column(db.String(20), index=True)
#    teamh_description = db.Column(db.String(300), index=True)
#
#    def __repr__(self):
#        return '<Team Hability {}>'.format(self.teamh_name)

#class Add_Team_Habilities(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    add_teamh_name = db.Column(db.String(20), index=True)
#    add_teamh_point = db.Column(db.Integer, index=True)
#    add_teamh_description = db.Column(db.String(300), index=True)
#
#    def __repr__(self):
#        return '<Additional Team Hability {}>'.format(self.add_teamh_name)
