"""added favorite_characters

Revision ID: 6623fd4cc40b
Revises: 1d389452ba3e
Create Date: 2021-07-07 12:48:27.708599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6623fd4cc40b'
down_revision = '1d389452ba3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite_characters')
    # ### end Alembic commands ###
