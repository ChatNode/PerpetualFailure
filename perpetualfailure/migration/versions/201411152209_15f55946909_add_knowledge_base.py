"""Add knowledge base

Revision ID: 15f55946909
Revises: 1dd1f9d85e2e
Create Date: 2014-11-15 22:09:02.701979

"""

# revision identifiers, used by Alembic.
revision = '15f55946909'
down_revision = '1dd1f9d85e2e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('knowledgebase_article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent', sa.Integer(), nullable=True),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['parent'], ['knowledgebase_article.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('knowledgebase_article_revision',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('parent', sa.Integer(), nullable=True),
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['knowledgebase_article.id'], ),
    sa.ForeignKeyConstraint(['parent'], ['knowledgebase_article_revision.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('knowledgebase_article_rel_revision',
    sa.Column('article', sa.Integer(), nullable=False),
    sa.Column('revision', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['article'], ['knowledgebase_article.id'], ),
    sa.ForeignKeyConstraint(['revision'], ['knowledgebase_article_revision.id'], ),
    sa.PrimaryKeyConstraint('article')
    )


def downgrade():
    op.drop_table('knowledgebase_article_rel_revision')
    op.drop_table('knowledgebase_article_revision')
    op.drop_table('knowledgebase_article')
