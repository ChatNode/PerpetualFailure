"""Add User authentication policy

Revision ID: 51abb7077d9e
Revises: 15f55946909
Create Date: 2014-11-17 22:51:57.129062

"""

# revision identifiers, used by Alembic.
revision = '51abb7077d9e'
down_revision = '15f55946909'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('authn_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Text(), nullable=False),
    sa.Column('hash', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('authn_user')
