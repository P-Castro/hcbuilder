"""relção units, dials tables

Revision ID: ec9c2be7cb4a
Revises: 0418050c9f0a
Create Date: 2018-06-06 10:04:09.303476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec9c2be7cb4a'
down_revision = '0418050c9f0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dial__atack',
    sa.Column('datack_id', sa.Integer(), nullable=False),
    sa.Column('datack_pos1', sa.Integer(), nullable=True),
    sa.Column('datack_pos2', sa.Integer(), nullable=True),
    sa.Column('datack_pos3', sa.Integer(), nullable=True),
    sa.Column('datack_pos4', sa.Integer(), nullable=True),
    sa.Column('datack_pos5', sa.Integer(), nullable=True),
    sa.Column('datack_pos6', sa.Integer(), nullable=True),
    sa.Column('datack_pos7', sa.Integer(), nullable=True),
    sa.Column('datack_pos8', sa.Integer(), nullable=True),
    sa.Column('datack_pos9', sa.Integer(), nullable=True),
    sa.Column('datack_pos10', sa.Integer(), nullable=True),
    sa.Column('datack_pos11', sa.Integer(), nullable=True),
    sa.Column('datack_pos12', sa.Integer(), nullable=True),
    sa.Column('datack_cor1', sa.String(length=30), nullable=True),
    sa.Column('datack_cor2', sa.String(length=30), nullable=True),
    sa.Column('datack_cor3', sa.String(length=30), nullable=True),
    sa.Column('datack_cor4', sa.String(length=30), nullable=True),
    sa.Column('datack_cor5', sa.String(length=30), nullable=True),
    sa.Column('datack_cor6', sa.String(length=30), nullable=True),
    sa.Column('datack_cor7', sa.String(length=30), nullable=True),
    sa.Column('datack_cor8', sa.String(length=30), nullable=True),
    sa.Column('datack_cor9', sa.String(length=30), nullable=True),
    sa.Column('datack_cor10', sa.String(length=30), nullable=True),
    sa.Column('datack_cor11', sa.String(length=30), nullable=True),
    sa.Column('datack_cor12', sa.String(length=30), nullable=True),
    sa.Column('units_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['units_id'], ['units.units_id'], ),
    sa.PrimaryKeyConstraint('datack_id')
    )
    op.create_index(op.f('ix_dial__atack_datack_cor1'), 'dial__atack', ['datack_cor1'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor10'), 'dial__atack', ['datack_cor10'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor11'), 'dial__atack', ['datack_cor11'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor12'), 'dial__atack', ['datack_cor12'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor2'), 'dial__atack', ['datack_cor2'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor3'), 'dial__atack', ['datack_cor3'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor4'), 'dial__atack', ['datack_cor4'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor5'), 'dial__atack', ['datack_cor5'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor6'), 'dial__atack', ['datack_cor6'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor7'), 'dial__atack', ['datack_cor7'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor8'), 'dial__atack', ['datack_cor8'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_cor9'), 'dial__atack', ['datack_cor9'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos1'), 'dial__atack', ['datack_pos1'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos10'), 'dial__atack', ['datack_pos10'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos11'), 'dial__atack', ['datack_pos11'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos12'), 'dial__atack', ['datack_pos12'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos2'), 'dial__atack', ['datack_pos2'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos3'), 'dial__atack', ['datack_pos3'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos4'), 'dial__atack', ['datack_pos4'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos5'), 'dial__atack', ['datack_pos5'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos6'), 'dial__atack', ['datack_pos6'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos7'), 'dial__atack', ['datack_pos7'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos8'), 'dial__atack', ['datack_pos8'], unique=False)
    op.create_index(op.f('ix_dial__atack_datack_pos9'), 'dial__atack', ['datack_pos9'], unique=False)
    op.create_table('dial__damage',
    sa.Column('ddamage_id', sa.Integer(), nullable=False),
    sa.Column('ddamage_pos1', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos2', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos3', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos4', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos5', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos6', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos7', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos8', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos9', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos10', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos11', sa.Integer(), nullable=True),
    sa.Column('ddamage_pos12', sa.Integer(), nullable=True),
    sa.Column('ddamage_cor1', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor2', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor3', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor4', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor5', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor6', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor7', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor8', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor9', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor10', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor11', sa.String(length=30), nullable=True),
    sa.Column('ddamage_cor12', sa.String(length=30), nullable=True),
    sa.Column('units_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['units_id'], ['units.units_id'], ),
    sa.PrimaryKeyConstraint('ddamage_id')
    )
    op.create_index(op.f('ix_dial__damage_ddamage_cor1'), 'dial__damage', ['ddamage_cor1'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor10'), 'dial__damage', ['ddamage_cor10'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor11'), 'dial__damage', ['ddamage_cor11'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor12'), 'dial__damage', ['ddamage_cor12'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor2'), 'dial__damage', ['ddamage_cor2'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor3'), 'dial__damage', ['ddamage_cor3'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor4'), 'dial__damage', ['ddamage_cor4'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor5'), 'dial__damage', ['ddamage_cor5'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor6'), 'dial__damage', ['ddamage_cor6'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor7'), 'dial__damage', ['ddamage_cor7'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor8'), 'dial__damage', ['ddamage_cor8'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_cor9'), 'dial__damage', ['ddamage_cor9'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos1'), 'dial__damage', ['ddamage_pos1'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos10'), 'dial__damage', ['ddamage_pos10'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos11'), 'dial__damage', ['ddamage_pos11'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos12'), 'dial__damage', ['ddamage_pos12'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos2'), 'dial__damage', ['ddamage_pos2'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos3'), 'dial__damage', ['ddamage_pos3'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos4'), 'dial__damage', ['ddamage_pos4'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos5'), 'dial__damage', ['ddamage_pos5'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos6'), 'dial__damage', ['ddamage_pos6'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos7'), 'dial__damage', ['ddamage_pos7'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos8'), 'dial__damage', ['ddamage_pos8'], unique=False)
    op.create_index(op.f('ix_dial__damage_ddamage_pos9'), 'dial__damage', ['ddamage_pos9'], unique=False)
    op.create_table('dial__defense',
    sa.Column('ddefense_id', sa.Integer(), nullable=False),
    sa.Column('ddefense_pos1', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos2', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos3', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos4', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos5', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos6', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos7', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos8', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos9', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos10', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos11', sa.Integer(), nullable=True),
    sa.Column('ddefense_pos12', sa.Integer(), nullable=True),
    sa.Column('ddefense_cor1', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor2', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor3', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor4', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor5', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor6', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor7', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor8', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor9', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor10', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor11', sa.String(length=30), nullable=True),
    sa.Column('ddefense_cor12', sa.String(length=30), nullable=True),
    sa.Column('units_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['units_id'], ['units.units_id'], ),
    sa.PrimaryKeyConstraint('ddefense_id')
    )
    op.create_index(op.f('ix_dial__defense_ddefense_cor1'), 'dial__defense', ['ddefense_cor1'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor10'), 'dial__defense', ['ddefense_cor10'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor11'), 'dial__defense', ['ddefense_cor11'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor12'), 'dial__defense', ['ddefense_cor12'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor2'), 'dial__defense', ['ddefense_cor2'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor3'), 'dial__defense', ['ddefense_cor3'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor4'), 'dial__defense', ['ddefense_cor4'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor5'), 'dial__defense', ['ddefense_cor5'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor6'), 'dial__defense', ['ddefense_cor6'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor7'), 'dial__defense', ['ddefense_cor7'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor8'), 'dial__defense', ['ddefense_cor8'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_cor9'), 'dial__defense', ['ddefense_cor9'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos1'), 'dial__defense', ['ddefense_pos1'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos10'), 'dial__defense', ['ddefense_pos10'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos11'), 'dial__defense', ['ddefense_pos11'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos12'), 'dial__defense', ['ddefense_pos12'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos2'), 'dial__defense', ['ddefense_pos2'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos3'), 'dial__defense', ['ddefense_pos3'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos4'), 'dial__defense', ['ddefense_pos4'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos5'), 'dial__defense', ['ddefense_pos5'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos6'), 'dial__defense', ['ddefense_pos6'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos7'), 'dial__defense', ['ddefense_pos7'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos8'), 'dial__defense', ['ddefense_pos8'], unique=False)
    op.create_index(op.f('ix_dial__defense_ddefense_pos9'), 'dial__defense', ['ddefense_pos9'], unique=False)
    op.drop_index('ix_dial_defense_ddefense_cor1', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor10', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor11', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor12', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor2', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor3', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor4', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor5', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor6', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor7', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor8', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_cor9', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos1', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos10', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos11', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos12', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos2', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos3', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos4', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos5', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos6', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos7', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos8', table_name='dial_defense')
    op.drop_index('ix_dial_defense_ddefense_pos9', table_name='dial_defense')
    op.drop_table('dial_defense')
    op.drop_index('ix_dial_atack_datack_cor1', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor10', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor11', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor12', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor2', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor3', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor4', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor5', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor6', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor7', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor8', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_cor9', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos1', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos10', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos11', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos12', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos2', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos3', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos4', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos5', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos6', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos7', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos8', table_name='dial_atack')
    op.drop_index('ix_dial_atack_datack_pos9', table_name='dial_atack')
    op.drop_table('dial_atack')
    op.drop_index('ix_dial_damage_ddamage_cor1', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor10', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor11', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor12', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor2', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor3', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor4', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor5', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor6', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor7', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor8', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_cor9', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos1', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos10', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos11', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos12', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos2', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos3', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos4', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos5', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos6', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos7', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos8', table_name='dial_damage')
    op.drop_index('ix_dial_damage_ddamage_pos9', table_name='dial_damage')
    op.drop_table('dial_damage')
    op.add_column('dial__move', sa.Column('units_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'dial__move', 'units', ['units_id'], ['units_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dial__move', type_='foreignkey')
    op.drop_column('dial__move', 'units_id')
    op.create_table('dial_damage',
    sa.Column('ddamage_id', sa.INTEGER(), nullable=False),
    sa.Column('ddamage_pos1', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos2', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos3', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos4', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos5', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos6', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos7', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos8', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos9', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos10', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos11', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_pos12', sa.INTEGER(), nullable=True),
    sa.Column('ddamage_cor1', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor2', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor3', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor4', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor5', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor6', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor7', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor8', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor9', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor10', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor11', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddamage_cor12', sa.VARCHAR(length=30), nullable=True),
    sa.PrimaryKeyConstraint('ddamage_id')
    )
    op.create_index('ix_dial_damage_ddamage_pos9', 'dial_damage', ['ddamage_pos9'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos8', 'dial_damage', ['ddamage_pos8'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos7', 'dial_damage', ['ddamage_pos7'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos6', 'dial_damage', ['ddamage_pos6'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos5', 'dial_damage', ['ddamage_pos5'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos4', 'dial_damage', ['ddamage_pos4'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos3', 'dial_damage', ['ddamage_pos3'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos2', 'dial_damage', ['ddamage_pos2'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos12', 'dial_damage', ['ddamage_pos12'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos11', 'dial_damage', ['ddamage_pos11'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos10', 'dial_damage', ['ddamage_pos10'], unique=False)
    op.create_index('ix_dial_damage_ddamage_pos1', 'dial_damage', ['ddamage_pos1'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor9', 'dial_damage', ['ddamage_cor9'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor8', 'dial_damage', ['ddamage_cor8'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor7', 'dial_damage', ['ddamage_cor7'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor6', 'dial_damage', ['ddamage_cor6'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor5', 'dial_damage', ['ddamage_cor5'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor4', 'dial_damage', ['ddamage_cor4'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor3', 'dial_damage', ['ddamage_cor3'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor2', 'dial_damage', ['ddamage_cor2'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor12', 'dial_damage', ['ddamage_cor12'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor11', 'dial_damage', ['ddamage_cor11'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor10', 'dial_damage', ['ddamage_cor10'], unique=False)
    op.create_index('ix_dial_damage_ddamage_cor1', 'dial_damage', ['ddamage_cor1'], unique=False)
    op.create_table('dial_atack',
    sa.Column('datack_id', sa.INTEGER(), nullable=False),
    sa.Column('datack_pos1', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos2', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos3', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos4', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos5', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos6', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos7', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos8', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos9', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos10', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos11', sa.INTEGER(), nullable=True),
    sa.Column('datack_pos12', sa.INTEGER(), nullable=True),
    sa.Column('datack_cor1', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor2', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor3', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor4', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor5', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor6', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor7', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor8', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor9', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor10', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor11', sa.VARCHAR(length=30), nullable=True),
    sa.Column('datack_cor12', sa.VARCHAR(length=30), nullable=True),
    sa.PrimaryKeyConstraint('datack_id')
    )
    op.create_index('ix_dial_atack_datack_pos9', 'dial_atack', ['datack_pos9'], unique=False)
    op.create_index('ix_dial_atack_datack_pos8', 'dial_atack', ['datack_pos8'], unique=False)
    op.create_index('ix_dial_atack_datack_pos7', 'dial_atack', ['datack_pos7'], unique=False)
    op.create_index('ix_dial_atack_datack_pos6', 'dial_atack', ['datack_pos6'], unique=False)
    op.create_index('ix_dial_atack_datack_pos5', 'dial_atack', ['datack_pos5'], unique=False)
    op.create_index('ix_dial_atack_datack_pos4', 'dial_atack', ['datack_pos4'], unique=False)
    op.create_index('ix_dial_atack_datack_pos3', 'dial_atack', ['datack_pos3'], unique=False)
    op.create_index('ix_dial_atack_datack_pos2', 'dial_atack', ['datack_pos2'], unique=False)
    op.create_index('ix_dial_atack_datack_pos12', 'dial_atack', ['datack_pos12'], unique=False)
    op.create_index('ix_dial_atack_datack_pos11', 'dial_atack', ['datack_pos11'], unique=False)
    op.create_index('ix_dial_atack_datack_pos10', 'dial_atack', ['datack_pos10'], unique=False)
    op.create_index('ix_dial_atack_datack_pos1', 'dial_atack', ['datack_pos1'], unique=False)
    op.create_index('ix_dial_atack_datack_cor9', 'dial_atack', ['datack_cor9'], unique=False)
    op.create_index('ix_dial_atack_datack_cor8', 'dial_atack', ['datack_cor8'], unique=False)
    op.create_index('ix_dial_atack_datack_cor7', 'dial_atack', ['datack_cor7'], unique=False)
    op.create_index('ix_dial_atack_datack_cor6', 'dial_atack', ['datack_cor6'], unique=False)
    op.create_index('ix_dial_atack_datack_cor5', 'dial_atack', ['datack_cor5'], unique=False)
    op.create_index('ix_dial_atack_datack_cor4', 'dial_atack', ['datack_cor4'], unique=False)
    op.create_index('ix_dial_atack_datack_cor3', 'dial_atack', ['datack_cor3'], unique=False)
    op.create_index('ix_dial_atack_datack_cor2', 'dial_atack', ['datack_cor2'], unique=False)
    op.create_index('ix_dial_atack_datack_cor12', 'dial_atack', ['datack_cor12'], unique=False)
    op.create_index('ix_dial_atack_datack_cor11', 'dial_atack', ['datack_cor11'], unique=False)
    op.create_index('ix_dial_atack_datack_cor10', 'dial_atack', ['datack_cor10'], unique=False)
    op.create_index('ix_dial_atack_datack_cor1', 'dial_atack', ['datack_cor1'], unique=False)
    op.create_table('dial_defense',
    sa.Column('ddefense_id', sa.INTEGER(), nullable=False),
    sa.Column('ddefense_pos1', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos2', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos3', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos4', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos5', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos6', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos7', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos8', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos9', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos10', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos11', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_pos12', sa.INTEGER(), nullable=True),
    sa.Column('ddefense_cor1', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor2', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor3', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor4', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor5', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor6', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor7', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor8', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor9', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor10', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor11', sa.VARCHAR(length=30), nullable=True),
    sa.Column('ddefense_cor12', sa.VARCHAR(length=30), nullable=True),
    sa.PrimaryKeyConstraint('ddefense_id')
    )
    op.create_index('ix_dial_defense_ddefense_pos9', 'dial_defense', ['ddefense_pos9'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos8', 'dial_defense', ['ddefense_pos8'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos7', 'dial_defense', ['ddefense_pos7'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos6', 'dial_defense', ['ddefense_pos6'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos5', 'dial_defense', ['ddefense_pos5'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos4', 'dial_defense', ['ddefense_pos4'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos3', 'dial_defense', ['ddefense_pos3'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos2', 'dial_defense', ['ddefense_pos2'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos12', 'dial_defense', ['ddefense_pos12'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos11', 'dial_defense', ['ddefense_pos11'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos10', 'dial_defense', ['ddefense_pos10'], unique=False)
    op.create_index('ix_dial_defense_ddefense_pos1', 'dial_defense', ['ddefense_pos1'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor9', 'dial_defense', ['ddefense_cor9'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor8', 'dial_defense', ['ddefense_cor8'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor7', 'dial_defense', ['ddefense_cor7'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor6', 'dial_defense', ['ddefense_cor6'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor5', 'dial_defense', ['ddefense_cor5'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor4', 'dial_defense', ['ddefense_cor4'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor3', 'dial_defense', ['ddefense_cor3'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor2', 'dial_defense', ['ddefense_cor2'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor12', 'dial_defense', ['ddefense_cor12'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor11', 'dial_defense', ['ddefense_cor11'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor10', 'dial_defense', ['ddefense_cor10'], unique=False)
    op.create_index('ix_dial_defense_ddefense_cor1', 'dial_defense', ['ddefense_cor1'], unique=False)
    op.drop_index(op.f('ix_dial__defense_ddefense_pos9'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos8'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos7'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos6'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos5'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos4'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos3'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos2'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos12'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos11'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos10'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_pos1'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor9'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor8'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor7'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor6'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor5'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor4'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor3'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor2'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor12'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor11'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor10'), table_name='dial__defense')
    op.drop_index(op.f('ix_dial__defense_ddefense_cor1'), table_name='dial__defense')
    op.drop_table('dial__defense')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos9'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos8'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos7'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos6'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos5'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos4'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos3'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos2'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos12'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos11'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos10'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_pos1'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor9'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor8'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor7'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor6'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor5'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor4'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor3'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor2'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor12'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor11'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor10'), table_name='dial__damage')
    op.drop_index(op.f('ix_dial__damage_ddamage_cor1'), table_name='dial__damage')
    op.drop_table('dial__damage')
    op.drop_index(op.f('ix_dial__atack_datack_pos9'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos8'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos7'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos6'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos5'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos4'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos3'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos2'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos12'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos11'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos10'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_pos1'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor9'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor8'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor7'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor6'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor5'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor4'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor3'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor2'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor12'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor11'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor10'), table_name='dial__atack')
    op.drop_index(op.f('ix_dial__atack_datack_cor1'), table_name='dial__atack')
    op.drop_table('dial__atack')
    # ### end Alembic commands ###
