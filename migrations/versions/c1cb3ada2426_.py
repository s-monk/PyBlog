"""empty message

Revision ID: c1cb3ada2426
Revises: 
Create Date: 2017-01-31 08:58:22.048222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1cb3ada2426'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entry', sa.Column('status', sa.SmallInteger(), server_default='0'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('entry', 'status')
    # ### end Alembic commands ###
