"""V1

Revision ID: 20250108_V1
Revises: 
Create Date: 2025-01-08 11:45:17.497487+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20250108_V1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('account_id')
    )
    op.create_table('knihy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nazev', sa.String(length=100), nullable=False),
    sa.Column('iban', sa.String(length=20), nullable=False),
    sa.Column('popisek', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('iban')
    )
    op.create_table('roles',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('role_id')
    )
    op.create_table('spz',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spz', sa.Text(), nullable=False),
    sa.Column('typ_vozidla', sa.Text(), nullable=False),
    sa.Column('datum_zarazeni', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('uzivatele',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('surename', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('evidence_vypujcek',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kniha_id', sa.Integer(), nullable=False),
    sa.Column('jmeno', sa.String(length=100), nullable=False),
    sa.Column('datum_narozeni', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['kniha_id'], ['knihy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Text(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('confirmed', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.account_id'], ),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('users_x_roles',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('assigned_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'role_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_x_roles')
    op.drop_table('users')
    op.drop_table('evidence_vypujcek')
    op.drop_table('uzivatele')
    op.drop_table('spz')
    op.drop_table('roles')
    op.drop_table('knihy')
    op.drop_table('accounts')
    # ### end Alembic commands ###