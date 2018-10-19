from app import app, db
from app.models import User, Collection, Dial_Movement, Dial_Attack, Dial_Defense, Dial_Damage, Pieces, Team, Keywords, Traits, team_and_pieces

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Collection': Collection, 'Dial_Movement': Dial_Movement,
            'Dial_Attack': Dial_Attack, 'Dial_Defense': Dial_Defense, 'Dial_Damage': Dial_Damage,
            'Pieces': Pieces, 'Team': Team, 'Keywords': Keywords, 'Traits': Traits, 'team_and_pieces':team_and_pieces}
