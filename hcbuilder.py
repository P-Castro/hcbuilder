from app import app, db
from app.models import User, Collection, Units, Dial_Move, Dial_Atack, Dial_Defense, Dial_Damage

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Collection': Collection, 'Units': Units,
            'Dial_Move': Dial_Move, 'Dial_Atack': Dial_Atack, 'Dial_Defense': Dial_Defense,
            'Dial_damage': Dial_damage}
