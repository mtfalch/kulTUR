"""empty message

Revision ID: 13e1006e884e
Revises: 14e10e3aa7f4
Create Date: 2019-03-08 13:19:51.729769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13e1006e884e'
down_revision = '14e10e3aa7f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('sex', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'sex')
    # ### end Alembic commands ###