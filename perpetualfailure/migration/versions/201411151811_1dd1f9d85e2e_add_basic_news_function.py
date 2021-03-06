"""Add basic news function

Revision ID: 1dd1f9d85e2e
Revises: None
Create Date: 2014-11-15 18:11:03.997828

"""

# revision identifiers, used by Alembic.
revision = '1dd1f9d85e2e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('news_article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('news_article')
